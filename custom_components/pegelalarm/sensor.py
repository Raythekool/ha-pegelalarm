from datetime import timedelta
import aiohttp
import async_timeout
import logging

from homeassistant.components.sensor import SensorEntity
from homeassistant.const import UnitOfLength
from homeassistant.helpers.aiohttp_client import async_get_clientsession
from .const import DOMAIN, API_BASE

_LOGGER = logging.getLogger(__name__)
SCAN_INTERVAL = timedelta(minutes=30)

async def async_setup_entry(hass, entry, async_add_entities):
    station_id = entry.data["station_id"]
    async_add_entities([PagelalarmItSensor(hass, station_id)], True)

class PagelalarmItSensor(SensorEntity):
    """Sensore Pagelalarm-it dinamico."""

    def __init__(self, hass, station_id):
        self._station_id = station_id
        self._attr_unique_id = f"pagelalarm-it_{station_id}"
        self._attr_name = f"Pagelalarm-it {station_id}"
        self._attr_native_unit_of_measurement = "cm"
        self._attr_icon = "mdi:waves"
        self._state = None
        self._attrs = {}
        self.hass = hass

    async def async_update(self):
        url = f"{API_BASE}?commonid={self._station_id}&responseDetailLevel=high"
        session = async_get_clientsession(self.hass)
        try:
            async with async_timeout.timeout(10):
                async with session.get(url) as resp:
                    data = await resp.json()

            station = data["payload"]["stations"][0]
            measure = station["data"][0]
            self._state = measure["value"]
            self._attrs = {
                "source_date": measure["sourceDate"],
                "trend": station["trend"],
                "station_name": station["stationName"],
                "region": station["region"],
                "altitude": station["altitudeM"],
                "river": station["water"],
                "warning_level_cm": station["defaultWarnValueCm"],
                "alarm_level_cm": station["defaultAlarmValueCm"],
                "provider": station["dataProviderName"],
                "url": station["stationDetailUrl"]
            }

        except Exception as e:
            _LOGGER.warning(f"Errore aggiornando Pagelalarm-it {self._station_id}: {e}")
            self._state = None

    @property
    def native_value(self):
        return self._state

    @property
    def extra_state_attributes(self):
        return self._attrs

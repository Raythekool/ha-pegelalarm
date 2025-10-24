from homeassistant import config_entries
import voluptuous as vol
from .const import DOMAIN

class PegelalarmFlowHandler(config_entries.ConfigFlow, domain=DOMAIN):
    VERSION = 1

    async def async_step_user(self, user_input=None):
        if user_input is not None:
            return self.async_create_entry(
                title=f"Stazione {user_input['station_id']}",
                data=user_input
            )

        schema = vol.Schema({
            vol.Required("station_id", description="ID della stazione (commonid)"): str
        })

        return self.async_show_form(
            step_id="user",
            data_schema=schema,
            description_placeholders={"example": "emilia-romagna-900-it"}
        )

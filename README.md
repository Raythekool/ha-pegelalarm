# Home Assistant Pegelalarm Sensor

A custom Home Assistant integration to fetch river level data from [Pegelalarm](https://api.pegelalarm.at).  
The integration supports current level, historical data, trends, and additional metadata.

---

## 📦 Installation

This integration can be installed via [HACS](https://hacs.xyz/) or manually:

### HACS

1. Add this repository to HACS under "Custom Repositories" (category: Integration).
2. Install it via HACS.
3. Restart Home Assistant.

### Manual

1. Copy the contents of this repository to `config/custom_components/pegelalarm`.
2. Restart Home Assistant.

---

## ⚙️ Configuration

Add the integration in your `configuration.yaml` or via UI (once available).

### Example YAML configuration

```yaml
sensor:
    name: "Livello Fiumalbo Attuale"
    station_id: "emilia-romagna-900-it"
    scan_interval: 1800  # optional, in seconds
```

### Available configuration options

| Option          | Type   | Default  | Description                        |
| --------------- | ------ | -------- | ---------------------------------- |
| `station_id`    | string | required | Pegelalarm station ID (`commonid`) |
| `scan_interval` | int    | 1800     | Update interval in seconds         |

---

## 💡 Example Entities

| Entity                                  | Example Value                    | Description                                |
| --------------------------------------- | -------------------------------- | ------------------------------------------ |
| `sensor.livello_fiumalbo_attuale`       | `126.0 cm`                       | Current river level                        |
| `sensor.livello_fiumalbo_trend`         | `falling`                        | Current level trend                        |
| `sensor.livello_fiumalbo_allarme`       | `130 cm`                         | Warning threshold                          |
| `sensor.livello_fiumalbo_storico`       | `[102.0, 103.0, 104.0...]`       | Historical hourly values for the last days |
| `sensor.livello_fiumalbo_data_provider` | `"Homepage ARPA Emilia Romagna"` | Source of the data                         |

---
\n## 📝 Sensor Attributes

The current level sensor provides extra attributes:

| Attribute                | Example                                            | Description                 |
| ------------------------ | -------------------------------------------------- | --------------------------- |
| `station_name`           | `"Fiumalbo"`                                       | Human-readable station name |
| `water`                  | `"Scoltenna"`                                      | River name                  |
| `latitude`               | `44.17934`                                         | Latitude coordinate         |
| `longitude`              | `10.64917`                                         | Longitude coordinate        |
| `altitude_m`             | `944.0`                                            | Station altitude in meters  |
| `default_warn_value_cm`  | `130`                                              | Warning threshold           |
| `default_alarm_value_cm` | `170`                                              | Alarm threshold             |
| `trend`                  | `-10`                                              | Current trend (cm)          |
| `situation`              | `10`                                               | Situation value             |
| `modifier`               | `"https://allertameteo.regione.emilia-romagna.it"` | URL with more info          |
| `station_type`           | `"surfacewater"`                                   | Type of station             |
| `visibility`             | `"PUBLIC"`                                         | Data visibility             |
| `data_provider_name`     | `"Homepage ARPA Emilia Romagna"`                   | Data provider               |

---

## ⚡ Usage

You can use this sensor in dashboards, automations, or scripts.
\n### Example Lovelace card

```yaml
type: entities
title: Livello Fiumalbo
entities:
  - sensor.livello_fiumalbo_attuale
  - sensor.livello_fiumalbo_trend
```

Or with `mini-graph-card`:

```yaml
type: custom:mini-graph-card
entities:
  - sensor.livello_fiumalbo_storico
name: Storico Fiumalbo
show:
  graph: line
hours_to_show: 48
points_per_hour: 1

- The integration automatically fetches current and historical data from Pegelalarm API.
---

## 🛠 Development
- Clone this repository into `custom_components/pegelalarm`.
- Use a dev container or Home Assistant environment to test.
- For contributions, follow [HACS dev guidelines](https://www.hacs.xyz/docs/contribute/devcontainer/).

---

## 🏷 License
This project is licensed under the MIT License – see [LICENSE](LICENSE) for details.

---

## 🌐 Author

[Marco Dodaro](https://github.com/raythekool

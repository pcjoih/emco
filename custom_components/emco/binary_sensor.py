from homeassistant.components.binary_sensor import BinarySensorEntity
from homeassistant.core import HomeAssistant
from .const import DOMAIN
import logging

_LOGGER = logging.getLogger(__name__)

async def async_setup_platform(hass: HomeAssistant, config, async_add_entities, discovery_info=None):
    """Set up the binary sensor platform asynchronously."""
    communal_sensor = SerialBinarySensor(hass, "communal")
    front_sensor = SerialBinarySensor(hass, "front")
        
    async_add_entities([communal_sensor, front_sensor], True)
    
    hass.data[DOMAIN]["communal_sensor"] = communal_sensor
    hass.data[DOMAIN]["front_sensor"] = front_sensor

class SerialBinarySensor(BinarySensorEntity):
    """Representation of a Binary Sensor."""

    def __init__(self, hass, name):
        """Initialize the binary sensor."""
        self._hass = hass
        self._name = name
        self._state = False

    @property
    def name(self):
        """Return the name of the binary sensor."""
        return f"{DOMAIN}_{self._name}_binary_sensor"

    @property
    def is_on(self):
        """Return true if the binary sensor is on."""
        return self._state

    @property
    def unique_id(self):
        """Return a unique ID for this light."""
        return f"{self._name}_id"

    async def async_update(self):
        """Update the state of the sensor asynchronously."""
        pass

    def set_state(self, state: bool):
        """Set the state of the binary sensor."""
        _LOGGER.info(
            f"Setting {self._name} sensor state to {'on' if state else 'off'}."
        )
        self._state = state
        # 상태가 변경될 때, Home Assistant에 상태 업데이트를 알림
        self.async_write_ha_state()


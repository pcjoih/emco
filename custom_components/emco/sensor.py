import logging
from homeassistant.components.sensor import SensorEntity
from homeassistant.core import HomeAssistant
from homeassistant.helpers.dispatcher import async_dispatcher_connect
from .const import DOMAIN

_LOGGER = logging.getLogger(__name__)

async def async_setup_platform(hass: HomeAssistant, config, async_add_entities, discovery_info=None):
    """Set up the sensor platform asynchronously."""
    async_add_entities([EvSensor(hass, "ev_1_state"),
                        EvSensor(hass, "ev_1_floor"),
                        EvSensor(hass, "ev_2_state"),
                        EvSensor(hass, "ev_2_floor")], True)

class EvSensor(SensorEntity):
    """Representation of an Elevator Sensor."""

    def __init__(self, hass, name):
        """Initialize the sensor."""
        self._hass = hass
        self._name = name
        self._state = 'unknown'
        
        async_dispatcher_connect(self._hass, "ev_update_sensor", self._async_update_sensor)

    @property
    def name(self):
        """Return the name of the sensor."""
        return f"{DOMAIN}_{self._name}"

    @property
    def state(self):
        """Return the state of the sensor."""
        return self._state
    
    @property
    def unique_id(self):
        """Return a unique ID for this light."""
        return f"{self._name}_id"

    async def _async_update_sensor(self, name, state):
        """Asynchronously handle updates from the dispatcher."""
        if self._name == name:
            _LOGGER.info(f"Updating sensor {self._name}: {state}")
            self._state = state
            self.async_write_ha_state()

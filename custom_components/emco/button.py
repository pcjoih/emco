# emco/button.py
import logging
from homeassistant.components.button import ButtonEntity
from homeassistant.core import HomeAssistant
from homeassistant.helpers.typing import ConfigType
from .const import DOMAIN

_LOGGER = logging.getLogger(__name__)

async def async_setup_platform(hass: HomeAssistant, config, async_add_entities, discovery_info=None):
    """Set up the button platform asynchronously."""
    async_add_entities([EvCallButton(hass), 
                        SerialButton(hass, "communal_open"), 
                        SerialButton(hass, "front_open"),
                        SerialButton(hass, "front_start"),
                        SerialButton(hass, "front_stop")], True)

class EvCallButton(ButtonEntity):
    """Representation of a button to call the elevator service."""

    def __init__(self, hass):
        """Initialize the button."""
        self._hass = hass
        self._attr_name = "EV Call"
        self._attr_icon = "mdi:elevator"

    @property
    def name(self):
        """Return the name of the button."""
        return f"{DOMAIN}_ev_call_button"

    @property
    def unique_id(self):
        """Return a unique ID for this light."""
        return f"{DOMAIN}_ev_call_button_id"

    async def async_press(self):
        """Handle the button press."""
        _LOGGER.info("EV Call button pressed, calling emco.ev_call service.")
        # Call the ev_call service when the button is pressed
        await self._hass.services.async_call(DOMAIN, "ev_call")

class SerialButton(ButtonEntity):
    """Representation of a button to send serial commands for opening locks."""

    def __init__(self, hass, name):
        """Initialize the button."""
        self._hass = hass
        self._name = name
        self._attr_name = f"{name.capitalize().replace('_', ' ')} Button"
        self._attr_icon = "mdi:door-open" if "open" in name else "mdi:elevator"

    @property
    def name(self):
        """Return the name of the button."""
        return f"{DOMAIN}_{self._name}_button"

    @property
    def unique_id(self):
        """Return a unique ID for this light."""
        return f"{DOMAIN}_{self._name}_button_id"

    async def async_press(self):
        """Handle the button press."""
        _LOGGER.info(f"{self._attr_name} button pressed, calling send_serial_data service for {self._name}.")
        # Call the send_serial_data service with the appropriate lock_name     
        await self._hass.services.async_call(DOMAIN, "send_serial_data", {"lock_name": self._name})

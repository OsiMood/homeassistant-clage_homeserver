import logging
from datetime import timedelta
import voluptuous as vol

from homeassistant import config_entries
from homeassistant.core import callback
from homeassistant.const import CONF_HOST, CONF_SCAN_INTERVAL

from .const import (
    DOMAIN,
    CONF_HOMESERVER_IP_ADDRESS,
    CONF_HOMESERVER_ID,
    CONF_HEATER_ID,
    CONF_NAME,
)

_LOGGER = logging.getLogger(__name__)


DEFAULT_UPDATE_INTERVAL = timedelta(seconds=20)
MIN_UPDATE_INTERVAL = timedelta(seconds=10)


class ConfigFlowHandler(config_entries.ConfigFlow, domain=DOMAIN):
    """Config flow for clage_homeserver setup."""

    VERSION = 1

    @staticmethod
    @callback
    async def async_get_options_flow(config_entry):
        return OptionsFlowHandler(config_entry)

    async def async_step_user(self, info):
        if info is not None:
            _LOGGER.debug(info)
            return self.async_create_entry(title=info[CONF_NAME], data=info)

        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema(
                {
                    vol.Required(CONF_HOMESERVER_IP_ADDRESS): str,
                    vol.Required(CONF_HOMESERVER_ID): str,
                    vol.Required(CONF_HEATER_ID): str,
                }
            ),
        )

"""Configuration flow for the Laundry Coin Counter integration.

This module defines how the integration is configured via the UI.
"""


import voluptuous as vol

from homeassistant import config_entries

from .const import (
    CONF_COIN_VALUE,
    CONF_DRY_COST,
    CONF_WASH_COST,
    DEFAULT_COIN_VALUE,
    DEFAULT_DRY_COST,
    DEFAULT_WASH_COST,
    DOMAIN,
)


class MyLaundryConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow for My Laundry."""

    VERSION = 1
    CONNECTION_CLASS = config_entries.CONN_CLASS_LOCAL_POLL

    async def async_step_user(self, user_input=None):
        """Handle the initial step."""
        if user_input is not None:
            # Use the user input to set up the configuration
            return self.async_create_entry(title="My Laundry", data=user_input)

        # Default values for the form
        default_coin_value = DEFAULT_COIN_VALUE
        default_wash_cost = DEFAULT_WASH_COST
        default_dry_cost = DEFAULT_DRY_COST

        # Form fields
        fields = {
            vol.Required(CONF_COIN_VALUE, default=default_coin_value): vol.Coerce(
                float
            ),
            vol.Required(CONF_WASH_COST, default=default_wash_cost): vol.Coerce(int),
            vol.Required(CONF_DRY_COST, default=default_dry_cost): vol.Coerce(int),
        }

        return self.async_show_form(step_id="user", data_schema=vol.Schema(fields))

    # @staticmethod
    # @callback
    # def async_get_options_flow(config_entry):
    #     return OptionsFlowHandler(config_entry)

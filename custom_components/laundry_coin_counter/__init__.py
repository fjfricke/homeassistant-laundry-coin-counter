"""Initialization for the Laundry Coin Counter integration.

This module sets up the integration and its services in Home Assistant.
"""

import asyncio
import logging

from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant

from .const import (
    CONF_COIN_VALUE,
    CONF_DRY_COST,
    CONF_WASH_COST,
    DEFAULT_COIN_VALUE,
    DEFAULT_DRY_COST,
    DEFAULT_WASH_COST,
    DOMAIN,
)
from .services import (
    add_coins,
    run_dryer,
    run_washing_machine,
    set_total_coins,
    subtract_coins,
)

_LOGGER = logging.getLogger(__name__)

PLATFORMS = ["sensor"]


async def async_setup(hass: HomeAssistant, config: dict):
    """Set up the component from configuration.yaml (if any)."""
    return True


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry):
    """Set up the component from a config entry."""
    hass.data.setdefault(DOMAIN, {})

    # Load configuration from entry
    coin_value = entry.data.get(CONF_COIN_VALUE, DEFAULT_COIN_VALUE)
    wash_cost = entry.data.get(CONF_WASH_COST, DEFAULT_WASH_COST)
    dry_cost = entry.data.get(CONF_DRY_COST, DEFAULT_DRY_COST)

    # Initialize your sensors/services with the configuration
    hass.data[DOMAIN][entry.entry_id] = {
        "coin_value": coin_value,
        "wash_cost": wash_cost,
        "dry_cost": dry_cost,
    }

    for platform in PLATFORMS:
        hass.async_create_task(
            hass.config_entries.async_forward_entry_setup(entry, platform)
        )

    hass.services.async_register(DOMAIN, "add_coins", add_coins)
    hass.services.async_register(DOMAIN, "subtract_coins", subtract_coins)
    hass.services.async_register(DOMAIN, "set_total_coins", set_total_coins)
    hass.services.async_register(DOMAIN, "run_washing_machine", run_washing_machine)
    hass.services.async_register(DOMAIN, "run_dryer", run_dryer)

    return True


async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry):
    """Unload a config entry."""
    unload_ok = all(
        await asyncio.gather(
            *[
                hass.config_entries.async_forward_entry_unload(entry, platform)
                for platform in PLATFORMS
            ]
        )
    )

    if unload_ok:
        hass.data[DOMAIN].pop(entry.entry_id)

    return unload_ok

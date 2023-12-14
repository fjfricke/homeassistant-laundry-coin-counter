"""
This module `services.py` for the 'Laundry Coin Counter' Home Assistant integration
provides the services to manage a coin-operated laundry system.

It includes services to add or subtract coins, set a new total coin count, and operate the washing machine and dryer.
"""

from homeassistant.core import HomeAssistant

from .const import DOMAIN


async def add_coins(hass: HomeAssistant, call):
    """Service to add coins."""
    number_of_coins = call.data.get("number_of_coins")
    hass.data[DOMAIN]["total_coins"] += number_of_coins
    # Trigger an update to any relevant entities


async def subtract_coins(hass: HomeAssistant, call):
    """Service to subtract coins."""
    number_of_coins = call.data.get("number_of_coins")
    hass.data[DOMAIN]["total_coins"] = max(
        hass.data[DOMAIN]["total_coins"] - number_of_coins, 0
    )
    # Trigger an update to any relevant entities


async def set_total_coins(hass: HomeAssistant, call):
    """Service to set a new total of coins."""
    new_total = call.data.get("new_total")
    hass.data[DOMAIN]["total_coins"] = max(new_total, 0)
    # Trigger an update to any relevant entities


async def run_washing_machine(hass: HomeAssistant, call):
    """Service to run the washing machine."""
    if hass.data[DOMAIN]["total_coins"] >= hass.data[DOMAIN]["wash_cost"]:
        hass.data[DOMAIN]["total_coins"] -= hass.data[DOMAIN]["wash_cost"]
        # Trigger an update to any relevant entities


async def run_dryer(hass: HomeAssistant, call):
    """Service to run the dryer."""
    if hass.data[DOMAIN]["total_coins"] >= hass.data[DOMAIN]["dry_cost"]:
        hass.data[DOMAIN]["total_coins"] -= hass.data[DOMAIN]["dry_cost"]
        # Trigger an update to any relevant entities

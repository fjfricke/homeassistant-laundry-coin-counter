"""Sensor module for the Laundry Coin Counter integration.

This module defines sensors for tracking coins, washes, and dries.
"""


from homeassistant.components.sensor import SensorEntity

from .const import CONF_COIN_VALUE, CONF_DRY_COST, CONF_WASH_COST, DOMAIN


def setup_platform(hass, config, add_entities, discovery_info=None):
    """Set up the sensor platform."""
    if discovery_info is None:
        return

    coin_value = hass.data[DOMAIN][discovery_info[CONF_COIN_VALUE]]
    wash_cost = hass.data[DOMAIN][discovery_info[CONF_WASH_COST]]
    dry_cost = hass.data[DOMAIN][discovery_info[CONF_DRY_COST]]

    sensors = [
        LaundrySensor(hass, coin_value, wash_cost, dry_cost, "Coins Available"),
        LaundrySensor(hass, coin_value, wash_cost, dry_cost, "Washes Remaining"),
        LaundrySensor(hass, coin_value, wash_cost, dry_cost, "Dries Remaining"),
    ]

    add_entities(sensors, True)


class LaundrySensor(SensorEntity):
    """Representation of the LaundrySensor."""

    def __init__(self, hass, coin_value, wash_cost, dry_cost, sensor_type):
        """Initialize the sensor."""
        self._hass = hass
        self._coin_value = coin_value
        self._wash_cost = wash_cost
        self._dry_cost = dry_cost
        self._type = sensor_type
        self._total_coins = 0
        self._attr_native_unit_of_measurement = (
            "coins" if sensor_type == "Coins Available" else "cycles"
        )
        # self._state = None
        self.update()

    @property
    def name(self):
        """Return the name of the sensor."""
        return f"Laundry {self._type}"

    # @property
    # def state(self):
    #     """Return the state of the sensor."""
    #     return self._state

    @property
    def native_value(self):
        """Return the native value of the sensor."""
        if self._type == "Coins Available":
            return self._calculate_coins()
        if self._type == "Washes Remaining":
            return self._calculate_washes()
        if self._type == "Dries Remaining":
            return self._calculate_dries()

    # @property
    # def unit_of_measurement(self):
    #     """Return the unit of measurement."""
    #     if self._type == "Coins Available":
    #         return "coins"
    #     return "cycles"

    def update(self):
        """Fetch new state data for the sensor."""
        # This is where you'll fetch or calculate the new state
        # For example, calculating the remaining washes or dries
        if self._type == "Coins Available":
            self._state = self._calculate_coins()
        elif self._type == "Washes Remaining":
            self._state = self._calculate_washes()
        elif self._type == "Dries Remaining":
            self._state = self._calculate_dries()

    def _calculate_coins(self):
        """Calculate and return the total number of coins."""
        return self._total_coins

    def _calculate_washes(self):
        """Calculate and return the number of washes remaining."""
        if self._coin_value == 0:  # Prevent division by zero
            return 0
        return int(self._total_coins / self._wash_cost)

    def _calculate_dries(self):
        """Calculate and return the number of dries remaining."""
        if self._coin_value == 0:  # Prevent division by zero
            return 0
        return int(self._total_coins / self._dry_cost)

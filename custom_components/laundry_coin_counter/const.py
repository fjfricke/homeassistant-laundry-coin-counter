"""Constants for integration_blueprint."""
from logging import Logger, getLogger

LOGGER: Logger = getLogger(__package__)

NAME = "Laundry Coin Counter"
DOMAIN = "laundry_coin_counter"
VERSION = "0.0.1"

# Constants for my_laundry integration

# Configuration keys
CONF_COIN_VALUE = "coin_value"
CONF_WASH_COST = "wash_cost"
CONF_DRY_COST = "dry_cost"

# Default values
DEFAULT_COIN_VALUE = 0.50  # 50 cents
DEFAULT_WASH_COST = 3  # 3 coins for a wash
DEFAULT_DRY_COST = 2  # 2 coins for a dry

# Laundry Coin Counter Integration for Home Assistant

## Overview
The Laundry Coin Counter integration for Home Assistant allows you to manage a coin-operated laundry system, including tracking the number of coins inserted and calculating the number of washes and dries available based on the coin count.

## Features
- Track the total number of coins in your laundry coin counter.
- Calculate available washes and dries based on the coin count.
- Add or subtract coins from the total count.
- Run the washing machine or dryer, automatically subtracting the appropriate number of coins.
- Set a new total coin count directly.

## Installation
To install this integration, follow these steps:
1. Download the `laundry_coin_counter` folder.
2. Place it into your `custom_components` directory in your Home Assistant installation.
3. Restart Home Assistant.

## Configuration
After installation, configure the integration via the Home Assistant UI:
1. Go to Configuration > Integrations.
2. Click on "Add Integration" and search for "Laundry Coin Counter".
3. Enter the necessary details, such as coin value, wash cost, and dry cost.

## Services
This integration offers the following services:

### `laundry_coin_counter.add_coins`
Add coins to your laundry system.
- `number_of_coins`: The number of coins to add.

### `laundry_coin_counter.subtract_coins`
Subtract coins from your laundry system.
- `number_of_coins`: The number of coins to subtract.

### `laundry_coin_counter.set_total_coins`
Set a new total of coins.
- `new_total`: The new total number of coins.

### `laundry_coin_counter.run_washing_machine`
Run the washing machine. This will subtract the cost from your coin total.

### `laundry_coin_counter.run_dryer`
Run the dryer. This will also subtract the appropriate cost from your coin total.

## Support
For support, issues, or feature requests, please open an issue on the [GitHub repository](https://github.com/fjfricke/homeassistant-laundry-coin-counter).

## Contribution
Contributions to this integration are welcome.

## License
This integration is released under the MIT License.

# Richmond Police Active Call Tracker

The Richmond Police Active Call Tracker is a Python script designed to monitor the Richmond Police Department's active call webpage. It periodically checks for updates and sends the latest call information to a Discord webhook in real-time.

## Features

- Automated monitoring of the Richmond Police Department's active call webpage.
- Periodic checks for new call data every 5 seconds.
- Integration with Discord webhooks for instant notifications.
- Customizable message formatting for Discord notifications.

## Usage

1. **Clone the Repository** or copy the script to your local environment.

2. **Install Required Packages**:

   ```bash
   pip install selenium beautifulsoup4 discord-webhook

# Discord Tracker Bot
### Released February 2026
### Version 1.0.0
### Updated February 2026

<br/>

## Description
Discord Tracker Bot is a template to create a Discord bot that pings a specific
user and records their responses. Pings a user a certain number of times each
by sending them a DM on Discord, and records every response the user has given
since the last ping.

<br/>

## Requirements
Requires Linux, as well as rtcwake, which must also be supported by your
hardware. Also requires the Discord library for Python.

<br/>

## License
This project is licensed under the MIT Licensed, also called the Expat License,
as detailed in LICENSE.

<br/>

## Usage

 - Set up your variables in `tracker_bot_settings.py`.
 - Set up the files defined in your settings, namely `RESULTS_PATH`,
   `CRONFILE_PATH`, `LOG_PATH`.
 - Copy all Python files to /usr/bin/, the command `sudo cp tracker* /usr/bin/`
   should suffice.
 - Schdule the first run of `tracker_bot_cron.py` manually, either by running it
   yourself before `DAY_START`, or by scheduling it with cron and booting the
   machine with rtcwake.

The user should include commas in their messages if and only if they want to
denote separate categories to be logged.
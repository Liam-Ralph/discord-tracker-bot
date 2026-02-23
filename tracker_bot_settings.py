# Copyright (C) 2026 Liam Ralph
# https://github.com/liam-ralph

# This program, including this file, is licensed under the
# MIT (Expat) License.
# See LICENSE or this project's source for more information.
# Project source: https://github.com/liam-ralph/discord-tracker-bot

# Discord Tracker Bot, a simple Discord bot that pings a
# user and trackers their responses.


# Imports

import datetime


# Static Variables

# Discord Token

DISCORD_TOKEN = "Enter Discord token here"
USER_ID = "Enter target user ID here" # The ID of the user who will be pinged

# Paths

BASE_PATH = "/home/user/discord-tracker-bot/" # Not required
RESULTS_PATH = BASE_PATH + "results.csv" # Path for storing user response data
CRONFILE_PATH = BASE_PATH + "cronfile.txt" # Path used to temporarily write cron jobs
LOG_PATH = BASE_PATH + "log.txt" # Required only for log_message

# Ping Information

PINGS_PER_DAY = 10 # Number of randomly timed pings per day
DAY_START = 8 * 60 # The start of the day, in minutes since 00:00,
                   # must be at least PRE_BOOT_PING minutes past 00:00
DAY_END = 20 * 60 # The end of the day, in minutes since 00:00, must be at least
                  # DAY_START + MIN_PING_GAP * PINGS_PER_DAY
MIN_PING_GAP = 30 # Minimum number of minutes between pings, must be greater
                  # than PRE_PING_BOOT
PRE_PING_BOOT = 5 # Number of minutes before each ping (and DAY_START for cron
                  # setup) to boot the machine


# Functions

def log_message(name, message):
    """
    
    """

    text = str(datetime.datetime.now()) + " " + name + ": " + message
    print(text)
    with open(LOG_PATH, "a") as logfile:
        logfile.write(text + "\n")
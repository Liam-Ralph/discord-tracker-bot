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
USER_ID = "Enter target user ID here"

# Paths

BASE_PATH = "/home/user/discord-tracker-bot/" # Not required
RESULTS_PATH = BASE_PATH + "results.csv"
CRONFILE_PATH = BASE_PATH + "cronfile.txt"
LOG_PATH = BASE_PATH + "log.txt" # Required only for log_message

# Ping Information

PINGS_PER_DAY = 10
DAY_START = 8 * 60
DAY_END = 20 * 60


# Functions

def log_message(name, message):

    text = str(datetime.datetime.now()) + " " + name + ": " + message
    print(text)
    with open(LOG_PATH, "a") as logfile:
        logfile.write(text + "\n")
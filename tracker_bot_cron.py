# Copyright (C) 2026 Liam Ralph
# https://github.com/liam-ralph

# This program, including this file, is licensed under the
# MIT (Expat) License.
# See LICENSE or this project's source for more information.
# Project source: https://github.com/liam-ralph/discord-tracker-bot

# Discord Tracker Bot, a simple Discord bot that pings a
# user and trackers their responses.


# Imports

import random
import subprocess

from tracker_bot_settings import *


# Functions

def string_to_minutes(string):

    str_hour, str_min = string.split(":")
    return int(str_hour) * 60 + int(str_min)


# Main Function

def main():

    # Calculate Random Ping Times

    start_time = string_to_minutes(DAY_START)
    cron_start_time = start_time - 30
    end_time = string_to_minutes(DAY_END)
    ping_times = []
    while len(ping_times) < PINGS_PER_DAY:
        random_time = random.randint(start_time, end_time)
        acceptable_ping = True
        for ping_time in ping_times:
            if abs(ping_time - random_time) > 30:
                acceptable_ping = False
                break
        if acceptable_ping:
            ping_times.append(random_time)
    ping_times.sort()

    # Create Cron Jobs

    with open(CRONFILE_PATH, "w") as cronfile:

        for i in range(len(ping_times)):
            ping_time = ping_times[i]
            hours = ping_time // 60
            minutes = ping_time % 60
            if i != len(ping_times) - 1:
                off_time = ping_times[i + 1] - ping_time - 15
            else:
                off_time = cron_start_time + 24 * 60 - ping_time - 15
            cronfile.write(
                str(minutes) + " " + str(hours) +
                " * * * root python3 /usr/bin/tracker_bot.py & && " +
                "/usr/sbin/rtcwake -m off -s " + str(off_time) + "\n"
            )

        hours = start_time // 60
        minutes = start_time % 60
        cronfile.write(
            str(minutes) + " " + str(hours) + " * * * root python3 /usr/bin/tracker_bot_cron.py &\n"
        )

    subprocess.run(["crontab", CRONFILE_PATH])

    # Schedule RTCWake for First Ping

    log_message(__file__, "Cron jobs set")

    off_time = ping_times[i] - cron_start_time - 15
    subprocess.run(["/usr/sbin/rtcwake", "-m", "off", "-s", str(off_time)])

main()
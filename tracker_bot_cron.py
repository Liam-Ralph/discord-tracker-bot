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
    """
    Convert a given string of format "HH:MM" into a number of minutes since
    00:00. Must be a 24-hour time.

    :param string: The string, of format "HH:MM", to be converted.
    """

    str_hour, str_min = string.split(":")
    return int(str_hour) * 60 + int(str_min)

def minutes_to_string(mins_tot):
    """
    Converts a time to a 24-hour time string of format "HH:MM". Midnight is
    00:00.

    :param mins_tot: The time, in minutes since 00:00, to be converted.
    """

    hours = "00" if mins_tot == 24 * 60 else str(mins_tot // 60)
    return hours.rjust(2, "0") + ":" + str(mins_tot % 60).rjust(2, "0")

def datetime_to_cron(date):
    """
    Converts a date of format "YYYY-MM-DD" to the format "dom mon dow" for
    scheduling a cron job. dom, mon, and dow stand for day of month, month, and
    day of week respectively. dow is 0 on Sunday.

    :param date: The date to be converted.
    """

    _, month, day = str(date).split("-")
    weekday = str(date.isoweekday() % 7)
    return f"{day.rjust(2, "0")} {month.rjust(2, "0")} {weekday}"


# Main Function

def main():
    """
    Main function, sets ping times and schedules cron jobs.
    """

    # Calculate Random Ping Times

    ping_times = []
    while len(ping_times) < PINGS_PER_DAY:
        random_time = random.randint(DAY_START, DAY_END)
        acceptable_ping = True
        for ping_time in ping_times:
            if abs(ping_time - random_time) < MIN_PING_GAP:
                acceptable_ping = False
                break
        if acceptable_ping:
            ping_times.append(random_time)
    ping_times.sort()

    # Create Cron Jobs

    with open(CRONFILE_PATH, "w") as cronfile:

        today = datetime.date.today()
        tomorrow = today + datetime.timedelta(days = 1)

        for i in range(len(ping_times)):

            ping_time = ping_times[i]
            hours = ping_time // 60
            minutes = ping_time % 60

            if i != len(ping_times) - 1:
                date_string = (
                    str(today) + " " + minutes_to_string(ping_times[i + 1] - PRE_PING_BOOT)
                )
            else:
                date_string = str(tomorrow) + " " + minutes_to_string(DAY_START - PRE_PING_BOOT * 2)

            cronfile.write(
                f"{str(minutes)} {str(hours)} {datetime_to_cron(today)} " +
                "python3 /usr/bin/tracker_bot.py && " +
                "/usr/sbin/rtcwake -m off --date \"" + date_string + "\"\n"
            )

        hours = (DAY_START - PRE_PING_BOOT) // 60
        minutes = (DAY_START - PRE_PING_BOOT) % 60
        cronfile.write(
            f"{str(minutes)} {str(hours)} {datetime_to_cron(tomorrow)} " +
            "python3 /usr/bin/tracker_bot_cron.py\n"
        )

    subprocess.run(["crontab", CRONFILE_PATH])

    # Schedule RTCWake for First Ping

    log_message(__file__, "Cron jobs set")

    subprocess.run([
        "/usr/sbin/rtcwake", "-m", "off", "--date",
        str(today) + " " + minutes_to_string(ping_times[0] - PRE_PING_BOOT)
    ])

main()
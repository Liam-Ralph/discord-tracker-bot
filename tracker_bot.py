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
import discord

from tracker_bot_settings import *


# Main Function

def main():

    @client.event
    async def on_ready():

        log_message(__file__, client.user.name + " online")

        # Read New Messages

        user = await client.fetch_user(USER_ID)
        channel = await user.create_dm()

        messages = []
        async for message in channel.history(limit = None):
            if message.author == client.user:
                break
            messages.append(message)
        messages.reverse()

        for message in messages:
            with open(RESULTS_PATH, "a") as csvfile:
                csvfile.write(
                    message.created_at.date() + ", " + message.created_at.time() + ", " +
                    message.content + "\n"
                )

        log_message(__file__, "Read " + len(messages) + " messages")

        # Send Ping

        embed = discord.Embed(
            title = "Ping",
            description = str(datetime.datetime.now().time()).split(".")[0]
        )
        embed.set_footer(len(messages) + " read since last ping")
        await user.send(embed = embed)

        log_message(__file__, "User pinged")

bot_intents = discord.Intents.default()
bot_intents.message_content = True
client = discord.Client(intents = bot_intents)
main()
client.run(DISCORD_TOKEN)
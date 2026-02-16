# Copyright (C) 2026 Liam Ralph
# https://github.com/liam-ralph

# This program, including this file, is licensed under the
# MIT (Expat) License.
# See LICENSE or this project's source for more information.
# Project source: https://github.com/liam-ralph/discord-tracker-bot

# Discord Tracker Bot, a simple Discord bot that pings a
# user and trackers their responses.


# Imports

import discord
from bot_settings import *


# Main Function

def main():

    @client.event
    async def on_ready():
        print(client.user.name + " is online.")

bot_intents = discord.Intents.default()
bot_intents.message_content = True
client = discord.Client(intents = bot_intents)
main()
client.run(DISCORD_TOKEN)
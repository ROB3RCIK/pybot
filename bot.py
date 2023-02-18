import discord
import os
import asyncio
from discord import channel
from discord import member
from discord import guild
from discord.client import Client
from discord.ext import commands

intents = discord.Intents.all()
intents.members = True
intents.messages = True

client = commands.Bot(command_prefix="/", intents=intents)
client.remove_command("help")

@client.event
async def on_ready():
    print("[Bot Shiaanah] Online")

    #await client.change_presence(activity=discord.Streaming(name="Nic", url="https://www.twitch.tv/shiaanah/"))
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Shiaanah"))

async def load():
    for filename in os.listdir('./cogs/'):
        if filename.endswith(".py"):
            await client.load_extension(f"cogs.{filename[:-3]}")

async def main():
    async with client:
        await load()
        await client.start("")

asyncio.run(main())
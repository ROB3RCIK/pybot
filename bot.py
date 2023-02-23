import discord
import os
import asyncio
from dotenv import load_dotenv
from discord import channel
from discord import member
from discord import guild
from discord.client import Client
from discord.ext import commands

load_dotenv()

intents = discord.Intents.all()
intents.members = True
intents.messages = True

client = commands.Bot(command_prefix="/", intents=intents)
client.remove_command("help")

@client.event
async def on_ready():
    print("[Bot Shiianah] Online")

    #await client.change_presence(activity=discord.Streaming(name="Nic", url="https://www.twitch.tv/shiianah/"))
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Shiianah"))

async def load():
    for filename in os.listdir('./cogs/'):
        if filename.endswith(".py"):
            await client.load_extension(f"cogs.{filename[:-3]}")

async def main():
    async with client:
        await load()
        await client.start(os.getenv("client_token"))

asyncio.run(main())
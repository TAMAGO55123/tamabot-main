import discord
from dotenv import load_dotenv
from discord.ext import commands
from discord import Status, app_commands
import datetime
import requests
from os import getenv

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True

bot = commands.Bot(command_prefix="t!", intents=intents)

try:
    bot.run(getenv("BOT_TOKEN"))
except Exception as e:
    print(f"エラーが発生しました。: {e}")
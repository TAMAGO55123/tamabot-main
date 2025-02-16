import discord
from dotenv import load_dotenv
from discord.ext import commands, tasks
from discord import Status, app_commands
import datetime
import requests
import asyncio
load_dotenv()
from os import getenv, listdir

now_status=0

@tasks.loop(seconds=20)
async def status():
    global now_status

    if now_status == 0:
        data1 = discord.Activity(type=discord.ActivityType.playing, name="T-BOT | TAMAGO55123")
        now_status = 1
    elif now_status == 1:
        data1 = discord.Activity(type=discord.ActivityType.competing, name=f"{len(bot.guilds)}サーバー")
        now_status =0

    await bot.change_presence(activity=data1)

async def main(bot:commands.Bot):

    @bot.event
    async def on_ready():
        print(f'\033[32m| {bot.user}としてログインしました。\033[0m')
        status.start()
        try:
            synced = await bot.tree.sync()
            print(f'\033[32m| {len(synced)}個のコマンドを同期しました。\033[0m')
        except Exception as e:
            print(f"\033[30m| コマンドの同期でエラーが発生しました。\n{e}\033[0m")

    for cog in listdir("cogs"):
        if cog.endswith(".py"):
            await bot.load_extension(f"cogs.{cog[:-3]}")
    
    

    # Bot Start
    print('\033[38;2;255;165;0m \033[1m')
    print('--------------')
    print('| \033[4mT-BOT\033[0m \033[38;2;255;165;0m')
    print('| Made By TAMAGO55123')
    print(f"| ServerName : {getenv("SERVER_NAME")}")
    print('--------------')
    print('\033[0m')
    await bot.start(getenv("BOT_TOKEN"))

if __name__ == "__main__":
    intents = discord.Intents.default()
    intents.message_content = True
    intents.guilds = True

    bot = commands.Bot(command_prefix="t!", intents=intents)
    asyncio.run(main(bot))

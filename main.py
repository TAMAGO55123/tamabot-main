import discord
from dotenv import load_dotenv
from discord.ext import commands
from discord import Status, app_commands
import datetime
import requests
import asyncio
load_dotenv()
from os import getenv, listdir


async def main():

    intents = discord.Intents.default()
    intents.message_content = True
    intents.guilds = True


    bot = commands.Bot(command_prefix="t!", intents=intents)

    @bot.event
    async def on_ready():
        print(f'{bot.user}としてログインしました。')
        try:
            synced = await bot.tree.sync()
            print(f'{len(synced)}個のコマンドを同期しました。')
        except Exception as e:
            print(f"コマンドの同期でエラーが発生しました。\n{e}")



    @bot.tree.command(name="tenki_setup",description="天気Botのセットアップ")
    async def tenki_setup(interaction: discord.Interaction):
        discord_webhook = await interaction.channel.create_webhook(name="Weather Hook")
        webhook_url = f"{getenv('WEATHER_HOOK')}?kind=k&url={discord_webhook}&type=add"
        print(discord_webhook.url)
        response = requests.get(url=webhook_url)
        if response.status_code == 200:
            await interaction.response.send_message("設定しました。")
        else:
            await interaction.response.send_message("なんらかの影響で設定できませんでした。\n作成されたWebhookを手動で削除して下さい。")

    for cog in listdir("cogs"):
        if cog.endswith(".py"):
            await bot.load_extension(f"cogs.{cog[:-3]}")
    
    await bot.start(getenv("BOT_TOKEN"))

if __name__ == "__main__":
    asyncio.run(main())

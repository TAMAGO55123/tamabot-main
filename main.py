import discord
from dotenv import load_dotenv
from discord.ext import commands
from discord import Status, app_commands
import datetime
import requests
load_dotenv()
from os import getenv
from keep_alive import keep_alive




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

@bot.tree.command(name="smash", description="何かを投げます")
async def smash(interaction: discord.Interaction, smash:str):
    await interaction.response.send_message(f"(っ'-')╮=͟͟͞ {smash}")

@bot.tree.command(name="ggrks", description="ググレカス")
async def ggrks(interaction:discord.Interaction, ggrks:str = "", link_embed:bool = True):
    if link_embed:
        link = f"https://ggrks.lol/{ggrks}"
    else:
        link = f"<https://ggrks.lol/{ggrks}>"
    await interaction.response.send_message(link)

try:
    keep_alive()
    bot.run(getenv("BOT_TOKEN"))
except Exception as e:
    print(f"エラーが発生しました。: {e}")
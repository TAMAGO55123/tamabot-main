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
    
    


    @bot.tree.context_menu(name="草を生やしまくる")
    async def kusa_boubou(interaction:discord.Interaction, message:discord.Message):
        kusa = [
            "<a:1330484687801421824:1366689867765121146>",
            "<:1160510894363644004:1366689856880775262>",
            "<:1257190547135791195:1366689859447558155>",
            "<:1257190750727176215:1366689861096050698>",
            "<:1280204538057457694:1366689862782160978>",
            "<:1293055646928998410:1366689865277902848>",
            "<:1332940409592221796:1366689869308629055>",
            "<:1343072400954228746:1366689871015710770>",
            "<:1353378191036907692:1366689873074847794>",
            "<:1354676301344280686:1366689875427983370>",
            "<:1354836172483989625:1366689877051183195>",
            "<:1365525798529794079:1366689880330997780>",
            "🇼",
            "🌱"
        ]
        await interaction.response.defer(thinking=True)
        for i in kusa:
            if i not in message.reactions:
                await message.add_reaction(i)
        true_kusa=0
        for i in kusa:
            if i in message.reactions:
                true_kusa=true_kusa+1
        if true_kusa == len(true_kusa):
            await interaction.followup.send(content="もうすでに草は生えまくってるようですが")
        else:
            await interaction.followup.send(content="草を生やしました。")

    # Bot Start
    print('\033[38;2;255;165;0m \033[1m')
    print('--------------')
    print('| \033[4mT-BOT\033[0m \033[38;2;255;165;0m')
    print('| Made By TAMAGO55123')
    print(f"| ServerName : {getenv('SERVER_NAME')}")
    print('--------------')
    print('\033[0m')
    await bot.start(getenv("BOT_TOKEN"))

if __name__ == "__main__":
    intents = discord.Intents.default()
    intents.message_content = True
    intents.guilds = True

    bot = commands.Bot(command_prefix="t!", intents=intents)
    discord.utils.setup_logging()
    asyncio.run(main(bot))

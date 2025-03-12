import discord
from discord.ext import commands
from discord import app_commands
from func.ready import bot_ready_print
from datetime import datetime, timezone, timedelta

class InfoCog(commands.Cog):
    def __init__(self, bot:commands.Bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_ready(self):
        bot_ready_print("Info Cog")

    @app_commands.command(name="ping", description="Botが作動するかのテストコマンド")
    async def ping(self, interaction:discord.Interaction):
        raw_ping = self.bot.latency
        print(raw_ping)
        ping = round(raw_ping * 1000)
        embed = discord.Embed(
            title="Pong!🏓",
            description=f"Latency: `{ping}ms`",
            color=0x00ff00,
            timestamp=datetime.timestamp(datetime.now(timezone(timedelta(hours=9))))
        )
        await interaction.response.send_message(content="Hello!", embed=embed)

async def setup(bot):
    await bot.add_cog(InfoCog(bot))
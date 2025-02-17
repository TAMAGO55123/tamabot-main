import discord
from discord.ext import commands
from discord import app_commands
import sys
from func.ready import bot_ready_print


ADMIN_LIST=[
    1209261129835085876,
    1198921988769587211
]

def check_admin(id:int):
    return id in ADMIN_LIST

# commands.Cogを継承する
class AdminCog(commands.Cog):
    def __init__(self, bot:commands.Bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_ready(self):
        bot_ready_print("Admin-Cog")
    
    @app_commands.command(name="admin_bot_stop", description="Botを停止させます。(管理者のみ)")
    async def admin_bot_stop(self, interaction:discord.Interaction, ok:bool):
        if ok & check_admin(interaction.user.id):
            await self.bot.change_presence(activity=discord.Activity(type=discord.ActivityType.unknown))
            await interaction.response.send_message(embed=discord.Embed(title="Botが停止しました。",description="再開するにはサーバーで`sudo systemctl start tbot`をする必要があります。"), ephemeral=True)
            sys.exit()

async def setup(bot):
    await bot.add_cog(AdminCog(bot))
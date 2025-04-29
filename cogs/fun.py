import discord
from discord.ext import commands
from discord import app_commands
from func.ready import bot_ready_print

# commands.Cogを継承する
class FunCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_ready(self):
        bot_ready_print(self.__cog_name__)
	
    @app_commands.command(name="ggrks", description="ググレカス")
    async def ggrks(self, interaction:discord.Interaction, ggrks:str = "", link_embed:bool = True):
        if link_embed:
            link = f"https://ggrks.lol/{ggrks}"
        else:
            link = f"<https://ggrks.lol/{ggrks}>"
        await interaction.response.send_message(link)
    
    @app_commands.command(name="smash", description="何かを投げます")
    async def smash(self, interaction: discord.Interaction, smash:str):
        await interaction.response.send_message(f"(っ'-')╮=͟͟͞ {smash}")
    
    

async def setup(bot):
    await bot.add_cog(FunCog(bot))
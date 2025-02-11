import discord
from discord.ext import commands
from discord import app_commands

# commands.Cogを継承する
class FunCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_ready(self):
        print("Fun-Cog ready!")
	
    @app_commands.command(name="ggrks", description="ググレカス")
    async def ggrks(interaction:discord.Interaction, ggrks:str = "", link_embed:bool = True):
        if link_embed:
            link = f"https://ggrks.lol/{ggrks}"
        else:
            link = f"<https://ggrks.lol/{ggrks}>"
        await interaction.response.send_message(link)
    
    @app_commands.command(name="smash", description="何かを投げます")
    async def smash(interaction: discord.Interaction, smash:str):
        await interaction.response.send_message(f"(っ'-')╮=͟͟͞ {smash}")

async def setup(bot):
    await bot.add_cog(FunCog(bot))
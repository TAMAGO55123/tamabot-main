from dotenv import load_dotenv
load_dotenv()
from os import getenv
import discord
from discord import Client, Intents, Interaction
from discord.app_commands import (
    CommandTree,
    allowed_installs, guild_install, user_install,
    allowed_contexts, dm_only, guild_only, private_channel_only,
)
import asyncio
load_dotenv()

class MyClient(Client):
    def __init__(self):
        super().__init__(intents=Intents.default())
        self.tree = CommandTree(self)

    async def setup_hook(self) -> None:
        await self.tree.sync()

    async def on_ready(self):
        print(f'Logged on as {self.user}')

client = MyClient()

# 実装

@client.tree.command()
@guild_install
@user_install
@allowed_contexts(guilds=True,dms=True,private_channels=True)
async def kaso2(interaction: Interaction, num:int, data:str, num_on:bool, silent:bool, des:str = ""):
    print(f"{interaction.user.name}({interaction.user.global_name})({interaction.user.id})")
    data2=""
    
    for i in range(num):
        if num_on:
            data3 = i+1
        else:
            
            data3 = ''
        data2 += f"{data3}{data}\n"
    #if len(data2) > 2000:
    #    embed = discord.Embed(title='文字数突破',description=f"{len(data2)}文字")
    #    await interaction.response.send_message(embed=embed)
    #else:
    embed = discord.Embed(description=data2)
    await interaction.response.send_message(embed=embed,content=des,silent=silent)

TOKEN = getenv('DISCORD_BOT_TOKEN')
client.run(TOKEN)

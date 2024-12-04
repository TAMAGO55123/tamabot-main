from dotenv import load_dotenv
load_dotenv()
from os import getenv
from discord import Client, Intents, Interaction
from discord.app_commands import (
    CommandTree,
    allowed_installs, guild_install, user_install,
    allowed_contexts, dm_only, guild_only, private_channel_only,
)
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
async def kaso2(interaction: Interaction, num:int, data:str):
    data2=""
    for i in range(num):
        data2 += f"{i+1}{data}\n"
    await interaction.response.send_message(data2)

TOKEN = getenv('DISCORD_BOT_TOKEN')
client.run(TOKEN)

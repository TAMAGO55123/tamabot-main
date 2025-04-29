import discord
from discord.ext import commands
from discord import app_commands
import sys
from func.ready import bot_ready_print


ADMIN_LIST=[
    1209261129835085876,
    1198921988769587211,
    1225220580668739694,
    1233064266580496506
]

def check_admin(id:int):
    return id in ADMIN_LIST

async def no_adimn(interaction:discord.Interaction):
    await interaction.response.send_message(embed=discord.Embed(
        title="使用不可",
        description="このコマンドはBotの管理者のみ使用できます"
    ))


# commands.Cogを継承する
class AdminCog(commands.Cog):
    def __init__(self, bot:commands.Bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_ready(self):
        bot_ready_print(self.__cog_name__)
    
    @app_commands.command(name="admin_bot_stop", description="Botを停止させます。(管理者のみ)")
    async def admin_bot_stop(self, interaction:discord.Interaction, ok:bool):
        if ok & check_admin(interaction.user.id):
            await self.bot.change_presence(activity=discord.Activity(type=discord.ActivityType.unknown))
            await interaction.response.send_message(embed=discord.Embed(title="Botが停止しました。",description="再開するにはサーバーで`sudo systemctl start tbot`をする必要があります。"), ephemeral=True)
            sys.exit()
        else:
            await no_adimn(interaction)
    
    @app_commands.command(name="server_list",description="Botが参加しているサーバーの一覧を表示します。（管理者のみ）")
    async def server_list(self, interaction:discord.Interaction):
        if check_admin(interaction.user.id):
            lists = self.bot.guilds
            des = ""
            for i in lists:
                des = des + f"\n{i.name}({i.id})"
            embed = discord.Embed(
                title="入っているサーバー",
                description=des,
                color=0x00ff00
            )
            await interaction.response.send_message(embed=embed, ephemeral=True)
        else:
            await no_adimn(interaction)
    
    @app_commands.command(name="server_invite",description="Botが参加しているサーバーの招待を作成します。（管理者のみ)")
    async def server_invite(self, interaction:discord.Interaction, id:str):
        if check_admin(interaction.user.id):
            #await interaction.response.send_message(content="どのサーバーの招待リンクを作成しますか？",ephemeral=True)
            link = await self.bot.get_guild(int(id)).categories[0].channels[0].create_invite(reason='T-BOTの管理者によって作成されました。', max_uses=1)
            await interaction.response.send_message(content=link, ephemeral=True)
            
        else:
            await no_adimn(interaction)

class server_invite_drop(discord.ui.Select):
    def __init__(self, bot:commands.Bot, timeout: float | None = 180):
        super().__init__(timeout=timeout)

        self.server_name = []
        for i in bot.guilds:
            self.server_name.append(i.name)
        self.server_name_choice = []
        for i in self.server_name:
            self.server_name_choice.append(discord.SelectOption(label=i))
        self.server_id = []
        for i in bot.guilds:
            self.server_id.append(i.id)
        
        self.bot = bot

        super().__init__(min_values=1, max_values=1, options=self.server_name)
    async def callback(self, interaction:discord.Interaction):
        if self.values[0] in self.server_name:
            guild = self.bot.get_guild(self.server_id[self.server_name.index(self.values[0])])
            link = await guild.categories[0].channels[0].create_invite(reason='T-BOTの管理者によって作成されました。', max_uses=1)
            await interaction.response.send_message(content=link)

async def setup(bot):
    await bot.add_cog(AdminCog(bot))
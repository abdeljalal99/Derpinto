import discord
from discord.ext import commands
import os
from keep_alive import keep_alive
from Music import Music
from Reaction import Reaction
from VoiceState import VoiceState

intents = discord.Intents().all()
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

cogs = [Music, Reaction, VoiceState]
for cog in cogs:
    cog.setup(bot)

@bot.event
async def on_member_join(member):
	role = discord.utils.get(member.guild.roles, name='Chorongito')
	await member.add_roles(role)

@bot.event
async def on_ready():
    print('ok')


keep_alive()
bot.run(f'{os.environ["token"]}')
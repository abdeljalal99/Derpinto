import discord
from discord.ext import commands
from discord.channel import DMChannel

class VoiceState(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after):
        if before.channel == None:
            msj = f'{member} entro a "{after.channel}"'
            await DMChannel.send(await self.bot.fetch_user(220203269262278656), msj)
        else:
            if after.channel == None:
                msj = f'{member} salio de "{before.channel}"'
                await DMChannel.send(await self.bot.fetch_user(220203269262278656), msj)
	
    def setup(bot):
    	bot.add_cog(VoiceState(bot))
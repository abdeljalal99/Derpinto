import discord
from discord.ext import commands

class Reaction(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, raw):
        if raw.message_id == 840363461745705021:
            if raw.emoji.id == 840365532825649213:
                role = self.bot.guilds[0].get_role(778393272367185960)
            elif raw.emoji.name == '🔥':
                role = self.bot.guilds[0].get_role(840331582664605736)
            elif raw.emoji.name == '🍀':
                role = self.bot.guilds[0].get_role(840365932961726475)
        
        message = await self.bot.guilds[0].get_channel(raw.channel_id).fetch_message(raw.message_id)
        for r in message.reactions:
                if raw.member in await r.users().flatten() and not raw.member.bot and str(r) != str(raw.emoji):
                    await message.remove_reaction(r.emoji, raw.member)
        try:
          	await raw.member.add_roles(role)
        except:
          	pass
          
    @commands.Cog.listener()
    async def on_raw_reaction_remove(self, raw):
        if raw.message_id == 840363461745705021:
            if raw.emoji.id == 840365532825649213:
                role = self.bot.guilds[0].get_role(778393272367185960)
            elif raw.emoji.name == '🔥':
                role = self.bot.guilds[0].get_role(840331582664605736)
            elif raw.emoji.name == '🍀':
                role = self.bot.guilds[0].get_role(840365932961726475)
        
        user = self.bot.guilds[0].get_member(raw.user_id)
        try:
          	await user.remove_roles(role)
        except:
        	pass

    def setup(bot):
    	bot.add_cog(Reaction(bot))
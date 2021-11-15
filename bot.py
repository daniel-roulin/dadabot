from discord.ext import commands
from discord.ext.commands import CommandNotFound

from dadadance.bot import Music
from dadanswers.bot import PhysicAnswers

bot = commands.Bot('dada ', description='The one and only dadabot')
bot.add_cog(Music(bot))
bot.add_cog(PhysicAnswers(bot))

@bot.event
async def on_ready():
    print('Logged in as:\n{0.user.name}'.format(bot))

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, CommandNotFound):
        await ctx.send('Error: {}'.format(str(error)))
        await ctx.send("To get a list of avaible commands, type `dada help`")



token = 'NzY0OTU1ODk5MzQ4Mzg1ODE1.X4Nysg.On025R8mZmcvvl23rtbzYjfziGQ'
bot.run(token)
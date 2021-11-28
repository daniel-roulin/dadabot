from discord.ext import commands
from discord.ext.commands import CommandNotFound

from dadadance.bot import Music
from dadanswers.bot import PhysicAnswers

bot = commands.Bot('dada ', description='The one and only dadabot')
bot.add_cog(Music(bot))
bot.add_cog(PhysicAnswers(bot))

@bot.command()
async def echo(ctx, *, arg):
    """Repeats your message"""
    await ctx.send(arg)

@bot.event
async def on_ready():
    print('Logged in as:\n{0.user.name}'.format(bot))

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, CommandNotFound):
        await ctx.send('Error: {}'.format(str(error)))
        await ctx.send("To get a list of avaible commands, type `dada help`")

with open("token.txt") as f:
    token = f.read()

bot.run(token)
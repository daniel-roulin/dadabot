from discord.ext import commands
from discord.ext.commands import CommandNotFound
import logging

from dadadance.dance import Music
from dadanswers.answer import PhysicAnswers

bot = commands.Bot(("dada ", "ddb ", "dd ", "d ", "da"), description='The one and only dadabot')
bot.add_cog(Music(bot))
bot.add_cog(PhysicAnswers(bot))

@bot.command()
async def echo(ctx, *, arg):
    """Repeats your message"""
    await ctx.send(arg)

@bot.event
async def on_ready():
    logging.info(f"Logged in as: '{bot.user.name}'")

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, CommandNotFound):
        logging.info(f"User '{ctx.author.name}' used an invalid command")
        await ctx.send('Error: {}'.format(str(error)))
        await ctx.send("To get a list of avaible commands, type `dada help`")

@bot.event
async def on_command(ctx):
    logging.info(f"User '{ctx.author.name}' sent message '{ctx.message.content}' in channel '{ctx.channel.name}' of server '{ctx.guild.name}'")


logging.basicConfig(level=logging.INFO, filename="logs.log", format="%(asctime)s %(levelname)-4s %(message)s", datefmt="%m/%d/%Y %H:%M:%S")
logging.info("Starting...")

with open("token.txt") as f:
    token = f.read()

bot.run(token)
from discord.ext import commands
from discord.ext.commands import CommandNotFound
import logging
import discord

from dadadance.dance import Music
from dadanswers.answer import PhysicAnswers

bot = commands.Bot(("dada ", "ddb ", "dd ", "d "), description='The one and only dadabot')
bot.add_cog(Music(bot))
bot.add_cog(PhysicAnswers(bot))

@bot.command()
async def echo(ctx, *, message):
    """Repeats your message
    
    Args:
        message (string): Message to repeat
    """
    await ctx.send(message)

@bot.command()
async def invite(ctx, permission:int = 8):
    """Invites this bot to another server

    Args:
        permission (integer): Custom permission integer, see https://discordapi.com/permissions.html
    """

    url = f"https://discord.com/oauth2/authorize?client_id=764955899348385815&scope=bot&permissions={permission}"
    embed = discord.Embed(title="Thank you for choosing dadabot", color=0xFF7700, description=f"To add dadabot to a server:\n[[Click here!]]({url})")
    embed.set_footer(text="Made with 🧡 by Daniel Roulin")
    await ctx.send(embed=embed)

@bot.event
async def on_ready():
    logging.info(f"Logged in as: '{bot.user.name}'")

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, CommandNotFound):
        logging.info(f"User '{ctx.author.name}' used an invalid command")
        await ctx.send('Error: {}'.format(str(error)))
        await ctx.send("To get a list of available commands, type `dada help`")

@bot.event
async def on_command(ctx):
    logging.info(f"User '{ctx.author.name}' sent message '{ctx.message.content}' in channel '{ctx.channel.name}' of server '{ctx.guild.name}'")


logging.basicConfig(level=logging.INFO, filename="logs.log", format="%(asctime)s %(levelname)-4s %(message)s", datefmt="%m/%d/%Y %H:%M:%S")
logging.info("Starting...")

with open("token.txt") as f:
    token = f.read()

bot.run(token)
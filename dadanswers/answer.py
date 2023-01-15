import logging
from discord.ext import commands
import discord
from dadanswers import generator
from io import BytesIO

class PhysicAnswers(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def cog_command_error(self, ctx, error):
        await ctx.send('Error: {}'.format(str(error)))

    @commands.command(name='answer', aliases=["a"])
    async def answer(self, ctx, chapter:int, exercise:int):
        """
        Get physics answers.

        <chapter>   must be the number of the chapter you want.
        <exercise>  must be the number of the chapter you want.

        Example:
        dada answer 11 68
        This command will send the answer of exercise 62 in chapter 11 (Rotation)
        """
        async with ctx.typing():
            try:
                with BytesIO() as image_binary:
                    image = generator.create_image(chapter, exercise)
                    image.save(image_binary, 'PNG')
                    image_binary.seek(0)
                    await ctx.send(
                        f"Answers for exercise {exercise} chapter {chapter}",
                        file = discord.File(fp = image_binary, filename = f"Exercise {exercise} Chapter {chapter}.png"))

                logging.info(f"Sent answer for chapter {chapter}, exercise {exercise} to user '{ctx.author.name}'")

                embed_ad = discord.Embed(
                    title="Did you know?", 
                    color=0xFF7700, 
                    description=f"Dadabot now has a website!\nCheck it out on [dadarou.com](https://dadarou.com)",
                    url="https://dadarou.com",
                )
                embed_ad.set_thumbnail(url="http://dadarou.com/favicon.png")
                embed_ad.set_footer(text="Made with 🧡 by Daniel Roulin")
                await ctx.send(embed=embed_ad)                    
        
            except generator.InvalidChapter:
                logging.info(f"User '{ctx.author.name}' tried to access chapter {chapter}, which does not exists")
                await ctx.send(f'Error: Chapter {chapter} does not exist')
            
            except generator.InvalidExercise:
                await ctx.send(f'Error: Exercise {exercise} does not exist')
                logging.info(f"User '{ctx.author.name}' tried to access exercise {exercise}, which does not exists")
            
            except Exception as e:
                await ctx.send(f'Internal Error: Contact Dada_Roulin#5870 for help')
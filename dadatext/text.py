from discord.ext import commands

class PhysicAnswers(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def cog_command_error(self, ctx, error):
        await ctx.send('Error: {}'.format(str(error)))

    @commands.command(name='answer', aliases=["a"])
    async def answer(self, ctx, mode:int, exercise:int):
        """
        Get physics answers.

        <chapter>   must be the number of the chapter you want.
        <exercise>  must be the number of the chapter you want.

        Example:
        dada answer 11 68
        This command will send the answer of exercise 62 in chapter 11 (Rotation)
        """
        async with ctx.typing():
            pass
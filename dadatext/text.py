from discord.ext import commands

class CoolText(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def cog_command_error(self, ctx, error):
        await ctx.send('Error: {}'.format(str(error)))

    @commands.command(name='text')
    async def cooltext(self, ctx, style, *, text):
        """
        Generates cool text.

        <style> Style of the text.
        <text>  Your text to be coolified.
        """

        async with ctx.typing():
            await ctx.send(f"Style: {style}, Text; {text}")
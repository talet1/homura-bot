from discord.ext import commands
from pybooru import Danbooru
from dotenv import load_dotenv
import os
import random

load_dotenv()

client = Danbooru('danbooru', username='USERNAME', api_key='API_KEY')

class CommandsCog(commands.Cog, name = "Commands"):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name = 'showpic', aliases=['show'])
    async def showpic(self, ctx, *, search: str):
        print(f"Executing showpic command with search term: {search}")  # Log message
        posts = client.post_list(tags=search, limit=100)
        if posts:
            random_post = random.choice(posts)
            await ctx.send(random_post['file_url'])
        else:
            await ctx.send("No images found.")

    @commands.command(name='repeat', aliases=['copy', 'mimic'])
    async def do_repeat(self, ctx, *, our_input: str):
        """A simple command which repeats our input.
        In rewrite Context is automatically passed to our commands as the first argument after self."""

        await ctx.send(our_input)
    
    @commands.command(name='add', aliases=['plus'])
    @commands.guild_only()
    async def do_addition(self, ctx, first: int, second: int):
        """A simple command which does addition on two integer values."""

        total = first + second
        await ctx.send(f'The sum of **{first}** and **{second}**  is  **{total}**')

    @commands.command(name='me')
    @commands.is_owner()
    async def only_me(self, ctx):
        """A simple command which only responds to the owner of the bot."""

        await ctx.send(f'Hello {ctx.author.mention}. This command can only be used by you!!')

    @commands.Cog.listener()
    async def on_member_ban(self, guild, user):
        """Event Listener which is called when a user is banned from the guild.
        For this example I will keep things simple and just print some info.
        Notice how because we are in a cog class we do not need to use @bot.event
        For more information:
        http://discordpy.readthedocs.io/en/rewrite/api.html#discord.on_member_ban
        Check above for a list of events.
        """

        print(f'{user.name}-{user.id} was banned from {guild.name}-{guild.id}')

        
async def setup(bot):
    await bot.add_cog(CommandsCog(bot))
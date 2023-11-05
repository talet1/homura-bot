from discord.ext import commands
from pybooru import Danbooru
import random
import os

client = Danbooru('danbooru', username=os.getenv('USERNAME'), api_key=os.getenv('API_KEY'))

class MadokaCog(commands.Cog, name = 'Puella Magi Madoka Magica'):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name = 'madokaPic', aliases = ['madoka'])
    async def showpic(self, ctx):
        print(f"Executing madokaPic command...")
        posts = client.post_list(tags = 'Kaname_Madoka rating:s', limit = 100)
        if posts:
            random_post = random.choice(posts)
            print(random_post['file_url'])
            await ctx.send(random_post['large_file_url'])
        else:
            await ctx.send("No images found.")

async def setup(bot):
    await bot.add_cog(MadokaCog(bot))
    

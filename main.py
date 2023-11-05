from discord.ext import commands
from discord import Intents
import os
intents = Intents.all()

def get_prefix(bot, message):
    """A callable Prefix for our bot. This could be edited to allow per server prefixes."""

    # Notice how you can use spaces in prefixes. Try to keep them simple though.
    prefixes = ['>', '.', '!']

    # Check to see if we are outside of a guild. e.g DM's etc.
    if not message.guild:
        # Only allow ? to be used in DMs
        return '?'

    # If we are in a guild, we allow for the user to mention us or use any of the prefixes in our list.
    return commands.when_mentioned_or(*prefixes)(bot, message)


initial_extensions = ['cogs.commands', 'cogs.pmmm']

bot = commands.Bot(command_prefix = get_prefix, intents=intents)


@bot.event
async def on_ready():
    # Send a message when the bot is online to channel with id 1169498988861464639
    channel = bot.get_channel(1169498988861464639)
    await channel.send("I'm online!")
    # Print some info to the console
    print("----------------------")
    print("Logged In As")
    print("Username: %s"%bot.user.name)
    print("ID: %s"%bot.user.id)
    print("----------------------")

    # Here we load our extensions(cogs) listed above in [initial_extensions].
    for extension in initial_extensions:
        await bot.load_extension(extension)
        print(f"Loaded {extension}")

bot.run(os.getenv('DISCORD_BOT_TOKEN'))  # Replace with your actual Discord bot token


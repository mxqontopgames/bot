import discord
from discord.ext import commands
import os

# Set up bot intents (important for message content)
intents = discord.Intents.default()
intents.message_content = True

# Set up command prefix and bot
bot = commands.Bot(command_prefix='!', intents=intents)

# Called when the bot is ready
@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user}")

# Simple "hello" command
@bot.command()
async def hello(ctx):
    await ctx.send(f"Hello, {ctx.author.name}!")

# Ping command
@bot.command()
async def ping(ctx):
    await ctx.send("Pong!")

# Run the bot
# You can either use an environment variable:
bot.run()

# OR (for testing only), paste the token directly — but DO NOT share it:
# bot.run("YOUR_BOT_TOKEN_HERE")

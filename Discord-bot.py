import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name}")
    print("------")

@bot.command()
async def hello(ctx):
    await ctx.send("Hello!")

@bot.command()
async def echo(ctx, *, message):
    await ctx.send(message)

@bot.command()
async def square(ctx, num: int):
    square_value = num ** 2
    await ctx.send(f"The square of {num} is {square_value}")

bot.run("YOUR_BOT_TOKEN")

import discord
import random, os
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def medio_ambiente(ctx):
    await ctx.send("Para ayudar al medio ambiente puedes: reciclar, hacer compost o utilizar enrgias renobales")
@bot.command()
async def reciclar(ctx):
    await ctx.send("hay varias formas de reciclar di !r para saber mas")
@bot.command()
async def compost(ctx):
    await ctx.send("hacer compost o composta el simple"
    " ***primero tienes que separar lo organico luego tienes que ponerle tierra y de preferencia lonbrices luego hojas y listo"
    " ya tienes tu tierra fertil")
@bot.command()
async def energias_renobables(ctx):
    await ctx.send("hay muchas energias renobales pero las principales son la solar,la eolica y la hidraulica")
@bot.command()
async def r(ctx):
    rrr = random.choice((os.listdir('como_separar')))
    with open(f'como_separar/{rrr}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)
bot.run("")

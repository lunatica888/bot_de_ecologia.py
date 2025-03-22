import discord
import random, os
from discord.ext import commands
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')
prome = 0
@bot.command()
async def medio_ambiente(ctx):
    await ctx.send("Para ayudar al medio ambiente puedes: reciclar, hacer compost, cuidar el agua o utilizar enrgias renobales")
    await ctx.send("a y tambien reforestar ayuda")
@bot.command()
async def reciclar(ctx):
    await ctx.send("hay varias formas de reciclar di !r para saber mas")
@bot.command()
async def compost(ctx):
    await ctx.send("hacer compost o composta es simple"
    " ***primero tienes que separar lo organico porque es el principal ingrediente luego tienes que ponerle tierra y de preferencia lonbrices luego hojas y listo"
    " ya tienes tu tierra fertil")
@bot.command()
async def dato_cutioso(ctx):
    await ctx.send("para que no se acabe nustro mundo la ONU se pusieron de acuerdo para formar la ODS un plan de sostentabilidad a 15 años.Este acuerdo fue firmado en 2015 "
    "y niguno de sus acuerdos se ha concretado aun")


@bot.command()
async def cuidar_agua(ctx):
    await ctx.send("para cuidar el agua evita dejar abierta le llave en cuelquier momento que no la enstas utilizando, tambien sierra la llve de de la ducha entre cada tallada entre muchas cosas mas")
@bot.command()
async def energias_renobables(ctx):
    await ctx.send("hay muchas energias renobales pero las principales son la solar,la eolica y la hidraulica")
@bot.command()
async def r(ctx):
    rrr = random.choice((os.listdir('como_separar')))
    with open(f'como_separar/{rrr}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)
@bot.command()
async def solar(ctx):
    await ctx.send("la energia solar se obtiene del sol con paneles o con los rayos directos como con hornos solares")
@bot.command()
async def hidraulica(ctx):
    await ctx.send("la energia hidraulica es una fuente de energía renovable que se obtiene al transformar la energía del agua en movimiento en electricidad.")
@bot.command()
async def eolica(ctx):
    await ctx.send("la energia eolica se obtine por la fuerza que aplica el viento a una turbina")
quiz = 0
@bot.command()
async def meme(ctx):
    ez = random.choice((os.listdir('memes_')))
    with open(f'memes_/{ez}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)
@bot.command()
async def quizz(ctx):
    await ctx.send("primera pregunta: tu cuales dirias que son las 2 principales formas de reciclar")
    await ctx.send("a_1: papel y plasticos")
    await ctx.send("b_1: varios y vidrios")
    await ctx.send("c_1: oganico e inorganicos")
    await ctx.send("!a_1,!b_1 o !c_1?")
    await ctx.send("(despues de responder pon !quizz2)")
@bot.command()
async def c_1(ctx):
    global quiz
    quiz += 2

@bot.command()
async def quizz2(ctx):
    e = random.choice((os.listdir('memes_de_quizz')))
    with open(f'memes_de_quizz/{e}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)
    await ctx.send("segunda pregunta: tu cual dirias que es el principal ingrediente de la composta?")
    await ctx.send("a_2: lombrises")
    await ctx.send("b_2: tierra")
    await ctx.send("c_2: reciduos oganicos")
    await ctx.send("d_2: hojas")
    await ctx.send("!a_2,!b_2,!c_2 o !d_2?")
    await ctx.send("(despues de responder pon !quizz3)")
@bot.command()
async def c_2(ctx):
    global quiz
    quiz += 2
@bot.command()
async def quizz3(ctx):
    await ctx.send("tercera pregunta: cuales son las 3 energias renobables principales ?")
    await ctx.send("a_3: hidraulica, solar y eolica")
    await ctx.send("b_3: fosil, electrica y termica")
    await ctx.send("c_3: gravitacional, cinetica y electromagnética")
    await ctx.send("!a_3,!b_3 o !c_3?")
    await ctx.send("(despues de responder pon !quizz4)")
@bot.command()
async def a_3(ctx):
    global quiz
    quiz += 2
@bot.command()
async def quizz4(ctx):
    e = random.choice((os.listdir('memes_de_quizz')))
    with open(f'memes_de_quizz/{e}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)
    await ctx.send("cuarta pregunta: como pudes cuda el agua?")
    await ctx.send("a_4: dejando la llave abierta y poniendo una cubeta abajo de la ducha")
    await ctx.send("b_4: serrando la llave del agua y ducharme sin preocuparme por el agua")
    await ctx.send("c_4: serrando la llave y o poner uma cubeta debajo de la ducha o serrala en tre cada tallada")
    await ctx.send("!a_4,!b_4 o !c_4?")
    await ctx.send("(despues de responder pon !quizz5)")
@bot.command()
async def c_4(ctx):
    global quiz
    quiz += 2
@bot.command()
async def quizz5(ctx):
    await ctx.send("quinta pregunta: quien formo la ODS?")
    await ctx.send("a_5: WWF")
    await ctx.send("b_5: ONU")
    await ctx.send("c_5: Bimbo")
    await ctx.send("!a_5,!b_5 o !c_5?")
    await ctx.send("ya terminaste ahora di !resultado para saver tu calificacion")
@bot.command()
async def b_5(ctx):
    global quiz
    quiz += 2

@bot.command()
async def resultado(ctx):
    global quiz
    await ctx.send("Calificacion:")
    await ctx.send(quiz)
    if quiz <5 and quiz >=0:
        a = random.choice((os.listdir('reprobado')))
        with open(f'reprobado/{a}', 'rb') as f:
            picture = discord.File(f)
        await ctx.send(file=picture)
    elif quiz <=8 and quiz >=6:
        ab = random.choice((os.listdir('apenas')))
        with open(f'apenas/{ab}', 'rb') as f:
            picture = discord.File(f)
        await ctx.send(file=picture)
    else:
        az = random.choice((os.listdir('sabelotodo')))
        with open(f'sabelotodo/{az}', 'rb') as f:
            picture = discord.File(f)
        await ctx.send(file=picture)
    quiz = 0

bot.run("")

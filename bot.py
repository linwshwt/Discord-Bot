import discord
import random
import os
from discord.ext import commands

from bot_logic import gen_pass
from bot_logic import flip_coin

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='$', intents=intents)


@bot.event
async def on_ready():
    print(f'Hemos iniciado sesión como {bot.user}')


@bot.command()
async def Holaa(ctx):
    await ctx.send("Holaa como estas ?")


@bot.command()
async def bye(ctx):
    await ctx.send("\U0001f642")


@bot.command()
async def coin(ctx):
    await ctx.send(flip_coin())


@bot.command()
async def password(ctx):
    await ctx.send("Tu contraseña " + gen_pass(10))


@bot.command()
async def joined(ctx, member: discord.Member):
    await ctx.send(
        f'{member.name} joined {discord.utils.format_dt(member.joined_at)}'
    )


@bot.command()
async def meme(ctx):
    images = os.listdir('images')

    img_name = random.choice(images)

    with open(f'images/{img_name}', 'rb') as f:
        picture = discord.File(f)

    await ctx.send(file=picture)
    
@bot.command()
async def animales(ctx):
    memes = os.listdir('images/animales')

    img_name = random.choice(memes)

    with open(f'images/animales/{img_name}', 'rb') as f:
        picture = discord.File(f)

    await ctx.send(file=picture)

@bot.command()
async def ayuda(ctx):
    await ctx.send(
        "$Holaa - Saluda\n"
        "$bye - Se despide\n"
        "$coin - Lanza una moneda\n"
        "$password - Genera una contraseña\n"
        "$joined @usuario - Muestra cuándo entró una persona\n"
        "$meme - Envía un meme aleatorio\n"
        "$ayuda - Muestra los comandos"
        "$animales - Envía un meme de animales\n"
    )
    
bot.run("PON_TU_TOKEN_AQUI")

import discord

from bot_logic import gen_pass
from bot_logic import flip_coin

# La variable intents almacena los privilegios del bot
intents = discord.Intents.default()

# Activar el privilegio de lectura de mensajes
intents.message_content = True

# Necesario para trabajar con miembros del servidor
intents.members = True

# Crear un cliente y transferirle los privilegios
client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f'Hemos iniciado sesión como {client.user}')


@client.event
async def on_message(message):

    if message.author == client.user:
        return

    if message.content.startswith('$Holaa'):
        await message.channel.send("Holaa como estas ?")

    elif message.content.startswith('$bye'):
        await message.channel.send("\U0001f642")

    elif message.content.startswith('$coin'):
        await message.channel.send(flip_coin())

    elif message.content.startswith('$password'):
        await message.channel.send("Tu contraseña " + gen_pass(10))

    elif message.content.startswith('$joined'):
        if message.mentions:
            member = message.mentions[0]

            await message.channel.send(
                f'{member.name} joined {discord.utils.format_dt(member.joined_at)}'
            )
        else:
            await message.channel.send(
                "Debes mencionar a una persona. Ejemplo: $joined @usuario"
            )

    
client.run("PON_TU_TOKEN_AQUI")

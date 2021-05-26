from keep_alive import *
from func import *
import discord
import os

client = discord.Client()


@client.event
async def on_ready():
  print('Connecté en tant que {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('$'):
    price = get_crypto_price(message.content[1:])
    await message.channel.send(price)

keep_alive()
client.run(os.getenv('TOKEN'))

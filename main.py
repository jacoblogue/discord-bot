import discord
import os
from discord import Spotify

TOKEN = 'OTg1NjI5MTM2MDQ1MzU1MDk5.GrGPco.ebiS2iVegSJ8cNWWLhCR8LmZ5hHYxHNhgQ_LsU'

client = discord.Client()

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('$hello'):
    await message.channel.send('Cheesedog!')
    await message.channel.send('😊')
    await message.add_reaction('😊')
    print('did it')
client.run(TOKEN)
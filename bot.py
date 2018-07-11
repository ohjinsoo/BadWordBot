from config import BOT_TOKEN

import discord
import asyncio
import websockets

from commands import BannedWords


client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as: %s [%s]' % (client.user.name, client.user.id))

@client.event
async def on_message(message):
    if message.content == '.cmds' or message.content == '.help':
        commands = '``` List of Commands: [] - required'
        commands += '\n    .add [word]  THIS IS AN ADMIN ONLY COMMAND'
        commands += '\n    .del [word]  THIS IS AN ADMIN ONLY COMMAND'
        commands += '\n    .words'
        commands += '\n    .warnings```'
        await client.send_message(message.channel, commands)

    elif message.content.startswith('.add '):
        await BannedWords.add(client, message)

    elif message.content.startswith('.del '):
        await BannedWords.delete(client, message)

    elif message.content == '.warnings':
        await BannedWords.showWarnings(client, message)

    elif message.content == '.words':
        await BannedWords.showWords(client, message)
    else:
        await BannedWords.containsBanned(client, message)

client.run(BOT_TOKEN)

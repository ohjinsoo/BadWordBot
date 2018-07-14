import asyncio
import discord

users = {}
bannedWords = {}

async def add(client, message):
  admin = await isAdmin(client, message)
  if not admin:
    return

  word = message.content[5:]
  if bannedWords.get(word) == None:
    bannedWords[word] = True;
    await client.send_message(message.channel, "The word is now a banned word.")
  elif bannedWords.get(word):
    await client.send_message(message.channel, "The word is already banned.")

async def delete(client, message):
  admin = await isAdmin(client, message)
  if not admin:
    return

  word = message.content[5:]
  if bannedWords.get(word) == None:
    await client.send_message(message.channel, "The word was not a banned word.")
  elif bannedWords[word]:
    del bannedWords[word]
    await client.send_message(message.channel, "The word is now allowed.")

async def showWarnings(client, message):
  if users == {}:
    await client.send_message(message.channel, "There are no users with any warnings.")
  else:
    i = 1
    words = '``` List of Warned Users:'
    for k, v in users.items():
      words += '\n    ' + k + ' has ' + str(v) + ' warning(s).'

      if i == len(users):
        words += '```'

      i += 1

    await client.send_message(message.channel, words)

async def showWords(client, message):
  if bannedWords == {}:
    await client.send_message(message.channel, "There are no banned words.")
  else:
    i = 1
    words = '``` List of Banned Words:'
    for k, v in bannedWords.items():
      words += '\n    ' + str(i) + '. ' + k

      if i == len(bannedWords):
        words += '```'

      i += 1

    await client.send_message(message.channel, words)

async def containsBanned(client, message):
  for k, v in bannedWords.items():
    if k in message.content:
      user = str(message.author)

      if users.get(user) == None:
        users[user] = 1
      else:
        users[user] = users[user] + 1

      await client.delete_message(message)
      await client.send_message(message.channel, "That is a banned word, " + str(user) + "! You have " + str(users[user]) + " warning(s).")

async def isAdmin(client, message):
  return message.channel.permissions_for(message.author).administrator


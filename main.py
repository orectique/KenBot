import discord
from collections import Counter
import pandas
import os

client = discord.Client()

@client.event
async def on_ready():
    print('Bot is ready')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$boss'):
        await message.channel.send('Hello!')

    if message.content.startswith('$UserAnalyze'):
        data = []
        async for mesg in message.channel.history(limit = 1000):
            data.append(mesg.author)
        
        count = pandas.DataFrame(dict(Counter(data)), columns=['Author', 'count'])
        count['rank'] = list([i for i in range(1, len(count) + 1)])
        if len(count) == 0:
            await message.channel.send('Nobody here')
        
        else:
            txt = ''
            for i in range(len(count)):
                txt += str(count.Author[i]) + ' - ' + str(count.rank[i]) + ', '

            await message.channel.send(txt)
       

client.run(os.getenv('TOKEN'))

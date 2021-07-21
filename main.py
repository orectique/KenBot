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
            if mesg.author != client.user:
                data.append(mesg.author)
        
       
        count = dict(Counter(data))
        count = {'Author' : list(count.keys()), 'Count' : list(count.values())}
        count = pandas.DataFrame.from_dict(count)

        if len(count) == 0:
            await message.channel.send('Nobody here')

        else: 
            txt = ''
            count = count.sort_values(by = 'Count', ascending = False).reset_index(inplace = False)
            count['Rank'] = list(i +1 for i in range(len(count)))
            for i in range(len(count)):
                txt += str(count.Author[i]) + ' - ' + str(count.Rank[i]) + ', '
                        
            await message.channel.send(txt)

TOKEN = os.getenv("TOKEN")
client.run(TOKEN)

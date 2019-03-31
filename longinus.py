import discord
import random
import settings


class LonginusBot(discord.Client):
    async def on_message(self, message):
        print("%s: %s" % (message.author, message.content))
        if message.author == self.user:
            return

        if 'sum sanctus' in message.content.lower():
            quote = random.choice([line.rstrip('\n') for line in open('sumsanctus.txt')])
            await message.channel.send('%s __**SUM SANCTUS!**__\r||```%s```||' % (message.author.mention, quote))


client = LonginusBot()
client.run(settings.DISCORD_TOKEN)

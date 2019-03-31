# Longinus Bot

Quick explanation of what the bot does and how it works so you can make changes yourself maybe?

line 7: Print the mesage author and content to terminal eg: `Floppy#3405: test message`

line 8-9: you never reply to your own bot, feedback loops would occur

line 11: IF the characters "sum sanctus" is IN message.content.lower() (the message all to lower case)

line 12: open the file sumsanctus.txt and pick a random line

line 13: send a message to the channel the message came from


## INSTALL

Put your bot token where it says TOKENHERE (line 17)

**__Do NOT use python 3.7, use python 3.6__**

`py -3 pip install -U https://github.com/Rapptz/discord.py/archive/rewrite.zip`

`python3 longinus.py`

done

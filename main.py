import discord
from config import TOKEN
from sports import golf,mlb,nhl,nba,soccerEU,soccerINT
client = discord.Client()

@client.event
async def on_ready():
    print("Bot is Ready!")
    await client.change_presence(status=discord.Status.idle,activity=discord.Game("Creating the bot"))


@client.event
async def on_message(message):
    if message.author == client.user:
        #make sure bot doesnt respond to itself
        return
    if message.content =="Hello":
        await message.channel.send("World")
    if message.content == "!MLB":
        await mlb.mlb_event(message)
    if message.content=="!GOLF":
        await golf.golf_event(message,message.author)
    if message.content == "!NBA":
        await nba.nba_event(message)
    if message.content== "!SOCCER_EU":
        await soccerEU.soccer_event(message)
    if message.content == "!SOCCER_INT":
        await soccerINT.soccer_event(message)
    if message.content =="!NHL":
        await nhl.nhl_event(message)
    
client.run(TOKEN)
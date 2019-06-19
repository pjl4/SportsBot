import discord
from config import MLB
import datetime
import http.client
import requests
import json
from pytz import timezone

tz=timezone('US/Michigan')


def api_request(league,apiKey,date):
    res=requests.get("https://api.sportradar.us/"+league+"/trial/v6.5/en/games/"+date+"/boxscore.json?api_key="+apiKey)
    data= json.loads(res.text)
    gamesDict=data['league']['games']
    gamesMessage=""
    inning="0"

    for game in gamesDict:
        if game['game']['status'] == "scheduled":
            gmtTime= datetime.datetime.strptime(game['game']['scheduled'],"%Y-%m-%dT%H:%M:%S%z")
            estTime = gmtTime.astimezone(tz)
        if game['game']['status'] == "closed":
           inning =str(game['game']['final']['inning'])
        if game['game']['status'] == "inprogress":
            inning =str(game['game']['outcome']['current_inning'])
        gamesMessage=gamesMessage+game['game']['away']['name']+" "+str(game['game']['away']['runs'])+" at "+ game['game']['home']['name']+ " "+str(game['game']['home']['runs'])+"\nStart Time: "+estTime.strftime("%H:%M:%S")+" EST \nInning: "+inning+"\n--------------------------------------------\n"
        

    return gamesMessage

def mlb_event(message):
    currentDT = datetime.datetime.now()
    formatted= currentDT.strftime("%Y/%m/%d")
    games=api_request("mlb",MLB,formatted)

    return message.channel.send(games)



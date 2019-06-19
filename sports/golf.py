import discord
from config import GOLF
import datetime
import http.client
import requests
import json
from pytz import timezone

tz=timezone('US/Michigan')


def api_request(apiKey,date):
    res=requests.get("https://api.sportradar.us/golf-t2/schedule/pga/"+date+"/tournaments/schedule.json?api_key="+apiKey)
    data= json.loads(res.text)
    tournaments=data['tournaments']
    tourneyMessage="Upcoming Tournaments\n\n"
    for tourney in tournaments:
        if datetime.datetime.strptime(tourney['start_date'],'%Y-%m-%d') > datetime.datetime.today():
            tourneyMessage=tourneyMessage+"Name: "+tourney['name']+ "   Start Date: "+tourney['start_date']+"\nCourse: "+tourney['venue']['name']+"\n----------------------------------------------\n"
    return tourneyMessage





def golf_event(message,author):
    currentDT = datetime.datetime.now()
    formatted= currentDT.strftime("%Y")
    golf=api_request(GOLF,formatted)
    if len(golf) > 2000:
        return message.channel.send("Message too long Implement workaround soon")
    return message.channel.send(golf)
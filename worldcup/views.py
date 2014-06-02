from flask import render_template, url_for, redirect
from worldcup import app
import unirest


def getWorldCupInfo():
    response = unirest.get("https://wmerydith-espn.p.mashape.com/sports/basketball/nba?apikey=%3Capikey%3E&_accept=application%2Fjson",
        headers={
            "X-Mashape-Authorization": "3gd92ZCjls37bbHhAZ1JmZXsDbYLOjiu"
        },
        params={
            "apikey": "gdkr4pnmhes2nf963mj5wxyd"
        }
    )
    return response

def getTeams():
    response = unirest.get("http://api.espn.com/v1/sports/soccer/fifa.world/teams",
        params = {'apikey': 'gdkr4pnmhes2nf963mj5wxyd'}
    )
    return response

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/teams/')
def teams():
    json = getTeams()
    return render_template('teams.html', json=json.body['sports'][0]['leagues'][0]['teams'])

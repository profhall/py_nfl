'''

API key explanation
crntdrv = current drive

'''


import requests
import json
import os
from xmljson import badgerfish as bf
from xml.etree.ElementTree import fromstring
from game import Game


Games=[]

def get_live_game_stats(**kwargs):
   # print("From def get_live_game_stats: ", kwargs)
    #http://www.nfl.com/liveupdate/game-center/2017012200/2017012200_gtd.json

    game_id = kwargs['game_id']
    game_stats = requests.get("http://www.nfl.com/liveupdate/game-center/{}/{}_gtd.json".format(game_id,game_id))

    if(game_stats.status_code is 200 ):
        Home={}
        Away={}

        game_count = kwargs['game_count']
        #print(game_stats.content)
        game_stats = game_stats.json()
        
        allgame = game_stats[str(game_id)]
        
        drives = allgame['drives']
        score_summary = allgame['scrsummary']
        quarter = allgame['qtr']

        #print(allgame.keys())
        #print(allgame['clock'])
        #print(drives.keys(), '\n', json.dumps(drives))

        home_team = allgame['home']
        home_team_stats = home_team['stats']
        home_team_abbr= home_team['abbr']
        home_score = home_team['score']


        away_team = allgame['away']
        away_team_stats = away_team['stats']
        away_team_abbr = away_team['abbr']
        away_score = away_team['score']



        '''-----Home Team Stats----'''
        Home[str(game_count)] = {}
        this_game = Home[str(game_count)]
        for key, item in home_team_stats.items():
            #print(key,"\n",item)
            #print(this_game[key])
            this_game[key] = []
            for k,i in item.items():
                this_game[key].append(i)
                #print (k, i)
            #print(json.dumps(this_game,indent=3))

        home_team_stats = Home[str(game_count)]

        '''-----Away Team Stats----'''
        Away[str(game_count)] = {}
        this_game = Away[str(game_count)]
        for key, item in away_team_stats.items():
            # print(key,"\n",item)
            # print(this_game[key])
            this_game[key] = []
            for k, i in item.items():
                this_game[key].append(i)
                # print (k, i)
            # print(json.dumps(this_game,indent=3))

        away_team_stats = Away[str(game_count)]

        #print("Game(game_id={}, home={} away={}, hscore={}, ascore={}, qtr={}, time={})".format(game_id, home_team_abbr,away_team_abbr,home_team['score'],away_team['score'],allgame['qtr'],allgame['clock']))

        curr_game = Game(game_id=game_id, home=home_team_abbr, away=away_team_abbr, hscore=home_team['score'],
                         ascore=away_team['score'], qtr=allgame['qtr'], time=allgame['clock'], scoring_summary=score_summary, game_drives=drives)
        Games.append(curr_game)

        '''Current Quarter'''
        #print('Current quarter...')
        #print(quarter)
        #print(json.dumps(qtr,indent=3))

        '''Score Summary Data'''
        #print('keys in score summary dictionary...')
        #print(score_summary.keys())
        #print(json.dumps(score_summary,indent=3))

        '''All Drives Summary Data'''
        #print('keys in drives dictionary...')
        #print(drives.keys())
        #print(json.dumps(drives,indent=3))



    else:
        print("----Game not started yet----")



def games_by_year_and_week(**kwargs):
    #print(kwargs)

    #check for week, season type and year
    #print(kwargs["week"],kwargs["season_type"],kwargs["season_year"])

    season_year = kwargs["season_year"]
    season_type = kwargs["season_type"]
    week = kwargs["week"]
    game_week_year_xml = requests.get("http://www.nfl.com/ajax/scorestrip?season={}&seasonType={}&week={}".format(season_year, season_type, week))

    #print("http://www.nfl.com/ajax/scorestrip?season={}&seasonType={}&week={}".format(season_year, season_type, week))

    #print((bf.data(fromstring(game_week_year_xml.content)).json()))
    game_year_week = bf.data(fromstring(game_week_year_xml.content))
   # print(json.dumps(game_year_week["ss"]["gms"],indent=4))
    this_weeks_games = game_year_week["ss"]["gms"]["g"]

    for i,game in enumerate(this_weeks_games):
        game_id = game['@eid']
        game_day= game['@d']
        game_time = game['@t']
        home_team = game['@v']
        away_team = game['@h']
        game_stats=get_live_game_stats(game_id=game_id, game_count=i)

        if (game['@vs'] is not None):
            away_score = game['@vs']
            home_score = game['@hs']

            #return {"vteam":away_team, "hteam":home_team, "vscore":away_score, "hscore":home_score, "gameday": game_day, "game_id": game_id, "gametime":game_time}
        else:
            print(away_team, home_team,game_id,game_day,game_time)
            #return {"vteam":away_team, "hteam":home_team, "gameday": game_day, "game_id": game_id, "gametime":game_time}

        #print(Games[len(Games) - 1].away,' @ ',Games[len(Games) - 1].home)


    return Games

#games_by_year_and_week(week=2,season_type='REG',season_year=2018)

def getCurrentWeekGameData():
    try:
        response = requests.get('http://www.nfl.com/liveupdate/scores/scores.json')
        games = response.json()
        gamecenter_url_ids = list(games.keys())
        #print("Live Games: Gamecenter URL IDs: ", gamecenter_url_ids)
        for index in range(len(gamecenter_url_ids)):
            game_stats_url = 'http://www.nfl.com/liveupdate/game-center/{}/{}_gtd.json'.format(gamecenter_url_ids[index],gamecenter_url_ids[index])
            response = requests.get(game_stats_url)
            game_id = gamecenter_url_ids[index]
            print("Gamecenter URL : ", game_stats_url)
            if (response):
                game_stats = response.json()
                #print("Stats: ", json.dumps(game_stats[game_id],indent=2))
                #print(game_stats[game_id].keys())
            else:
                print("No Stats Yet")

    except:
        print("Error with Token")
        return("Error with Token\n")

#getCurrentWeekGameData()

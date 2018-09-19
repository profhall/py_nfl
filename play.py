from getGames import *
import time
#getCurrentWeekGameData()

def main():

    print("Welcome to nfl game retriever!!!")
    year = input(" What year you want to choose game from?")
    week = input("Which week?")
    type = 'REG'

    game_list = games_by_year_and_week(week=week,season_type=type,season_year=year)

    for game in game_list:
        print(game.home,' @ ',game.away)
        print(game.home_score['T'] , ' : ', game.away_score['T'])
        game.scoring_summary(team="both")
        print("-----",game.home, "Scoring Summary----")
        print(json.dumps(game.home_score_sum,indent=3))
        print("----",game.away," Scoring Summary----")
        print(json.dumps(game.away_score_sum,indent=3))




if __name__ == '__main__':
    main()

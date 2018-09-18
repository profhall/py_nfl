#from generateToken import games_by_year_and_week

'''Sample Model

Game(game_id=2018091700,home='CHI', away='SEA',hscore={'1': 7, '2': 3, '3': 0, '4': 14, '5': 0, 'T': 24},ascore={'1': 0, '2': 3, '3': 0, '4': 14, '5': 0, 'T': 17},qtr='Final',time='00:00')
'''

class Game:

    def __init__(self, **kwargs):
        self.home=kwargs['home']
        self.home_score = kwargs['hscore']
        self.away=kwargs['away']
        self.away_score = kwargs['ascore']
        self.time = kwargs['time']
        self.qtr = kwargs['qtr']
        self.id = kwargs['game_id']

    def scoring_summary(self, **kwargs):
        #dict.get(key, default = None)
        print(kwargs)
        team = kwargs.get('team', None)

        if(team is not None):
            print(team)
        else:
            print('no team provided to scoring_summary() Game method. \nPlease choose away, home or both for keyword "team"')

    def quarter_summary(self, **kwargs):
        print(kwargs)

    def drives(self, **kwargs):
        print(kwargs)


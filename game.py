#from generateToken import games_by_year_and_week

class Game:

    def __init__(self, **kwargs):
        self.home=kwargs['home']
        self.home_score = kwargs['hscore']
        self.away=kwargs['away']
        self.away_score = kwargs['ascore']
        self.time = kwargs['time']
        self.qtr = kwargs['qtr']
        self.id = kwargs['game_id']



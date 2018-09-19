'''Sample Model

Game(game_id=2018091700,home='CHI', away='SEA',hscore={'1': 7, '2': 3, '3': 0, '4': 14, '5': 0, 'T': 24},ascore={'1': 0, '2': 3, '3': 0, '4': 14, '5': 0, 'T': 17},qtr='Final',time='00:00')
'''

class Game:

    def __init__(self, **kwargs):

        '''Home'''
        self.home=kwargs['home']
        self.home_score = kwargs['hscore']
        self.home_score_sum=[]


        '''Away'''
        self.away=kwargs['away']
        self.away_score = kwargs['ascore']
        self.away_score_sum=[]


        '''Game info'''
        self.time = kwargs['time']
        self.qtr = kwargs['qtr']
        self.id = kwargs['game_id']
        self.scoring_sum = kwargs['scoring_summary']



    def scoring_summary(self, **kwargs):

        #print(kwargs)
        team = kwargs.get('team', None)

        if(team is not None):
            #print(team)
            #print(self.scoring_sum)
            for key, score in self.scoring_sum.items():
                #print(key)

                if score['team'] == self.home:
                    self.home_score_sum.append(score)

                elif score['team'] == self.away:
                    self.away_score_sum.append(score)
        else:
            print('no team provided to scoring_summary() Game method. \nPlease choose away, home or both for keyword "team"')

    def quarter_summary(self, **kwargs):
        print(kwargs)


    def drives(self, **kwargs):
        print(kwargs)


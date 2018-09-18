from DjangoNfl.getGames import *

class TestGames(object):
    Games = games_by_year_and_week(week=1,season_type='REG',season_year=2018)

    def test_get_all_games(self):

        assert len(Games) > 0
        assert Games[5].home is not None
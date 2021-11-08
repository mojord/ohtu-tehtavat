import unittest
from statistics import Statistics
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri", "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]
# 16, 99, 90, 98, 124
class TestStatistics(unittest.TestCase):
    def setUp(self):
        # annetaan Statistics-luokan oliolle "stub"-luokan olio
        self.statistics = Statistics(
            PlayerReaderStub()
        )


    def test_search_works(self):
        tested = str(self.statistics.search("Semenko").name)
        self.assertEqual(tested, "Semenko")
    def test_search_works_iffutile(self):
        tested = str(self.statistics.search("Ronaldo"))
        self.assertEqual(tested, "None")
    
    def test_team_works(self):
        list = []
        team = self.statistics.team("EDM")
        for player in team:
            list.append(str(player))
        self.assertEqual(list,['Semenko EDM 4 + 12 = 16','Kurri EDM 37 + 53 = 90','Gretzky EDM 35 + 89 = 124'])

    def test_top_scorers_work(self):
        toplist = []
        scorers = self.statistics.top_scorers(3)
        for player in scorers:
            toplist.append(str(player))
        print(scorers)
        self.assertEqual(toplist,['Gretzky EDM 35 + 89 = 124','Lemieux PIT 45 + 54 = 99', 'Yzerman DET 42 + 56 = 98'])
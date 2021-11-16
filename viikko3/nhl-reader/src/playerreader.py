import requests
from player import Player


class PlayerReader:
    def __init__(self, url):
        self.url = url

    def get_players(self):
        response = requests.get(self.url).json()
        players = []

        for player_dict in response:
            name = player_dict["name"]
            nationality = player_dict["nationality"]
            assists = player_dict["assists"]
            goals = player_dict["goals"]
            penalties = player_dict["penalties"]
            team = player_dict["team"]
            games = player_dict["games"]

            player = Player(name, nationality, assists, goals, penalties, team, games)

            if player.nationality == "FIN":
                players.append(player)

#            if len(parts) > 3:
#                player = Player(
#                    parts[0].strip(),
#                    parts[1].strip(),
#                    int(parts[3].strip()),
#                    int(parts[4].strip())
#                )
#        for player in players:
#            print(player)


        return players

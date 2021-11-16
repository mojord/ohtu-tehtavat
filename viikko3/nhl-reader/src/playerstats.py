from playerreader import PlayerReader

def sort_by_points(player):
    return player.points

class Statistics:
    def __init__(self, reader):
        self.reader = reader
        self._players = reader.get_players()

    def top_scorers_by_nationality(self, nationality):
        finns = []
        for player in self._players:
            if player.nationality == nationality:
                finns.append(player)

        sorted_finns = sorted(
            finns,
            reverse=True,
            key=sort_by_points
        )

        return sorted_finns
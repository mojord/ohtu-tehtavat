from statistics import Statistics
from player_reader import PlayerReader
from matchers import And, HasAtLeast, PlaysIn, HasFewerThan, Not, All, Or

def main():
    url = "https://nhlstatisticsforohtu.herokuapp.com/players.txt"
    reader = PlayerReader(url)
    stats = Statistics(reader)

#    matcher = And(
#        HasAtLeast(5, "goals"),
#        HasAtLeast(5, "assists"),
#        PlaysIn("PHI")
#    )

#    matcher = And(
#        HasFewerThan(1, "goals"),
#        PlaysIn("NYR")
#    )

#    for player in stats.matches(matcher):
#        print(player)
    
#    print("")
    
#    matcher = And(
#    Not(HasAtLeast(1, "goals")),
#    PlaysIn("NYR")
#    )

#    for player in stats.matches(matcher):
#        print(player)

#    print("")

#    matcher = Or(
#    HasAtLeast(30, "goals"),
#    HasAtLeast(50, "assists")
#    )
#    matcher = And(
3    HasAtLeast(40, "points"),
#    Or(
#        PlaysIn("NYR"),
#        PlaysIn("NYI"),
#        PlaysIn("BOS")
#    )
#)





    for player in stats.matches(matcher):
        print(player)



if __name__ == "__main__":
    main()

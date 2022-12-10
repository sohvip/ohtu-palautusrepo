from statistics import Statistics
from player_reader import PlayerReader
from matchers import And, HasAtLeast, PlaysIn, Not, HasFewerThan, All, Or
from query import QueryBuilder

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2021-22/players.txt"
    reader = PlayerReader(url)
    stats = Statistics(reader)
    query = QueryBuilder()
    matcher = (
        query
            .Or(
            query.playsIn("PHI")
                .hasAtLeast(10, "assists")
                .hasFewerThan(5, "goals")
                .build(),
            query.playsIn("EDM")
                .hasAtLeast(50, "points")
                .build()
            )
            .build()
        )
    for player in stats.matches(matcher):
        print(player)
    
    # filtered_with_all = stats.matches(All())
    # print(len(filtered_with_all))


if __name__ == "__main__":
    main()

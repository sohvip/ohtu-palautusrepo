from player_reader import PlayerReader
from player_stats import PlayerStats
from datetime import datetime
def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2021-22/players"
    reader = PlayerReader(url)
    stats = PlayerStats(reader.get_players())
    players = stats.top_scorers_by_nationality("FIN")

    date = datetime.now()
    print(f'Players from FIN {date}')

    for player in players:
        print(player)

if __name__ == "__main__":
    main()

from player import Player

class PlayerStats:
    def __init__(self, reader):
        self.reader = reader

    def top_scorers_by_nationality(self, nationality):
        players = []

        for player_dict in self.reader:
            if player_dict['nationality'] == nationality:
                player = Player(
                    player_dict['name'],
                    player_dict['team'],
                    player_dict['goals'],
                    player_dict['assists']
                )
                players.append((player, player.points))

        players.sort(key=lambda a: a[1], reverse=True)

        for i in range(len(players)):
            players[i] = players[i][0]

        return players
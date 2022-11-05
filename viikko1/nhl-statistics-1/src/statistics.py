from player_reader import PlayerReader

def sort_by_points(player):
    return player.points

def sort_by_goals(player):
    return player.goals

def sort_by_assists(player):
    return player.assists


class Statistics:
    def __init__(self, player_reader):
        reader = player_reader

        self._players = reader.get_players()

    def search(self, name):
        for player in self._players:
            if name in player.name:
                return player

        return None

    def team(self, team_name):
        players_of_team = filter(
            lambda player: player.team == team_name,
            self._players
        )

        return list(players_of_team)

    def top(self, how_many, sort_by=1):
        if sort_by == 1:
            sorted_players = sorted(
                self._players,
                reverse=True,
                key=sort_by_points
            )

        elif sort_by == 2:
            sorted_players = sorted(
                self._players,
                reverse=True,
                key=sort_by_goals
            )

        elif sort_by == 3:
            sorted_players = sorted(
                self._players,
                reverse=True,
                key=sort_by_assists
            )
        
        else:
            return None

        result = []
        i = 0
        while i <= how_many:
            result.append(sorted_players[i])
            i += 1

        return result

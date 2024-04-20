from player_reader import PlayerReader
from statistics_service import StatisticsService

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2022-23/players.txt"
    reader = PlayerReader(url)
    stats = StatisticsService(reader)

    
    searched_player = stats.search("Player Name")
    print(searched_player)

    team_players = stats.team("Team Name")
    print(team_players)

    top_players = stats.top(10)
    for player in top_players:
        print(player)

if __name__ == "__main__":
    main()
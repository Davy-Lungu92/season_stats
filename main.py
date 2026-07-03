import argparse
from load_data import Data
from compare_stats import organizer
from display import create_table


# def main():
#     print("Hello from season-stats!")


# if __name__ == "__main__":
#     main()

chelsea = Data(league="ENG Premier League",season="2025-2026",statistic="Shots On Target",team="Chelsea")

chelsea.data_loader()
chelsea.get_league_data()
chelsea.get_team_data()
chelsea.get_available_teams()

league_stats = chelsea.league_data
home_stats = chelsea.home_data
away_stats = chelsea.away_data

print(home_stats)
print()
print(away_stats)
print(league_stats)
print()

# data = organizer(away_data=away_stats,home_data=home_stats,league_data=league_stats,team="Chelsea")
# print()
# print()
# create_table(data=data,place="Home",season="2025-2026",stat="Shots On Target",team="Chelsea")

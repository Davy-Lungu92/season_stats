import argparse
from load_data import Data
from compare_stats import organizer
from display import create_table

parser = argparse.ArgumentParser()
parser.add_argument("team_name", help="Enter the name of the team you wish to obtain results for",type=str)

parser.add_argument("stat", help="Enter the stat you wish to see [Goals FT, Goals HT, Shots, Shots On Target, Fouls, Corners, Yellow Cards, Red Cards ]",type=str)

parser.add_argument("league", help="""Enter the League you wish to access ['BEL First Division A','DEU Bundesliga 1','DEU Bundesliga 2','ENG Premier League','ENG Championship','ENG League 1','ENG League 2','ENG Conference','ESP La Liga','ESP La Liga Segunda','FRA Ligue 1','FRA Ligue 2','GRC Super League','ITA Serie A','ITA Serie B','NLD Eredivisie','PRT Liga 1','SCO Premier League','SCO Division 1','SCO Division 2','SCO Division 3','TUR Super Lig']""",type=str)

parser.add_argument("season", help="Enter the season you wish to access, in the format 2025-2026",type=str)



args = parser.parse_args()

def main():
    try:
        team = args.team_name
        stat = args.stat 
        league = args.league
        season = args.season

        
        my_data = Data(league=league,season=season,statistic=stat,team=team)
        if not isinstance(league,str) or not isinstance(season,str):
            raise Exception("League and Season must be strings")
        else: 
            my_data.data_loader()
            my_data.get_available_teams()
        my_teams = my_data.available_teams
        if team not in my_teams:
            raise Exception(f"{team} is not in available teams or has been spelt incorrectly, available teams: {my_teams}")
        else:
            my_data.get_league_data()
            my_data.get_team_data()
        

        league_stats = my_data.league_data
        home_stats = my_data.home_data
        away_stats = my_data.away_data


        data = organizer(away_data=away_stats,home_data=home_stats,league_data=league_stats,team=team)

        create_table(data=data,place="Home",season=season,stat=stat,team=team)
        create_table(data=data,place="Away",season=season,stat=stat,team=team)
    except Exception as e:
        print(e)
if __name__ == "__main__":
    main()

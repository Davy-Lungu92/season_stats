import penaltyblog as pb #type: ignore
import pandas as pd #type: ignore
from functools import lru_cache
import warnings
from pandas.errors import PerformanceWarning #type: ignore

warnings.filterwarnings("ignore", category=PerformanceWarning)




mapper: dict[str,list[str]] = {
    "Goals FT": ["fthg","ftag"],
    "Goals HT": ["hthg","athg"],
    "Shots": ["hst","ast"],
    "Shots On Target": ["hst","ast"], 
    "Fouls": ["hf","af"],
    "Corners": ["hc", "ac"],
    "Yellow Cards": ["hy", "ay"],
    "Red Cards" : ["hr", "ar"],
}


class Data:
    """Class to handle data from penalty blog"""
    def __init__(self, team:str, league:str, season:str, statistic:str):
        self.team = team
        self.league = league
        self.season = season
        self.statistic = statistic
        self.data = pd.DataFrame()
        self.available_teams = []
    
    
    @staticmethod
    @lru_cache(maxsize=20)
    def get_data(leg,sea):
        """ caching enabled Method to obtain league data from a specified season, 
        
        args:
            leg: the actual league user wishes to obtain league data for.
            sea: the actual season the user wishes to obtain league data    
        
        returns:
            A pandas data frame containing all the league data for a particular season .

        """
        return pb.scrapers.FootballData(leg, sea).get_fixtures()
    
    def data_loader(self):
        """ loads specfic data by using the get_data method

        args:
            self.league
            self.season
        """
        df = self.get_data(self.league, self.season)    
        new_df = df[['team_home','team_away','fthg','ftag','ftr','hthg','htag','htr','hs','as','hst','ast','hf','af','hc','ac','hy','ay','hr','ar',]].copy()
        self.data = pd.concat([self.data, new_df], ignore_index=True)

    def get_league_data(self) -> dict:
        """ Method to obtain league wide summary for the selected statistic
        Returns a dict of the statistic
        """
        
        league_dict = {}
        
        # obtain league descriptive stats
        summary = self.data.describe()

        # obtain avearge values for home and away
        league_dict["Home Average"] = round(summary.loc["mean",mapper[self.statistic][0]].item(),2) # type: ignore
        league_dict["Away Average"] = round(summary.loc["mean",mapper[self.statistic][1]].item(),2) # type: ignore

        # Obtain minimum values for home and away
        league_dict["Home Minimum"] = round(summary.loc["min",mapper[self.statistic][0]].item() ,2)# type: ignore
        league_dict["Away Minimum"] = round(summary.loc["min",mapper[self.statistic][1]].item() ,2)# type: ignore

        # Obtain maximum values for home and away
        league_dict["Home Maximum"] = round(summary.loc["max",mapper[self.statistic][0]].item() ,2)# type: ignore
        league_dict["Away Maximum"] = round(summary.loc["max",mapper[self.statistic][1]].item() ,2)# type: ignore

        return league_dict

    def get_team_data(self):
        pass

    def get_available_teams(self):
        """ Method to obtain all the available teams in a particular league and season"""
        home_teams = list(self.data["team_home"])
        away_teams = list(self.data["team_away"])

        # all_teams = set(home_teams.extend(away_teams))
        # len(all_teams)
        all_teams = list(set(home_teams + away_teams))
        self.available_teams.extend(all_teams)


arsenal = Data("Arsenal","ENG Premier League","2021-2022","Shots On Target")

arsenal.data_loader()
arsenal.get_available_teams()
print(arsenal.available_teams)
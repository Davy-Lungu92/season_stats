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
        self.league_data = {}
        self.home_data = {}
        self.away_data = {}
        self.positive = ["Goals FT", "Goals HT","Shots","Shots On Target", "Corners"]
        self.negative = ["Fouls","Yellow Cards", "Red Cards"]
    
    @staticmethod
    @lru_cache(maxsize=20)
    def __get_data(leg,sea):
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
        df = self.__get_data(self.league, self.season)    
        new_df = df[['team_home','team_away','fthg','ftag','ftr','hthg','htag','htr','hs','as','hst','ast','hf','af','hc','ac','hy','ay','hr','ar',]].copy()
        self.data = pd.concat([self.data, new_df], ignore_index=True)

    @staticmethod
    def __get_stats(home_label:str, away_label:str, summary:pd.DataFrame| pd.Series,statistic) -> dict[str,float|int]:
        """ Method to obtain league wide summary for the selected statistic
        Returns a dict of the statistic
        """
        league_dict = {}

        # obtain avearge values for home and away
        league_dict[f"{home_label} Home Average"] = round(summary.loc["mean",mapper[statistic][0]].item(),2) # type: ignore
        league_dict[f"{away_label} Away Average"] = round(summary.loc["mean",mapper[statistic][1]].item(),2) # type: ignore

        # Obtain minimum values for home and away
        league_dict[f"{home_label} Home Minimum"] = round(summary.loc["min",mapper[statistic][0]].item() ,2)# type: ignore
        league_dict[f"{away_label} Away Minimum"] = round(summary.loc["min",mapper[statistic][1]].item() ,2)# type: ignore

        # Obtain maximum values for home and away
        league_dict[f"{home_label} Home Maximum"] = round(summary.loc["max",mapper[statistic][0]].item() ,2)# type: ignore
        league_dict[f"{away_label} Away Maximum"] = round(summary.loc["max",mapper[statistic][1]].item() ,2)# type: ignore

        # Obtain std values for home and away
        league_dict[f"{home_label} Home std"] = round(summary.loc["std",mapper[statistic][0]].item() ,2)# type: ignore
        league_dict[f"{away_label} Away std"] = round(summary.loc["std",mapper[statistic][1]].item() ,2)# type: ignore

        # Obtain 25 percentile values for home and away
        league_dict[f"{home_label} Home 25%"] = round(summary.loc["25%",mapper[statistic][0]].item() ,2)# type: ignore
        league_dict[f"{away_label} Away 25%"] = round(summary.loc["25%",mapper[statistic][1]].item() ,2)# type: ignore

        # Obtain 50 percentile values for home and away
        league_dict[f"{home_label} Home 50%"] = round(summary.loc["50%",mapper[statistic][0]].item() ,2)# type: ignore
        league_dict[f"{away_label} Away 50%"] = round(summary.loc["50%",mapper[statistic][1]].item() ,2)# type: ignore
        
        # Obtain 75 percentile values for home and away
        league_dict[f"{home_label} Home 75%"] = round(summary.loc["75%",mapper[statistic][0]].item() ,2)# type: ignore
        league_dict[f"{away_label} Away 75%"] = round(summary.loc["75%",mapper[statistic][1]].item() ,2)# type: ignore


        return league_dict
        

    def get_league_data(self):
        """ Method to obtain league wide summary for the selected statistic
        Returns a dict of the statistic
        """
        
        # obtain league descriptive stats
        summary = self.data.describe()

        league_data = self.__get_stats("League","League",summary,self.statistic)
        self.league_data = league_data

    def get_team_data(self):
        """ Method to obtain team specific summary for the selected statistic"""
        home_table = self.data.loc[self.data["team_home"] == self.team]
        away_table = self.data.loc[self.data["team_away"] == self.team]
        
        home_summary = home_table.describe()
        away_summary = away_table.describe()

        self.home_data = self.__get_stats(self.team, "Opponent", home_summary, self.statistic) 
        self.away_data = self.__get_stats("Opponent",self.team,away_summary, self.statistic) 


    def get_available_teams(self):
        """ Method to obtain all the available teams in a particular league and season"""
        home_teams = list(self.data["team_home"])
        away_teams = list(self.data["team_away"])

        # all_teams = set(home_teams.extend(away_teams))
        # len(all_teams)
        all_teams = list(set(home_teams + away_teams))
        self.available_teams.extend(all_teams)

   
            


    
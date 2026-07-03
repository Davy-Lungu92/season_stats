from rich.console import Console
from rich.table import Table
from compare_stats import organizer


def create_table(team:str,stat:str,season:str, data, place:str):
    console = Console()
    if place == "Home":
        title = f"{team} {stat} at {place} for the {season} Season"
        instruction = f"""Note: Compare the Mean for {team} to the Percentile's for All teams League at Home to see which Percentile it falls under, same for the Mean of the opponents to the percentiles for All teams League Away\n"""
        team_mean, league_home_mean, opponents_faced_mean, away_teams_mean = data["Average"][f"{team} Home Average"], data["Average"]["All Teams Home Average"], data["Average"]["Opponents Away Average"], data["Average"]["All Teams Away Average"]   

        team_max, league_home_max, opponents_faced_max, away_teams_max = data["Maximum"][f"{team} Home Maximum"], data["Maximum"]["All Teams Home Maximum"], data["Maximum"]["Opponents Away Maximum"], data["Maximum"]["All Teams Away Maximum"] 

        team_min, league_home_min, opponents_faced_min, away_teams_min = data["Minimum"][f"{team} Home Minimum"], data["Minimum"]["All Teams Home Minimum"], data["Minimum"]["Opponents Away Minimum"], data["Minimum"]["All Teams Away Minimum"]

        team_std, league_home_std, opponents_faced_std, away_teams_std = data["std"][f"{team} Home std"], data["std"]["All Teams Home std"], data["std"]["Opponents Away std"], data["std"]["All Teams Away std"]

        team_25, league_home_25, opponents_faced_25, away_teams_25 = data["25%"][f"{team} Home 25%"], data["25%"]["All Teams Home 25%"], data["25%"]["Opponents Away 25%"], data["25%"]["All Teams Away 25%"]

        team_50, league_home_50, opponents_faced_50, away_teams_50 = data["50%"][f"{team} Home 50%"], data["50%"]["All Teams Home 50%"], data["50%"]["Opponents Away 50%"], data["50%"]["All Teams Away 50%"]

        team_75, league_home_75, opponents_faced_75, away_teams_75 = data["75%"][f"{team} Home 75%"], data["75%"]["All Teams Home 75%"], data["75%"]["Opponents Away 75%"], data["75%"]["All Teams Away 75%"]

    elif place == "Away":
        title = f"{team} {stat} {place} for the {season} Season"
        instruction = f"""Note: Compare the Mean for {team} to the Percentile's for All teams League Away to see which Percentile it falls under, same for the Mean of the opponents to the percentiles for All teams League Home\n"""
        team_mean, league_home_mean, opponents_faced_mean, away_teams_mean = data["Average"][f"{team} Away Average"], data["Average"]["All Teams Home Average"], data["Average"]["Opponents Home Average"], data["Average"]["All Teams Away Average"]

        team_max, league_home_max, opponents_faced_max, away_teams_max = data["Maximum"][f"{team} Away Maximum"], data["Maximum"]["All Teams Home Maximum"], data["Maximum"]["Opponents Home Maximum"], data["Maximum"]["All Teams Away Maximum"] 

        team_min, league_home_min, opponents_faced_min, away_teams_min = data["Minimum"][f"{team} Away Minimum"], data["Minimum"]["All Teams Home Minimum"], data["Minimum"]["Opponents Home Minimum"], data["Minimum"]["All Teams Away Minimum"]

        team_std, league_home_std, opponents_faced_std, away_teams_std = data["std"][f"{team} Away std"], data["std"]["All Teams Home std"], data["std"]["Opponents Home std"], data["std"]["All Teams Away std"]

        team_25, league_home_25, opponents_faced_25, away_teams_25 = data["25%"][f"{team} Away 25%"], data["25%"]["All Teams Home 25%"], data["25%"]["Opponents Home 25%"], data["25%"]["All Teams Away 25%"]

        team_50, league_home_50, opponents_faced_50, away_teams_50 = data["50%"][f"{team} Away 50%"], data["50%"]["All Teams Home 50%"], data["50%"]["Opponents Home 50%"], data["50%"]["All Teams Away 50%"]

        team_75, league_home_75, opponents_faced_75, away_teams_75 = data["75%"][f"{team} Away 75%"], data["75%"]["All Teams Home 75%"], data["75%"]["Opponents Home 75%"], data["75%"]["All Teams Away 75%"]

    else:
        raise Exception("Wrong key entered, expected Home or Away")
    
    table = Table(title=title)

    # Define the columns
    table.add_column("Description", justify="left", style="cyan", no_wrap=True)
    table.add_column(team, style="magenta", no_wrap=False)
    table.add_column("Opponents Faced", justify="center", style="green",no_wrap=False)
    table.add_column("All teams League Home", style="blue", no_wrap=False)
    table.add_column("All teams League Away", style="blue", no_wrap=False)

        

    # Add the rows of data
    table.add_row("Mean", str(team_mean),str(opponents_faced_mean) ,str(league_home_mean),  str(away_teams_mean))
    table.add_row("MAX", str(team_max),str(opponents_faced_max), str(league_home_max),  str(away_teams_max))
    table.add_row("MIN", str(team_min), str(opponents_faced_min) ,str(league_home_min), str(away_teams_min))
    table.add_row("STD", str(team_std), str(opponents_faced_std) ,str(league_home_std), str(away_teams_std))
    table.add_row("25% Percentile", str(team_25),str(opponents_faced_25), str(league_home_25),  str(away_teams_25))
    table.add_row("50% Percentile", str(team_50),str(opponents_faced_50) ,str(league_home_50) , str(away_teams_50))
    table.add_row("75% Percentile", str(team_75),str(opponents_faced_75) ,str(league_home_75) , str(away_teams_75))

    # Print the table to the terminal
    print("\n")
    print(f"{instruction}")
    console.print(table)


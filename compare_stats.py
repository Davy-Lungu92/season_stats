def organizer(team, home_data,away_data, league_data):
    organized = {}
    average_dict = {}
    min_dict = {}
    max_dict = {}
    std_dict = {}
    percen_25_dict = {}
    percen_50_dict = {}
    percen_75_dict = {}
    
    # fill up average dict
    average_dict["All Teams Home Average"] = league_data["League Home Average"]    
    average_dict["All Teams Away Average"] = league_data["League Away Average"]
    
    average_dict["Opponents Away Average"] = home_data["Opponent Away Average"]
    average_dict["Opponents Home Average"] = away_data["Opponent Home Average"]

    average_dict[f"{team} Home Average"] = home_data[f"{team} Home Average"]
    average_dict[f"{team} Away Average"] = away_data[f"{team} Away Average"]

    # fill up minimum dict
    min_dict["All Teams Home Minimum"] = league_data["League Home Minimum"]    
    min_dict["All Teams Away Minimum"] = league_data["League Away Minimum"]
    
    min_dict["Opponents Away Minimum"] = home_data["Opponent Away Minimum"]
    min_dict["Opponents Home Minimum"] = away_data["Opponent Home Minimum"]

    min_dict[f"{team} Home Minimum"] = home_data[f"{team} Home Minimum"]
    min_dict[f"{team} Away Minimum"] = away_data[f"{team} Away Minimum"]

    # fill up maximum dict
    max_dict["All Teams Home Maximum"] = league_data["League Home Maximum"]    
    max_dict["All Teams Away Maximum"] = league_data["League Away Maximum"]
    
    max_dict["Opponents Away Maximum"] = home_data["Opponent Away Maximum"]
    max_dict["Opponents Home Maximum"] = away_data["Opponent Home Maximum"]

    max_dict[f"{team} Home Maximum"] = home_data[f"{team} Home Maximum"]
    max_dict[f"{team} Away Maximum"] = away_data[f"{team} Away Maximum"]


    # fill up maximum dict
    std_dict["All Teams Home std"] = league_data["League Home std"]    
    std_dict["All Teams Away std"] = league_data["League Away std"]
    
    std_dict["Opponents Away std"] = home_data["Opponent Away std"]
    std_dict["Opponents Home std"] = away_data["Opponent Home std"]

    std_dict[f"{team} Home std"] = home_data[f"{team} Home std"]
    std_dict[f"{team} Away std"] = away_data[f"{team} Away std"]


    # fill up 25 percentile dict
    percen_25_dict["All Teams Home 25%"] = league_data["League Home 25%"]    
    percen_25_dict["All Teams Away 25%"] = league_data["League Away 25%"]
    
    percen_25_dict["Opponents Away 25%"] = home_data["Opponent Away 25%"]
    percen_25_dict["Opponents Home 25%"] = away_data["Opponent Home 25%"]

    percen_25_dict[f"{team} Home 25%"] = home_data[f"{team} Home 25%"]
    percen_25_dict[f"{team} Away 25%"] = away_data[f"{team} Away 25%"]


    # fill up 50 percentile dict
    percen_50_dict["All Teams Home 50%"] = league_data["League Home 50%"]    
    percen_50_dict["All Teams Away 50%"] = league_data["League Away 50%"]
    
    percen_50_dict["Opponents Away 50%"] = home_data["Opponent Away 50%"]
    percen_50_dict["Opponents Home 50%"] = away_data["Opponent Home 50%"]

    percen_50_dict[f"{team} Home 50%"] = home_data[f"{team} Home 50%"]
    percen_50_dict[f"{team} Away 50%"] = away_data[f"{team} Away 50%"]


    # fill up 75 percentile dict
    percen_75_dict["All Teams Home 75%"] = league_data["League Home 75%"]    
    percen_75_dict["All Teams Away 75%"] = league_data["League Away 75%"]
    
    percen_75_dict["Opponents Away 75%"] = home_data["Opponent Away 75%"]
    percen_75_dict["Opponents Home 75%"] = away_data["Opponent Home 75%"]

    percen_75_dict[f"{team} Home 75%"] = home_data[f"{team} Home 75%"]
    percen_75_dict[f"{team} Away 75%"] = away_data[f"{team} Away 75%"]

    # put all dicts in one main dict
    organized["Average"] = average_dict
    organized["Minimum"] = min_dict
    organized["Maximum"] = max_dict
    organized["std"] = std_dict
    organized["25%"] = percen_25_dict
    organized["50%"] = percen_50_dict
    organized["75%"] = percen_75_dict

    return organized

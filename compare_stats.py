def organizer(team, home_data, away_data, league_data):
    def add_stats(target, stat_name):
        target[f"All Teams Home {stat_name}"] = league_data[f"League Home {stat_name}"]
        target[f"All Teams Away {stat_name}"] = league_data[f"League Away {stat_name}"]
        target[f"Opponents Away {stat_name}"] = home_data[f"Opponent Away {stat_name}"]
        target[f"Opponents Home {stat_name}"] = away_data[f"Opponent Home {stat_name}"]
        target[f"{team} Home {stat_name}"] = home_data[f"{team} Home {stat_name}"]
        target[f"{team} Away {stat_name}"] = away_data[f"{team} Away {stat_name}"]

    organized = {}
    for stat_name in ("Average", "Minimum", "Maximum", "std", "25%", "50%", "75%"):
        organized[stat_name] = {}
        add_stats(organized[stat_name], stat_name)

    return organized

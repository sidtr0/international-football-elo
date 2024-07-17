import csv
import pandas as pd
import math

c = 400
k = 32

results = pd.read_csv("internation-football-results/results.csv")

for index, row in results.iterrows():
    home_team = row["home_team"]
    away_team = row["away_team"]
    home_score = row["home_score"]
    away_score = row["away_score"]
    home_outcome = 0.5
    print(home_team, home_score, away_team, away_score)

    if home_score > away_score:
        home_outcome = 1
    else:
        home_outcome = 0

    elos = pd.read_csv("elos.csv")

    try:
        home_elo = elos[elos["country"] == home_team]["elo"].to_list()[0]
        away_elo = elos[elos["country"] == away_team]["elo"].to_list()[0]

        home_index = elos.index[elos['country'] == home_team].tolist()[0]
        away_index = elos.index[elos['country'] == away_team].tolist()[0]
    except IndexError:
        pass

    qa = math.pow(10, home_elo/c)
    qb = math.pow(10, away_elo/c)
    expected_outcome = qa/(qa + qb)

    new_home_elo = home_elo + k*(home_outcome - expected_outcome)
    new_away_elo = away_elo + k*((1 - home_outcome) - (1 - expected_outcome))

    elos.loc[home_index, "elo"] = new_home_elo
    elos.loc[away_index, "elo"] = new_away_elo
    
    elos.to_csv("elos.csv", index=False)
import csv
import pandas

base_elo = 1000

countries = []

with open("internation-football-results/results.csv", mode="r", encoding="utf-8") as file:
    csvFile = csv.reader(file)
    for lines in csvFile:
        country_name = lines[1]
        if country_name not in countries:
            countries.append(country_name)

print(countries)

with open("elos.csv", mode="w", encoding="utf-8", newline="\n") as file:
    csvwriter = csv.writer(file)

    csvwriter.writerow(["country", "elo"])
    for country in countries:
        csvwriter.writerow([country, base_elo])
import random


numbers = None
tempature = None
season = None


numbers = ["-5", "-4", "-3", "-2", "-1", "0",
 "1", "2", "3", "4", "5", "6", "7", "8", "9",
"10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21",
 "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", "32", "33",
 "34", "35", "36"]

season = ["Spring", "Summer", "Autumn", "Winter"]

random_season = random.choice(season)


if random_season == "Spring":
    numbers = ["10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20"]
elif random_season == "Summer":
    numbers = ["25", "26", "27", "28", "29", "30", "31", "32", "33", "34", "35", "36"]
elif random_season == "Autumn":
    numbers = ["17", "18", "19", "20", "21", "22", "23", "24", "25"]
elif random_season == "Winter":
    numbers = ["-5", "-4", "-3", "-2", "-1", "0",  "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]

tempature = random.choice(numbers)

print(f"\nSeason: {random_season}")
print(f"Tempature: {tempature}")
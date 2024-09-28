import pandas as pd

# Age data
age_data = [12, 18, 13, 15]
names = ["e", "f", "a", "i"]
ages = pd.Series(age_data, index=names)

print(ages["i"])
print(ages[3])

#------------------------------------------

# Dictionary data
dictionary = {"i": 15, "f": 18, "e": 12, "a": 13}
ages = pd.Series(dictionary)

print(ages)
print(ages.sum())
print(ages.describe())

#------------------------------------------

# Subjects and scores
students = ["ayse", "burak", "cem", "didem", "elif"]
turkish_scores = [50, 55, 60, 65, 70]
chemistry_scores = [65, 70, 75, 80, 85]

turkish = pd.Series(turkish_scores, index=students)
chemistry = pd.Series(chemistry_scores, index=students)

print((chemistry + turkish) / 2)
print(chemistry.index)
print(chemistry.values)

#------------------------------------------

# Weighted average calculation
chemistry_weighted = (chemistry * 0.6)
turkish_weighted = (turkish * 0.4)

print(chemistry_weighted + turkish_weighted)

#---------------------------------------------

# Final and midterm scores
midterm = pd.Series([90, 50, 0, 50, 50])
final = pd.Series([80, 70, 0, 60, 70])

average = midterm * 0.4 + final * 0.6
print(average)

passed = (average > 70)
conditional = (average >= 60) & (average <= 70)
failed = (average < 60)

print(average[passed].count())
print(average[conditional].count())
print(average[failed].count())

#-----------------------------------------

# Reading data from CSV
read_data_wins = pd.read_csv("teams.csv", sep=";", usecols=["WINS"])
wins = read_data_wins.squeeze()

read_data_draws = pd.read_csv("teams.csv", sep=";", usecols=["DRAWS"])
draws = read_data_draws.squeeze()

points = wins * 3 + draws
print(points)

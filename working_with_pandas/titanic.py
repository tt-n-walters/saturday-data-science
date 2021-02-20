import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


plt.style.use("ggplot")

url = "https://gist.githubusercontent.com/tt-n-walters/66c3e1f0dc36842c64d4d61ade87e884/raw/5688648cc18a409c75b3cbe1f91434d0d7f4ec0d/titanic.csv"
data = pd.read_csv(url)

print(data.info())
print(data.columns)
print(data.shape)

# missing_cabin = data.cabin.isnull()
# print(data.cabin[missing_cabin].shape)

# missing_embarked = data.embarked.isnull()
# print(data.embarked[missing_embarked].shape)


gender_distribution = data.sex.value_counts()
gender_distribution.plot(kind="pie")
plt.legend(gender_distribution)
plt.savefig("sexes.png")

data.plot(kind="scatter", x="age", y="fare")
plt.savefig("ages_fare_scatter.png")

fig, axes = plt.subplots()
data.age.plot(kind="hist", fig=fig, axes=axes, bins=20, ylim=(0,55))
plt.savefig("ages_of_all.png")


is_male = data.sex == "male"
print(data[is_male].fare.describe())
is_female = data.sex == "female"
print(data[is_female].fare.describe())

fig, axes = plt.subplots(nrows=2)
male_money = data[is_male].fare
# male_money.plot(kind="bar", fig=fig, ax=axes[0], ylim=(0, 512))
female_money = data[is_female].fare
# female_money.plot(kind="bar", fig=fig, ax=axes[1], ylim=(0, 512))

plt.savefig("fares_by_gender.png")


average_age = round(data.age.mean(), 5)
print("Average age of all passengers:", average_age)

survived = data.survived == 1
passengers_survived = data[survived]
print("Passengers survived:", len(passengers_survived))
print("Average age of survivors:", round(passengers_survived.age.mean(), 5))

fig, axes = plt.subplots()
data[survived].age.plot(kind="hist", fig=fig, axes=axes, bins=20, ylim=(0,55))
plt.savefig("ages_of_survivors.png")



fig, axes = plt.subplots(ncols=2)
data.sex.value_counts().plot(kind="pie", ax=axes[0], title="All passengers")

survivors_by_gender = data[survived].sex.value_counts()
print(survivors_by_gender)
survivors_by_gender.plot(kind="pie", ax=axes[1], title="All passengers")

plt.savefig("genders_of_all.png")
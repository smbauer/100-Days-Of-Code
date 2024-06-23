import pandas as pd

# data = pd.read_csv("weather_data.csv")
# temp_c = data[data.day == "Monday"].temp[0]
# temp_f = 32 + (temp_c * 9 / 5)
# print(f"{temp_f=}")

data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
squirrel_counts_df = data["Primary Fur Color"].value_counts().to_frame()
squirrel_counts_df.to_csv("squirrel_counts.csv")
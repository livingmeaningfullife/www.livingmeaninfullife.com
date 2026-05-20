import pandas as pd

df = pd.read_csv('data.csv')

# df.fillna({'Calories': 130, 'Date': "'2020/12/22'"}, inplace = True)

x = df["Calories"].mean()
print(x)

df.fillna({"Calories": x}, inplace=True)
print(df.to_string())

import pandas as pd  

df = pd.read_csv("urban_growth.csv")

print(df.head())

print("\nDataset Information: ")
print(df.info())

print("\nStatistical Summary: ")
print(df.describe())

import matplotlib.pyplot as plt  

plt.figure(figsize=(8,5))

plt.plot(df["Year"], df["UrbanArea"], marker ="o")

plt.title("Urban Growth Over Time")
plt.xlabel("Year")
plt.ylabel("Urban Area (sq km)")

plt.grid(True)

plt.savefig("urban_growth_line_chart.png")
plt.show()

df["Growth"] = df["UrbanArea"].diff()

print(df)

print("\nMean value of Growth: ")
print(df["Growth"].mean())

plt.figure(figsize=(8,5))

plt.bar(df["Year"][1:], df["Growth"][1:])

plt.title("Urban Growth Between Years")
plt.xlabel("Year")
plt.ylabel("Growth (sq km)")

plt.savefig("urban_growth_bar_chart.png")
plt.show()

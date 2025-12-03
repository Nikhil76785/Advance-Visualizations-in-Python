import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("Iris.csv")

#Sir I found out you have to print the head function and use plt to show it thats why it was not working in VS Code
print(df.head())

plt.figure(figsize=(6,4))
sns.barplot(x="Species", y="SepalLengthCm", data=df)
plt.title("Bar Plot: Sepal Length vs Species")
plt.show()

plt.figure(figsize=(6,4))
sns.countplot(x="Species", data=df)
plt.title("Count of Species")
plt.show()

plt.figure(figsize=(6,4))
sns.boxplot(x="Species", y="SepalWidthCm", data=df)
plt.title("Box Plot: Sepal Width vs Species")
plt.show()

plt.figure(figsize=(6,4))
sns.swarmplot(x="Species", y="SepalWidthCm", data=df)
plt.title("Swarm Plot: Sepal Width vs Species")
plt.show()

plt.figure(figsize=(6,4))
sns.histplot(df["SepalWidthCm"], kde=True)
plt.title("Distribution of Sepal Width")
plt.show()

sns.jointplot(x="SepalWidthCm", y="SepalLengthCm", data=df, kind="scatter")
plt.show()

sns.pairplot(df.drop("Id", axis=1), hue="Species")
plt.show()
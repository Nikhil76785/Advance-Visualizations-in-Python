import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

weather = pd.read_csv(r"weatherdata.csv")
print(weather.head(10))
#weather.info()
sns.barplot(weather['wind_speed'])
plt.show()
sns.displot(weather['temperature'])
plt.show()
sns.jointplot(weather['humidity'])
plt.show()
sns.jointplot(weather['temperature'])
plt.show()
sns.pairplot(weather[['humidity', 'temperature', 'air_pollution_index']])
plt.show()
sns.stripplot(weather['weather_type'])
plt.show()
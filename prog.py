import pandas as pd
import seaborn as sns

weather = pd.read_csv(r"weatherdata.csv")
weather.head(10)
#weather.info()
sns.barplot(weather['wind_speed'])
sns.displot(weather['temperature'])
sns.jointplot(weather['humidity'])
sns.jointplot(weather['temperature'])
sns.pairplot(weather[['humidity', 'temperature', 'air_pollution_index']])
sns.stripplot(weather['weather_type'])
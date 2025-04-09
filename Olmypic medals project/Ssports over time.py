import pandas as pd

import seaborn as sns
import matplotlib.pyplot as plt


df= pd.read_csv('athlete_events.csv')

sports= df.groupby(['Year', 'Sport']).size().unstack(fill_value=0)
years=sports.index
sports_partcpation=sports.values
plt.figure(figsize=(12, 6))
for i, sport in enumerate(sports.columns):
    plt.bar(years, sports.iloc[:, i], label=sport)
plt.title('Sports Participation Over the Years in the Olympics')
plt.xlabel('Year')
plt.ylabel('Number of Athletes')
plt.xticks(rotation=45)
plt.tight_layout()
plt.legend(loc='upper right')
plt.show()
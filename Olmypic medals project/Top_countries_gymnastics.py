import pandas as pd

import seaborn as sns
import matplotlib.pyplot as plt


df= pd.read_csv('athlete_events.csv')

Gymnistics= df[df['Sport'] == 'Gymnastics']
Medal_winners = Gymnistics[Gymnistics['Medal'] != 'NA']
medals_by_country = Medal_winners.groupby(['NOC', 'Medal']).size().unstack(fill_value=0)
medals_by_country['Total Medals'] = medals_by_country.sum(axis=1)
sorted_medals = medals_by_country.sort_values(by='Total Medals', ascending=False)
countries = sorted_medals.index
gold = sorted_medals['Gold']
silver = sorted_medals['Silver']
bronze = sorted_medals['Bronze']
plt.figure(figsize=(12, 6))
plt.bar(countries, bronze, label='Bronze', color='#cd7f32', width=0.8)
plt.bar(countries, silver, bottom=bronze, label='Silver', color='#c0c0c0', width=0.8)
plt.bar(countries, gold, bottom=bronze + silver, label='Gold', color='#ffd700', width=0.8)
plt.title('Medal Distribution by Country in Gymnastics')
plt.xlabel('Country (NOC)')
plt.ylabel('Number of Medals')
plt.xticks(rotation=45)
plt.tight_layout()
plt.legend(loc='upper right')
plt.show()
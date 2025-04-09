import pandas as pd

import seaborn as sns
import matplotlib.pyplot as plt


df= pd.read_csv('athlete_events.csv')


gold_medals = df[df['Medal'] == 'Gold']
gold_medals_by_country = gold_medals.groupby('NOC').size().reset_index(name='Gold Medal Count')
top_countries = gold_medals_by_country.sort_values(by='Gold Medal Count', ascending=False).head(20)
plt.figure(figsize=(12, 6))
sns.barplot(data=top_countries, x='NOC', y='Gold Medal Count', palette='Blues')
plt.title('Top 10 Countries by Gold Medals')
plt.xlabel('Country (NOC)')
plt.ylabel('Gold Medal Count')
plt.xticks(rotation=45)
plt.show()
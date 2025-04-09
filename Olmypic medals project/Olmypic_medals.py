import pandas as pd

import seaborn as sns
import matplotlib.pyplot as plt


df= pd.read_csv('athlete_events.csv')
#task 1

# gold_medals = df[df['Medal'] == 'Gold']
# gold_medals_by_country = gold_medals.groupby('NOC').size().reset_index(name='Gold Medal Count')
# top_countries = gold_medals_by_country.sort_values(by='Gold Medal Count', ascending=False).head(20)
# plt.figure(figsize=(12, 6))
# sns.barplot(data=top_countries, x='NOC', y='Gold Medal Count', palette='Blues')
# plt.title('Top 10 Countries by Gold Medals')
# plt.xlabel('Country (NOC)')
# plt.ylabel('Gold Medal Count')
# plt.xticks(rotation=45)
# plt.show()


#task 2
# Gymnistics= df[df['Sport'] == 'Gymnastics']
# Medal_winners = Gymnistics[Gymnistics['Medal'] != 'NA']
# medals_by_country = Medal_winners.groupby(['NOC', 'Medal']).size().unstack(fill_value=0)
# medals_by_country['Total Medals'] = medals_by_country.sum(axis=1)
# sorted_medals = medals_by_country.sort_values(by='Total Medals', ascending=False)
# countries = sorted_medals.index
# gold = sorted_medals['Gold']
# silver = sorted_medals['Silver']
# bronze = sorted_medals['Bronze']
# plt.figure(figsize=(12, 6))
# plt.bar(countries, bronze, label='Bronze', color='#cd7f32', width=0.8)
# plt.bar(countries, silver, bottom=bronze, label='Silver', color='#c0c0c0', width=0.8)
# plt.bar(countries, gold, bottom=bronze + silver, label='Gold', color='#ffd700', width=0.8)
# plt.title('Medal Distribution by Country in Gymnastics')
# plt.xlabel('Country (NOC)')
# plt.ylabel('Number of Medals')
# plt.xticks(rotation=45)
# plt.tight_layout()
# plt.legend(loc='upper right')
# plt.show()


#task 3

# gender_partcpation=df.groupby(['Year', 'Sex']).size().unstack(fill_value=0)
# years=gender_partcpation.index
# male=gender_partcpation['M']
# female=gender_partcpation['F']
# plt.figure(figsize=(12, 6))
# plt.bar(years,male,label='male',color='blue',width=2)
# plt.bar(years,female,bottom=male, label='female',color='pink',width=2)
# plt.title("Gender partcpation over the years in the Olympics")
# plt.xlabel('Year')
# plt.ylabel('Number of Athletes')
# plt.xticks(rotation=45)
# plt.tight_layout()
# plt.legend(loc='upper right')
# plt.show()


#task 4

# sports= df.groupby(['Year', 'Sport']).size().unstack(fill_value=0)
# years=sports.index
# sports_partcpation=sports.values
# plt.figure(figsize=(12, 6))
# for i, sport in enumerate(sports.columns):
#     plt.plot(years, sports.iloc[:, i], label=sport)
# plt.title('Sports Participation Over the Years in the Olympics')
# plt.xlabel('Year')
# plt.ylabel('Number of Athletes')
# plt.xticks(rotation=45)
# plt.tight_layout()
# plt.legend(loc='upper right')
# plt.show()


#task 5


gold_medals = df[df['Medal'] == 'Gold']
age_of_gold_medalists = gold_medals.groupby('Age')
# print(gold_medals)
print(age_of_gold_medalists.head(5))

# plt.figure(figsize=(12, 6))
# plt.bar(age_of_gold_medalists.index, age_of_gold_medalists['Gold Medal Count'], color='gold')


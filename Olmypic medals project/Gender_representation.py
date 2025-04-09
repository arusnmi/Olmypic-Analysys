import pandas as pd

import seaborn as sns
import matplotlib.pyplot as plt


df= pd.read_csv('athlete_events.csv')

#task 3

gender_partcpation=df.groupby(['Year', 'Sex']).size().unstack(fill_value=0)
years=gender_partcpation.index
male=gender_partcpation['M']
female=gender_partcpation['F']
plt.figure(figsize=(12, 6))
plt.bar(years,male,label='male',color='blue',width=2)
plt.bar(years,female,bottom=male, label='female',color='pink',width=2)
plt.title("Gender partcpation over the years in the Olympics")
plt.xlabel('Year')
plt.ylabel('Number of Athletes')
plt.xticks(rotation=45)
plt.tight_layout()
plt.legend(loc='upper right')
plt.show()
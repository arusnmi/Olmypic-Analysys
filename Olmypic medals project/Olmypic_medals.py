import pandas as pd

import seaborn as sns
import matplotlib.pyplot as plt


df= pd.read_csv('athlete_events.csv')



gold_medals = df[df['Medal'] == 'Gold']
age_of_gold_medalists = gold_medals.groupby('Age').size().reset_index(name='Gold Medal Count')
number_of_gold_medalists = age_of_gold_medalists['Age']


plt.figure(figsize=(12, 6))
plt.bar(number_of_gold_medalists, age_of_gold_medalists['Gold Medal Count'], color='gold')
plt.title('Age of Gold Medalists Over the Years')
plt.xlabel('Age')
plt.ylabel('Number of Gold Medals')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()



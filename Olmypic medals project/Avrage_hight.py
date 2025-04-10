from numpy import size
import pandas as pd

import seaborn as sns
import matplotlib.pyplot as plt


df= pd.read_csv('athlete_events.csv')


df = df.dropna(subset=['Height', 'Year', 'Sex'])
avg_height = df.groupby(['Sex', 'Year'])['Height'].mean().reset_index()

male_height = avg_height[avg_height['Sex'] == 'M']
female_height = avg_height[avg_height['Sex'] == 'F']
plt.figure(figsize=(20,10))
plt.plot(male_height['Year'], male_height['Height'], label='Male', color='blue', marker='o')
plt.plot(female_height['Year'], female_height['Height'], label='Female', color='pink', marker='o')
plt.xticks(rotation=90)
plt.xlabel('Height')
plt.ylabel('Count')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
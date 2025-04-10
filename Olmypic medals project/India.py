import pandas as pd

import seaborn as sns
import matplotlib.pyplot as plt


df= pd.read_csv('athlete_events.csv')

india= df[df['NOC'] == 'IND']
indian_medals= india.groupby(['Year', 'Medal']).size().reset_index(name='Count')
indian_medals= indian_medals.dropna()
indian_medals['Year'] = indian_medals['Year'].astype(str)
plt.figure(figsize=(12, 6))
plt.title('Indian Medals Over the Years')
sns.barplot(data=indian_medals, x='Year', y='Count', hue='Medal')
plt.xticks(rotation=45)
plt.xlabel('Year')
plt.ylabel('Count')
plt.legend(title='Medal')
plt.tight_layout()
plt.show()

import pandas as pd

import seaborn as sns
import matplotlib.pyplot as plt


df= pd.read_csv('athlete_events.csv')

summer= df[df['Season'] == 'Summer']
sports_count = summer.groupby('Year')['Sport'].nunique()
plt.figure(figsize=(12, 6))
plt.bar(sports_count.index, sports_count.values, color='Yellow')
plt.title('Summer Sports Participation Over the Years in the Olympics')
plt.xlabel('Year')
plt.ylabel('Number of Athletes')
plt.xticks(rotation=45)
plt.tight_layout()
plt.legend(loc='upper right')
plt.show()
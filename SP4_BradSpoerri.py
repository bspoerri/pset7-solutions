# Brad Spoerri 
# DS5010 - SP26
# Problem Set 7 - Problem 4

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

diamonds = pd.read_csv('Files/diamonds.csv')

# groupby cut then find count for each cut type
cut_quality_dist = (diamonds.groupby(["cut"])["cut"]
                    .value_counts(ascending=False))

# create series with proportions of each cut grade
cut_quality_dist = cut_quality_dist / cut_quality_dist.sum() * 100

# create pie chart with prescribed formatting
plt.figure(figsize=(10,8))
plt.pie(cut_quality_dist, 
        autopct = '%.1f%%',
        colors=['crimson', 'orange', 'gold', 'limegreen', 'forestgreen'])
plt.title("Proportion of Diamonds by Cut Quality")
plt.legend(labels=cut_quality_dist.index, loc='lower right')
plt.show()
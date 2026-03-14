# Brad Spoerri 
# DS5010 - SP26
# Problem Set 7 - Problem 5

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

diamonds = pd.read_csv('Files/diamonds.csv')

# extract cut and price columns
clarity_and_price = diamonds.loc[:, ["clarity", "price"]]
# pull list of unique cut values
grade = clarity_and_price['clarity'].unique()
print()

# create a subplot for each grade of cut
fig, axes = plt.subplots(nrows=len(grade), ncols=1, 
                         figsize=(10, 2*len(grade)))

# iterate by cut grade and plot the distribution of prices for each cut
for i in range(len(grade)):
    axes[i].hist((clarity_and_price.
                  loc[clarity_and_price['clarity']==grade[i],"price"]),
                 bins=20,
                 color="cyan",
                 edgecolor='black')
    axes[i].set_title(f"Price Distribution for Clarity: {grade[i]}")
    axes[i].set_xlabel("Price")
    axes[i].set_ylabel("Count")

plt.tight_layout()
plt.savefig("problem_5_result.png")

# Brad Spoerri 
# DS5010 - SP26
# Problem Set 7 - Problem 2

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# question 2.1

# read diamonds.csv into df
diamonds = pd.read_csv('Files/diamonds.csv')

# groupby cut then find count for each cut type
cut_quality_dist = (diamonds.groupby(["cut"])["cut"]
                    .value_counts(ascending=False))

# plot bar chart with prescribed labelling and style
plt.bar(cut_quality_dist.index, cut_quality_dist, width=0.6, color="grey")
plt.xlabel('Cut Quality')
plt.ylabel('Number of Diamonds')
plt.title('Distribution of Diamonds by Cut')
plt.savefig("problem_2a_result.png")

# question 2.2
plt.figure()
# create df with just length
length_only = diamonds["x"]

# plot histogram with prescribed styling; density param used for frequency
plt.hist(length_only, density=True, color="lightblue", edgecolor="black")
plt.xlabel("Length (in mm)")
plt.ylabel("Frequency")
plt.title("Frequency Distribution of Diamonds by Length")
# exclude bins with no values
plt.xlim(3, 10) 
plt.savefig("problem_2b_result.png")
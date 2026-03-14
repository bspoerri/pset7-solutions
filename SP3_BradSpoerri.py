# Brad Spoerri 
# DS5010 - SP26
# Problem Set 7 - Problem 3

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

diamonds = pd.read_csv('Files/diamonds.csv')

# create sub-df with just carat and price columns
carat_and_price = diamonds.loc[:,['carat','price']]

# create scatter plot of carat vs price; replicating sample format
plt.figure(figsize=(12,6))
plt.scatter(carat_and_price.iloc[:,0], carat_and_price.iloc[:,1], 
            color='steelblue', alpha=0.5)
plt.xlabel("Carat")
plt.ylabel("Price")
plt.title("Price vs. Carat of Diamonds")
# show grid lines on y-axis only
plt.grid(axis='y')
# add text at position (3, 7000)
plt.text(3, 7000, 'Outlier') 
plt.savefig("problem_3_result.png")


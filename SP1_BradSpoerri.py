# Brad Spoerri 
# DS5010 - SP26
# Problem Set 7 - Problem 1

import numpy as np
import matplotlib.pyplot as plt

# create a 10x10 figure
figure = plt.figure(figsize=(10,10), dpi=50)

# add axes using ref: [left, bottom, width, height]
ax1 = figure.add_axes([0.075, 0.05, 0.85, 0.8])
ax2 = figure.add_axes([0.17, 0.5, 0.3, 0.225])
# generate x values and convert to numpy array
x = range(-20,20,1)
x = np.array(x)

# calculate y values for both functions
g_of_x = x / (1 + x**2)**0.5  
f_of_x = np.e**x / (1 + np.e**x)

# main plot - f(x)
ax1.plot(x, f_of_x, color='blue')
ax1.set_title(r"$f(x) = \frac{e^x}{1+e^x}$")
ax1.set_xlabel("x for f(x)")  
ax1.set_ylabel("f(x)")

# add plot for g(x)
ax2.plot(x, g_of_x, lw=2, linestyle='--', color='crimson')
ax2.set_title(r"$g(x) = \frac{x}{\sqrt{1+x^2}}$")
ax2.set_xlabel("x for g(x)")
ax2.set_ylabel("g(x)")

# save figure to file
plt.savefig("problem_1_result.png")
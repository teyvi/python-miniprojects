# This line plot is the population of the world for the past 60 years

# importing libraries
import matplotlib.pyplot as plt

# the data and its variables
year = [1950, 1970, 1990, 2010]
# pop is world population in billions
pop = [2.519, 3.692, 5.263, 6.972]

# lineplot
plt.plot(year, pop)
plt.show()

# scatterplot
plt.scatter(year, pop)
plt.show()

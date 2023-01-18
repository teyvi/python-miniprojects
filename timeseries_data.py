# Import libraries
import matplotlib.pyplot as plt
import pandas as pd
fig, ax = plt.subplots()

# Read the data from file using read_csv
climate_change = pd.read_csv('data/climate_change.csv', parse_dates=['date'],index_col = 'date')

# Add the time-series for "relative_temp" to the plot
ax.plot(climate_change.index, climate_change['relative_temp'])

# Set the x-axis label
ax.set_xlabel('Time')

# Set the y-axis label
ax.set_ylabel('Relative temperature (Celsius)')

# Show the figure
plt.show()


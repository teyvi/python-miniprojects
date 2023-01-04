# using indexing to select data

# Definition of countries and capital
countries = ['spain', 'france', 'germany', 'norway']
capitals = ['madrid', 'paris', 'berlin', 'oslo']

# Get index of 'germany': ind_ger
ind_ger =countries.index("germany")

# Use ind_ger to print out capital of Germany
print(capitals[ind_ger])


# creating a dictionary
# Definition of countries and capital
countries = ['spain', 'france', 'germany', 'norway']
capitals = ['madrid', 'paris', 'berlin', 'oslo']

# From string in countries and capitals, create dictionary europe
europe = {'spain':'madrid','france':'paris', 'germany':'berlin', 'norway':'oslo' }

# Print europe
print(europe)

# creating a manual dataframe
# importing libraries
import pandas as pd

names=['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt']
dr=[True, False, False, False, True, True, True]
cpc= [809, 731, 588, 18, 200, 70, 45]

# creating a manual dictionary
my_dict= {
'country':names , 'drivers_right':dr , 'cars_per_cap':cpc
}

# building the dataframe called cars
cars=pd.DataFrame(my_dict)

print(cars)
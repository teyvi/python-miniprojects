# importing libraries
import matplotlib.pyplot as plt
import pandas as pd

# read the tsv data
data = pd.read_csv ("data/gapminder.tsv", sep='\t')

print(data)
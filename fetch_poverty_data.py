import numpy as np
import pandas as pd
import csv

# fetchs the data and creates a sorted dataframe

# def fetch_poverty_data(state_list):
poverty_df = pd.read_csv('Poverty_Rate_v3.csv') # name of the file here
poverty_dataframe = poverty_df.loc[1:,['NAME','Year','S1701_C03_001E']] # S1701_C03_001E is the column name for the poverty rate dataset
poverty_dataframe.columns = ['State','Year','Poverty_Rate'] # changes the column names to make intuitive sense
poverty_dataframe["Year"] = pd.to_numeric(poverty_dataframe["Year"], downcast = "integer") # downcasts the datatype of year to integer
poverty_dataframe = poverty_dataframe.sort_values(['State','Year']) # sorts the dataframe by state and year

#     return poverty_dataframe

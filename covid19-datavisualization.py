# Hazel Zhou
# May 28, 2024
# Covid-19 data visualization

import pandas as pd
import matplotlib.pyplot as plt

# Load Covid-19 cvs data to dataframe
DATA_URL = 'https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-counties.csv'
df = pd.read_csv(DATA_URL)

# Clean data to only contain data from Washington State & after 2020-5-28
df = df[df['state'] == 'Washington']
df = df[df['date'] >= '2020-5-28']

# Below are different types of data visualization

# 1. Data table of the first 10 rows without fips and index
print("1. Data table of the first 10 rows without fips and index")
# create new dataframe without fips column
df_no_fips = df.drop(columns=['fips'])
# display the table
print("Table1. First 10 Rows of Covid-19 Data")
print(df_no_fips.head(10).to_string(index = False)) 

print('-'*80)

# 2. Bar chart of the number of cases in each county
print("2. Bar chart of the number of cases in each county")
# create new dataframe with each county's case sum
county_cases = df.groupby('county')['cases'].sum()
# plot the data
plt.figure(figsize=(15, 6))
county_cases.plot(kind='bar', color='lightgreen', edgecolor='black')
# customize the plot
plt.xlabel('County')
plt.ylabel('Total Cases')
plt.title('Figure1. Total Cases by County')
plt.xticks(rotation=45)
# display the plot
plt.show()

print('-'*80)

# 3. Line plot of cases vs time
print("3. Line plot of cases vs time")
# group data by date and sum cases
date_cases = df.groupby('date')['cases'].sum()
# plot the data
plt.figure(figsize=(15, 6))  # Set the size of the figure
date_cases.plot(kind='line', color='blue', marker='o')
# customize the plot
plt.xlabel('Date')
plt.ylabel('Total Cases')
plt.title('Figure2. Total Covid-19 cases after time in Washington State')
plt.xticks(rotation=45)
# display the plot
plt.show()
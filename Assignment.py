# Import libraries

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')

# Load the data
raw_data = pd.read_csv('https://raw.githubusercontent.com/fivethirtyeight/data/master/college-majors/recent-grads.csv')
raw_data

# Considering Sample Data
data = raw_data.iloc[:30,0:15]
data1 = data.copy()
data1 = data1.drop(['Major_code','Major','Total','Men','Women','Major_category','ShareWomen','Sample_size','Employed','Full_time_year_round', 'Unemployed'], axis = 1)
data1.to_csv('file.csv')

# 1. plot a graph considering parameter individually
plt.plot(data1['Rank'], data1['Full_time'], color = 'Green', marker = 'o')
plt.title('Simple line graph', fontsize = 14)
plt.xlabel('College Rank')
plt.ylabel('Full time')
plt.show()

plt.plot(data1['Part_time'],data1['Unemployment_rate'], color = 'red',marker = 'o')
plt.title('Simple line graph' , fontsize = 14)
plt.xlabel('Part time')
plt.ylabel('Unemployment rate')
plt.show()

# 2. Plot the graph using all parameter in one
df = data1.copy()
df.set_index('Rank',inplace = True)
df.plot()
plt.show()
df.to_csv('File2.csv')


# Bar graph between college rank ,college jobs and non-college jobs
new_data = raw_data.copy()
cols = [0,18,19]
new_data = new_data[new_data.columns[cols]]
final = new_data.iloc[:30,:]
final
plt.bar(final['Rank'],final['College_jobs'], color = 'blue', width = 0.9)
plt.xlabel('College rank')
plt.ylabel('College jobs')
plt.show()

plt.bar(final['Rank'],final['Non_college_jobs'], color = 'black',width = 0.9)
plt.xlabel('College rank')
plt.ylabel('non college jobs')
plt.show()
final.to_csv('File3.csv')
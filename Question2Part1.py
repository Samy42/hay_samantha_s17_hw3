
# coding: utf-8

# In[1]:

import numpy
import pandas


# In[2]:

#read data from csv to data frame
df = pandas.read_csv('./Data/employee_compensation.csv')

#drop unnecessary columns
df.drop(df.columns[0:3], axis = 1, inplace = True)
df.drop(df.columns[1], axis = 1, inplace = True)
df.drop(df.columns[2:-1], axis = 1, inplace = True)


# In[3]:

#sort dataframe by total compensation
df = df.sort_values(by='Total Compensation', ascending = False)


# In[4]:

#group the data by the organization group and department
df = df.groupby(('Organization Group','Department')).mean()


# In[5]:

#write the data to a csv
df.to_csv('./Output/Question2Part1Output.csv')


# In[6]:

#print the first few rows of the output for verification
print(df.head().to_string())


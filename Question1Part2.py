
# coding: utf-8

# In[1]:

import pandas
import numpy


# In[2]:

# import csv
df = pandas.read_csv('./Data/vehicle_collisions.csv')


# In[3]:

# remove unnecessary columns from data
df.drop(df.columns[0:3], axis = 1, inplace = True)
df.drop(df.columns[1:16], axis = 1, inplace = True)
df.drop(df.columns[-5:], axis = 1, inplace = True)


# In[4]:

#group the data by the borough
data = df.groupby('BOROUGH')
data = data.count()


# In[5]:

#rename the columns to reflect the number of vehicles involved
data.rename(index=str, columns={'VEHICLE 1 TYPE':'ONE_VEHICLE_INVOLVED','VEHICLE 2 TYPE':'TWO_VEHICLES_INVOLVED','VEHICLE 3 TYPE':'THREE_VEHICLES_INVOLVED','VEHICLE 4 TYPE':'MORE_VEHICLES_INVOLVED','VEHICLE 5 TYPE':'FIVE_VEHICLES_INVOLVED'},inplace = True)


# In[6]:

#data was in num(or more) involved so subtracting next column from each entry
data['ONE_VEHICLE_INVOLVED'] = data['ONE_VEHICLE_INVOLVED'] - data['TWO_VEHICLES_INVOLVED']
data['TWO_VEHICLES_INVOLVED'] = data['TWO_VEHICLES_INVOLVED'] - data['THREE_VEHICLES_INVOLVED']
data['THREE_VEHICLES_INVOLVED'] = data['THREE_VEHICLES_INVOLVED'] - data['MORE_VEHICLES_INVOLVED']


# In[7]:

#remove last column as that is not necessary
data.drop('FIVE_VEHICLES_INVOLVED',axis=1, inplace = True)


# In[8]:

#print the data to a csv file
data.to_csv('./Output/Question1Part2Output.csv')


# In[10]:

#print the first few rows to verify output
data.head()


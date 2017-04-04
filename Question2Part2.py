
# coding: utf-8

# In[1]:

import numpy
import pandas


# In[2]:

#read in data
df = pandas.read_csv('./Data/employee_compensation.csv')


# In[3]:

#identify Fiscal years
df['Fiscal'] = df['Year Type'] == 'Fiscal'
#delete rows with fiscal year data
df = df.drop(df[df['Fiscal']].index)
#drop column used to idenfity fiscal rows
df.drop(df.columns[-1], axis = 1, inplace = True)


# In[4]:

#create job family lookup table based on employee number
employees = df.copy()
employees.drop(employees.columns[0:9], axis = 1, inplace = True)
employees.drop(employees.columns[1:3], axis = 1, inplace = True)
employees.drop(employees.columns[2:11], axis = 1, inplace = True)
employees.head()


# In[5]:

# group the data by employee ID number
data = df.groupby('Employee Identifier').mean()


# In[6]:

#create a dumplicate of the index value for job family lookup later
data['Employee Identifier'] = data['Year'].index


# In[7]:

#calculate 5th percentile of salaries
topOvertimeCutoff = data[data.columns[6]].quantile(.05)
#create a column to identify if employee earned more in overtime than the 5% salary cutoff
data['Not Top Overtime'] = data['Overtime'] < topOvertimeCutoff
#drop all employees that are not in the top overtime earners
data = data.drop(data[data['Not Top Overtime']].index)
#drop column used to determine if employee was a top overtime earner
data.drop(data.columns[-1], axis = 1, inplace = True)


# In[8]:

#merge job family back into table
data = data.merge(employees, on='Employee Identifier')


# In[9]:

#group data by Job Family
data = data.groupby('Job Family').mean()


# In[10]:

#drop unnecessary columns
data.drop(data.columns[0:10], axis = 1, inplace = True)
data.drop(data.columns[2], axis = 1, inplace = True)


# In[11]:

#calculate benefits percentage as a function of total compensation
data['Percent_Total_Benefit'] = 100*(data['Total Benefits']/data['Total Compensation'])


# In[12]:

#sort by this percentage
data = data.sort_values(by='Percent_Total_Benefit', ascending = False)


# In[13]:

#output data to csv
data.to_csv('./Output/Question2Part2Output.csv')


# In[14]:

#print top few rows of data
data.head()


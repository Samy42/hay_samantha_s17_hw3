
# coding: utf-8

# In[1]:

import pandas


# In[2]:

#import data
df = pandas.read_csv('./Data/cricket_matches.csv')


# In[3]:

#drop all unnecessary columns
df.drop(df.columns[0:6], axis = 1, inplace = True)
df.drop(df.columns[3:5], axis = 1, inplace = True)
df.drop(df.columns[3:4], axis = 1, inplace = True)
df.drop(df.columns[5:8], axis = 1, inplace = True)
df.drop(df.columns[7:12], axis = 1, inplace = True)


# In[4]:

#add boolean column with value if home team lost
df['NotHomeWinner'] = df['home'] != df['winner']

#remove all rows where the home team lost
df = df.drop(df[df['NotHomeWinner']].index)

#delete the column added with home team win data as it is now unnecessary
df.drop(df.columns[-1], axis = 1, inplace = True)


# In[5]:

#get winning team's score
df['Score'] = df[['innings1_runs','innings2_runs']].max(axis=1)


# In[6]:

#drop all but the last column
df.drop(df.columns[1:-1], axis = 1, inplace = True)


# In[7]:

#group the data by the home team and average their winning scores
df = df.groupby('home').mean()


# In[8]:

#print data to csv
df.to_csv('./Output/Question3Part1Output.csv')


# In[9]:

#print top 5 rows
df.head()



# coding: utf-8

# In[1]:

import pandas


# In[2]:

#read in csv to pandas data frame
df = pandas.read_csv('./Data/vehicle_collisions.csv')


# In[3]:

#create a data frame to convert numeric months to text
monthLookup = pandas.DataFrame(['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'], index=['1','2','3','4','5','6','7','8','9','10','11','12'], columns = ['Month'])


# In[4]:

#this function takes in a date in string format mm/dd/yyyy and outputs the text of the month name
def strDateToMonth(d):
    if d[1] == '/':
        month = d[0]
    else:
        month = d[0:2]
        
    return monthLookup['Month'][month]


# In[5]:

#adds a column to main data frame with the name of the month
df['MONTH'] = df['DATE'].apply(strDateToMonth)


# In[6]:

#create a new data frame for formatted output
data = pandas.DataFrame()


# In[7]:

#load in a column of the month names
data['MONTH'] = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']


# In[8]:

#create a new data frame counting the total accidents per month
NYCcount = df.groupby('MONTH', sort = False).size().to_frame()
NYCcount['MONTH'] = NYCcount.index
NYCcount = NYCcount.rename(index=str, columns={0:'NYC'})


# In[9]:

#create a new data frame counting the total accidents per month in manhattan
MANcount = df.groupby(('BOROUGH','MONTH'), sort = False).size().reset_index()
MANcount = MANcount.loc[MANcount['BOROUGH'] == 'MANHATTAN']
MANcount = MANcount.rename(index=str, columns={0:'MANHATTAN'})


# In[10]:

#merge the NYC and Manhattan counts into the output data frame
data = pandas.merge(data,MANcount)
data = pandas.merge(data,NYCcount)
data.drop('BOROUGH',axis=1, inplace=True)


# In[11]:

#calculate the percentage of accidents in manhattan for each month
data['PERCENTAGE'] = data['MANHATTAN']/data['NYC']
#output the correctly formatted values to a new csv
data.to_csv('./Output/Question1Part1Output.csv')


# In[12]:

#print the first 5 rows of the output
data.head()


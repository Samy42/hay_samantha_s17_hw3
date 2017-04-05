
# coding: utf-8

# In[1]:

import pandas
import numpy
import re


# In[2]:

#import data
df = pandas.read_csv('./Data/movies_awards.csv')


# In[3]:

#drop unimportant columns
df.drop(df.columns[0:5], axis = 1, inplace = True)
df.drop(df.columns[1:10], axis = 1, inplace = True)
df.drop(df.columns[2:7], axis = 1, inplace = True)


# In[4]:

# add in blank columns for the awards
df['Awards_won'] = 0
df['Awards_nominated'] = 0
df['Prime_Awards_won'] = 0
df['Prime_Awards_nominated'] = 0
df['Oscars_Awards_won'] = 0
df['Oscars_Awards_nominated'] = 0
df['Golden_Globe_Awards_won'] = 0
df['Golden_Globe_Awards_nominated'] = 0
df['BAFTA_Awards_won'] = 0
df['BAFTA_Awards_nominated'] = 0


# In[5]:

#this takes in a string and extracts the set of awards indicated by that string
def extractAwards(awardString):
    #split string into substrings
    awardString = awardString.replace('. ',',')
    awardString = awardString.replace('& ',',')
    awardString = awardString.split(',')
    
    
    return [intrepretAward(a) for a in awardString]


# In[6]:

#this takes in a substring which contains an award type and count, and extracts that information
def intrepretAward(awardSubString):
    #split string into words
    words = awardSubString.split(' ')
    winType = 'win(s)' #default = win, unless otherwise found
    number = 0 #number of awards = 0 until found otherwise
    
    #make strings lowercase to limit iterations
    #also deletes trailing period and finds the number of awards
    for w in range(len(words)):
        if len(words[w]):
            words[w] = words[w].lower()
            if words[w][-1] == '.':
                words[w].replace('.','')
            if words[w].isdigit():
                number = words[w]
    
    #determine award type
    awardType = 'unknown'
    if words.count('primetime'):
        awardType = 'Prime'
    if words.count('oscar') or words.count('oscars'):
        awardType = 'Oscars'
    if words.count('golden'):
        awardType = 'Golden_Globe' 
    if words.count('bafta'):
        awardType = 'BAFTA'
    
    
    #wins or nominations
    if words.count('nomination') or words.count('nomination.') or words.count('nominations.') or words.count('nominated.') or words.count('nominations') or words.count('nominated'):
        winType = 'nomination(s)'
            
    return [awardType,winType,number]


# In[7]:

#turning off warning as the code is working as intended
pandas.options.mode.chained_assignment = None

for row in range(len(df['Title'])):
    #iterates over each row in the data frame
    
    #check if row contains a valid string to parse, then send it to be parsed
    if type(df['Awards'][row]) == str:
        awards = extractAwards(df['Awards'][row])

        for a in range(len(awards)):
            column= '' #start with a null column
            if awards[a][-1]:
                if awards[a][0] != 'unknown':
                    #add in the award name to the column to find the correct column
                    column = awards[a][0] + '_' 
                column = column + 'Awards'

                # pick correct column based on if award was won or just nominated
                if awards[a][1] == 'win(s)':
                    column = column + '_won'
                else:
                    column = column + '_nominated'

                # put the number of awards into the correct column
                df[column][row] = awards[a][-1]
        


# In[8]:

# add specific awards won or nomated to the total awards won or nominated
df['Awards_won'] = df['Awards_won'] + df['Prime_Awards_won'] + df['Oscars_Awards_won'] + df['Golden_Globe_Awards_won'] + df['BAFTA_Awards_won']

df['Awards_nominated'] = df['Awards_nominated'] + df['Prime_Awards_nominated'] + df['Oscars_Awards_nominated'] + df['Golden_Globe_Awards_nominated'] + df['BAFTA_Awards_nominated']


# In[9]:

#print data to csv
df.to_csv('./Output/Question4Part1Output.csv')


# In[10]:

#print first few rows of data
print(df.head().to_string())



# coding: utf-8

# In[1]:

import pandas
import numpy
import re
import pprint


# In[2]:

df = pandas.read_csv('./Data/movies_awards.csv')


# In[3]:

df.drop(df.columns[0:5], axis = 1, inplace = True)
df.drop(df.columns[1:10], axis = 1, inplace = True)
df.drop(df.columns[2:7], axis = 1, inplace = True)
df.head()


# In[4]:

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

def extractAwards(awardString):
    #split string into substrings
    awardString = awardString.replace('. ',',')
    awardString = awardString.replace('& ',',')
    awardString = awardString.split(',')
    
    
    return [intrepretAward(a) for a in awardString]


# In[6]:

def intrepretAward(awardSubString):
    #split string into words
    words = awardSubString.split(' ')
    winType = 'win(s)'
    number = 0
    
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
    if words.count('nomination') or words.count('nominations') or words.count('nominated'):
        winType = 'nomination(s)'
            
    return [awardType,winType,number]


# In[7]:

pandas.options.mode.chained_assignment = None
for row in range(len(df['Title'])):
    
    if type(df['Awards'][row]) == str:
        awards = extractAwards(df['Awards'][row])

        for a in range(len(awards)):
            column= ''
            if awards[a][-1]:
                if awards[a][0] != 'unknown':
                    column = awards[a][0] + '_'
                column = column + 'Awards'

                if awards[a][1] == 'win(s)':
                    column = column + '_won'
                else:
                    column = column + '_nominated'

                df[column][row] = awards[a][-1]
        


# In[8]:

df.to_csv('./Output/Question4Part1Output.csv')


# In[9]:

print(df.head().to_string())


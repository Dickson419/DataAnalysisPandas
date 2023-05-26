import pandas as pd

"""
Modifying dataframes - Updating rows and columns
"""
df = pd.read_csv('pokemon_data.csv', index_col='Number')

"""Look at columns"""
#print(df.columns)

"""You can change all names in the columns... but not used often"""
df.columns = ['Name', 'Type 1', 'Type 2', 'HP', 'Attack', 'Defense', 'Special. Atk',
       'Special Def', 'Speed', 'Generation', 'Legendary']
#print(df.columns)

"""Change to upper to lower, get rid of spaces etc -> list comprehension -> useful for using methods"""
df.columns = [x.lower() for x in df.columns]
#print(df.columns)

df.columns = df.columns.str.replace(' ', '_')
#print(df.columns)

"""Rename specific columns -> dictionary"""
df.rename(columns= {'special._atk': 'sp_atk',
                    'special_def': 'sp_def'}, inplace=True)
print(df.columns)

"""Updating all data in rows"""
print(df.loc[2]) #get all colum data for the row
df.loc[2] = ['Steveosaur', 'Flame', 'Dirt', '70', '74','80','100','90','78','86','True'] #change all data
print(df.loc[2])

"""Updating specific rows"""
df.loc[2, ['name', 'attack']] = ['Ivysaur', '62'] #use second argument to input an array of columns with data to change
print(df.loc[2])
#one value
df.loc[2, ['legendary']] = ['False']
print(df.loc[2])

### Use of a filter for specific values to change
filt = (df['name'] == 'Charmander') #find row with the name Charmander
print(df[filt]['type_1'] == 'Flame!') #will not work --> use .loc! BELOW
df.loc[filt, 'type_1'] = 'Flame!'
print(df.head())
print("\n\n----- ----- ----- \n\n")


"""Updating multiple rows of data - change all names to lower then title case"""
filt2 = df['name'].str.upper() #can chanhe .title to any str method
print(filt2)

#assignment can be used with this
print('\n----- Use of assignment for data frames -----\n')
df['name'] = df['name'].str.title()
print(df.head())

##### ADVANCED METHODS - apply, map, applymap and replace #####
print("\n\nApply - used for calling a function on values. Works for data frames or a series (a column)")
#for instance, check the length of each name
df['name'].apply(len) #function goes inside the apply brackets
print(df['name'].apply(len))

##Apply can also be used to update values...
def updateName(name):
    return name.replace('s', '$')
print(df['name'].apply(updateName)) #no parenthesis as it does not need to be executed
df['name'] = df['name'].apply(updateName)
print(df)

##lambda functions can be used for simply functions/tasks
print(df['name'].apply(lambda x: x.upper())) #lambda NAME of what is passed in : WHAT happens to it

### TO use apply on a data frame ###
print(df.apply(len)) #shows how many values are in each column i.e name has 800 things

##EXAMPLE - get minimun value from each column
#print(df.apply(pd.Series.min)) ERRor - mixed data?

###applymap - only works on dataframes. Applies function to each oject in data frame i.e adds up all 0,0 then 0,1 0,2 etc etc
### Can be used to change all strings to upper/lower etc rather than by column
### mixed data needs different more advanced fucntions
print("Applymap - only works on data frames")
#appmap = df.applymap(len)
#print(appmap)
#appmap2 = df.applymap(lambda x: len(x) if isinstance(x, str) else x)
#print(appmap2)

### MAP - works in series (by column) to apply something. i.e Substitute names
print("\nMAP function - NOTE values which are not changed are then NaN value (not a number value)\n")
dfmap = df['name'].map({'Diancie' : 'Who da fuck!', 'Volcanion': 'Dickhead new pokemon'})
print(dfmap)
#to keep all other values .replace can be used
dfmap2 = df['name'].replace({'Diancie' : 'Who da fuck!', 'Volcanion': 'Dickhead new pokemon'})
print(dfmap2)







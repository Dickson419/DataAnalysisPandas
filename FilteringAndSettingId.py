import pandas as pd

"""
Read in the data BUT pick a unique index id to use --> saves setting index later! Helps with cleaning.
Filtering and creating variables as data frames.
Use of logical operators to further filter data.
"""
df = pd.read_csv('pokemon_data.csv', index_col='Number')
#print(df.head())

"""Filtering - conditionals to filter rows and columns"""
print('\n\n----- Filtering -----\n\n')

#find items/rows with generation == 1
print(df['Generation'] == 1) #true or false values are returned

#this can be put in a variable...
filt = df['Generation'] == 1 #filter is a Python keyword so use something different


print("\n----- All first generation Pokemon! -----")
print(df[filt])
print(df.loc[filt]) #give the same result... BUT allows us to get specific columns as well!
print(df.loc[filt, 'Name'])

print("\n----- Filter Mew or Dragonite -----\n")
filt2 = (df['Name'] == 'Dragonite') | (df['Name'] == 'Mew')
print(df[filt2])

### Try and get only gen 1 pokemon fire types
print("\n----- CHALLENGE: Gen 1 pokemon fire types -----\n")
filt3 = (df['Generation'] == 1 & (df['Type 1'] == 'Fire'))
print(df.loc[filt3])
#this can be further specified... display only fire types and their name, hp, attack and defense
print(df.loc[filt3, ['Name', 'HP', 'Attack', 'Defense']])

"""Filter by multiple vlues"""
types = ['Water', 'Grass']
filt4 = (df['Type 1'].isin(types)) & (df['Generation'] == 1)

print("\n----- Filtering by multiple values -----")
print(df.loc[filt4])


"""Filtering with string methods - for when values are separated by ;- etc and you want to get one key word"""
print("\n----- Filter with string methods -----\n")
filt5 = (df['Name'].str.contains('mega')) | (df['Name'].str.contains('Mega')) #contains(word to find, fill value to ignore i.e n/a)
print(df.loc[filt5])

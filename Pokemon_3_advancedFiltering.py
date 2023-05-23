import pandas as pd
import regex


"""
Some advanced searching methods with conditionals
"""
#pd.set_option('display.max_columns', None)
df = pd.read_csv('Modified_pokemon.csv')

#specify all columns with one variable in
print(df.loc[df['Type 1'] == 'Fire']) #get all fire pokemon
#specify two variables and return them
print(df.loc[(df['Type 1'] == 'Grass') & (df['Type 2'] == 'Poison')]) #get all fire pokemon AND poison
#conditions > < can also be set
print(df.loc[(df['Type 1'] == 'Grass') & (df['Type 2'] == 'Poison') & (df['HP'] > 70)]) #get all fire pokemon AND poison with HP > 100

"""Query results can be saved as a new data frame and saved as a separate csv"""
new_df = df.loc[(df['Type 1'] == 'Water') & (df['Type 2'] == 'Ice') & (df['HP'] > 50)] #get all fire pokemon AND poison with HP > 100
print(new_df)
#new_df.to_csv('WaterAndIce.csv')

"""Index can be rest"""
new_df = new_df.reset_index(drop=True) #drop=true gets rid of old indicies
print(new_df)
# OR it can be done in place --> new_df.reset_index(drop=True, inplace=True) just include inplace

print("\n\n\n")
"""
Filtering out name which contain 'mega' 
Uses the contains function which can be very powerful.
Regex (regular expressions) can be used. Needs to be imported
"""
#df.loc[(df['Type 1'] == 'Water') & (df['Type 2'] == 'Ice') & (df['HP'] > 50)]

print(df.loc[df['Name'].str.contains('Mega')]) #similar syntax to above. Shows all names with mega in them
print(df.loc[~df['Name'].str.contains('Mega')]) # ~ <-- means NOT
no_megas = df.loc[~df['Name'].str.contains('Mega')]
#no_megas.to_csv('noMegas.csv')

"""Use of regex expressions - Returns only fire and grass types"""
print(df.loc[df['Type 1'].str.contains('fire|grass', flags=regex.I, regex=True)]) #flag = ignore case

#Find all pokemon with a name starting with Pixxxx
print(df.loc[df['Name'].str.contains('^pi[a-z]*', flags=regex.I, regex=True)]) # ^ --> start of line. * --> zero or more


"""Make changes to categories i.e change a type such as fire to hotStuff"""
df.loc[df['Type 1'] == 'Fire', 'Type 1'] = 'Hot Stuff'
print(df)
#change back
df.loc[df['Type 1'] == 'Hot Stuff', 'Type 1'] = 'Fire'
print(df)




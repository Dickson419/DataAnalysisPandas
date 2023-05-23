import pandas as pd

"""
Data can be read in so let's start making changes to it...

- Add ALL of the stats together to make a super stat
"""

df = pd.read_csv('pokemon_data.csv') #df = dataFrame

# ----- Combine columns into a new column
#HP,Attack,Defense,Sp. Atk,Sp. Def,Speed <--- Stats to combine
df['Total'] = df['HP'] + df['Attack'] + df['Defense'] + df['Sp. Atk'] + df['Sp. Def'] + df['Speed'] #new column heading 'total'

#print(df.head(5))
print(df.sort_values('Total').head(5))

# ----- Drop a column -----
#df = df.drop(columns = ['Total']) #need to reassign as a variable for it to work
#print(df.head(5))

# ----- A faster method -----
#df['Total'] = df.iloc[:, 4:10].sum(axis=1) #remember to go one extra than needed! : before , means select all rows
#print(df.head(5))

# ----- Move the Total column to a different place -----
#Get columns as a list
cols = list(df.columns)
print(df.columns)
#order by column headings --> #,Name,Type 1,Type 2,HP,Attack,Defense,Sp. Atk,Sp. Def,Speed,Generation,Legendary

df = df[cols[0:4] + [cols[-1]] + cols[4:12]] #single items, total, must be placed inside a list

print(df.head(5))
print(df.columns)

"""Saving the new csv"""
df.to_csv('Modified_pokemon.csv', index=False) #index=false removes the indexes on the LHS. sep=/t seperates by tabs not commas







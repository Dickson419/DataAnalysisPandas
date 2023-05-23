import pandas as pd

"""
First of all data needs to be loaded in --> as a data frame.
This is what Pandas allows you to manipulate data with.
"""

# Set display options to show all rows and columns
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

df = pd.read_csv('pokemon_data.csv') #df = dataFrame
# print(df.head(3))
# print(df.tail(5)) #all data or top/bottom can be printed

"""Reading in data. Different headers can be used"""
## ----- Read headers -----

#print(df.columns)

# ----- Read each column -----

#print(df['Name'][0:10])
#print(df.Name) #also works!
#print(df[['Name', 'Type 1', 'HP']])

## ----- Read each row -----

#print(df.iloc[1]) #used integer look up. Displays contents of a row

# for index, row in df.iterrows():
#     #print(index, row)
#     print(index, row['Name'])

#print(df.loc[df['Type 1'] == 'Fire']) # [df['Type 1'] is the column // followed by a boolean statement for a match.
                                      # Is anything in column Type 1 equal to 'Fire'?

## ----- Read specific locations (R/C) -----

#print(df.iloc[2][1])

## ----- Useful commands/methods -----

#print(df.describe()) #gives various high level overviews i.e mean/mode/std dev
print(df.sort_values(['Type 1', 'HP'])) #column value to sort, true is default. Arrays for multiple parameters

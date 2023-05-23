import pandas as pd

"""
Statistical analysis with the groupby function
"""

# """Average HP and Attack of Pokemon grouped by each type i.e does poison has best attach?"""

# Read the Pokémon dataset from a CSV file
df = pd.read_csv('Modified_pokemon.csv')
# df.groupby(['Type 1']).mean()


# Select numeric columns for calculation
numeric_cols = ['HP', 'Attack', 'Defense']

# Convert selected columns to numeric data type
df[numeric_cols] = df[numeric_cols].apply(pd.to_numeric, errors='coerce').sort_values('Defense', ascending=False)

# Group Pokémon by Type 1 and calculate the mean values
grouped_df = df.groupby(['Type 1'])[numeric_cols].mean()

# Print the result
print(grouped_df)
import pandas as pd
# readng two csv and comparng same columns
df = pd.read_csv('filtered_data_with_loc.csv')
df1 = pd.read_csv('commit_data.csv')
# to compare each column and copy the result s matchng found..
for outer_index, outer_row in df.iterrows():
    for inner_index, inner_row in df1.iterrows():
        if outer_row['Dataset ID'] == inner_row['Dataset ID']:
            df.at[outer_index, 'Commit Size'] = inner_row['Commit Amount']


df.to_csv('filtered_data_with_loc_commit_count.csv', index=False)

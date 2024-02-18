import pandas as pd

# Assuming you have a DataFrame with columns 'ML TD Type' and 'total'
file = "one_new_components.csv"
df_1 = pd.read_csv(file)

# Drop duplicate rows based on all columns
df_1 = df_1.drop_duplicates()

# Group by 'ML Pipeline Stage' and 'ML TD Type', and calculate the sum for each group
grouped_df_1 = df_1.groupby(['ML Pipeline Stage', 'ML TD Type'])['Principal_Component'].sum().reset_index()

# Sort by the 'Principal_Component' column in descending order
grouped_df_1 = grouped_df_1.sort_values(by='Principal_Component', ascending=False)


# Print the aggregated scores sorted by the highest to the lowest
grouped_df_1

grouped_df_1.to_csv("all_ranking.csv", index = None)

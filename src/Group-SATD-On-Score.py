import pandas as pd


df = pd.read_csv(r'D:\Me\concordia\Notes\SE4AI\project\Implementation\Implementation-Git\SOEN-691-Project\data\dataset_with_normalized_used_metric_v3.csv')

# Group by 'ML SATD Type' and calculate the mean of 'Weighted Average' for each group
grouped_df = df.groupby('ML TD Type')['Weighted Average'].mean().reset_index()

# Sort the DataFrame by the mean values in descending order
sorted_df = grouped_df.sort_values(by='Weighted Average', ascending=False)

# Save the sorted DataFrame to a new CSV file
sorted_df.to_csv(r'D:\Me\concordia\Notes\SE4AI\project\Implementation\Implementation-Git\SOEN-691-Project\data\sorted_weighted_average_by_ML_SATD_Type.csv', index=False)

import pandas as pd
import os


file_path = r'D:\Me\concordia\Notes\SE4AI\project\Implementation\Implementation-Git\SOEN-691-Project\data\dataset_with_normalized_used_metric_v2.csv'
df = pd.read_csv(file_path)

# Define weights
weights = {'NLC': 0.143,
           'TFI': 0.143,
            'CS': 0.143,
           'ANL': 0.143,
           'ANC': 0.143,
           'AVT': 0.143,
           'AVM': 0.143,
           }

# Calculate Weighted Average for each row
df['Weighted Average'] = (df[list(weights.keys())] * pd.Series(weights)).sum(axis=1) / sum(weights.values())

# Save the updated DataFrame (including the new column) back to the same CSV file
df.to_csv(file_path, index=False)

print("Weighted Average column appended and CSV updated.")

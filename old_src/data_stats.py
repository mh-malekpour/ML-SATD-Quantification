import pandas as pd
import numpy as np

# Load your CSV data into a DataFrame
# Replace 'your_data.csv' with the actual name of your CSV file
df = pd.read_csv('SOEN-691-Project/data_with_metrics.csv')

# Assuming 'ML TD Type' is the column containing ML SATD types
ml_satd_types = df['ML TD Type'].unique()

# Create a new DataFrame to store the summary statistics
summary_df = pd.DataFrame(columns=['ML SATD Type', 'Mean Lines of Code End', 'Mean Complexity End', 'Mean Commits Between Start End', 'Median Lines of Code End', 'Median Complexity End', 'Median Commits Between Start End', 'STD Lines of Code End', 'STD Complexity End'])

# Loop through each ML SATD type
for ml_satd_type in ml_satd_types:
    # Select data for the current ML SATD type
    ml_satd_data = df[df['ML TD Type'] == ml_satd_type]
    ml_satd_data = ml_satd_data.dropna(subset=['Lines of Code End', 'Complexity End', 'Commits Between Start End'])



    # Check if there is sufficient data for the ML SATD type
    if not ml_satd_data.empty:
        # Calculate mean, median, and standard deviation for specific columns
        mean_lines_of_code_end = np.mean(ml_satd_data['Lines of Code End'])
        mean_complexity_end = np.mean(ml_satd_data['Complexity End'])
        mean_commits_between_start_end = np.mean(ml_satd_data['Commits Between Start End'])

        median_lines_of_code_end = np.median(ml_satd_data['Lines of Code End'])
        median_complexity_end = np.median(ml_satd_data['Complexity End'])
        median_commits_between_start_end = np.median(ml_satd_data['Commits Between Start End'])

        std_lines_of_code_end = np.std(ml_satd_data['Lines of Code End'])
        std_complexity_end = np.std(ml_satd_data['Complexity End'])

        # Append the summary statistics to the new DataFrame
        summary_df = summary_df.append({
            'ML SATD Type': ml_satd_type,
            'Mean Lines of Code End': mean_lines_of_code_end,
            'Mean Complexity End': mean_complexity_end,
            'Mean Commits Between Start End': mean_commits_between_start_end,
            'Median Lines of Code End': median_lines_of_code_end,
            'Median Complexity End': median_complexity_end,
            'Median Commits Between Start End': median_commits_between_start_end,
            'STD Lines of Code End': std_lines_of_code_end,
            'STD Complexity End': std_complexity_end
        }, ignore_index=True)
summary_df.to_csv('SOEN-691-Project/data_stats.csv', index=False)

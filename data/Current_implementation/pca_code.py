import pandas as pd
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

data = "dataset_with_normalized_used_metric_v3.csv"

# Load your data
df = pd.read_csv(data)  # Replace 'your_data.csv' with the actual filename

# Select the features for PCA
features = df[['NLC', 'CS', 'TFI', 'ANL', 'ANC', 'AVT', 'AVM']]
features.fillna(features.mean(), inplace=True)

#print(features.columns)
#features.head()


# Apply PCA
pca = PCA(n_components=1)  # You can experiment with the number of components
principal_components = pca.fit_transform(features)

# Create a DataFrame with the principal components
df_pca = pd.DataFrame(data=principal_components, columns=['Principal_Component'])

# Assign ranks based on the principal components
df_pca['Rank'] = df_pca['Principal_Component'].rank(ascending=False)

# Concatenate the original DataFrame with the PCA results and ranks
df_result = pd.concat([df, df_pca], axis=1)

# Display the resulting DataFrame with ranks
df_result.to_csv("one_components.csv", index=None)
df_result[['NLC', 'CS', 'TFI', 'ANL', 'ANC', 'AVT', 'AVM', 'Rank']]

file = "one_components.csv"
df_1 = pd.read_csv(file)

# Group by 'ML TD Type' and calculate the sum for each group
grouped_df_1 = df_1.groupby(['ML TD Type', 'ML Pipeline Stage'])['Principal_Component'].sum().reset_index()

# Sort by the 'total' column in descending order
grouped_df_1 = grouped_df_1.sort_values(by='Principal_Component', ascending=False)

# Print the aggregated scores sorted by the highest to the lowest
grouped_df_1

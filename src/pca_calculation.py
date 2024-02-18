import pandas as pd
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

data = "dataset_with_normalized_used_metric_v2.csv"

# Load your data
df = pd.read_csv(data)  # Replace 'your_data.csv' with the actual filename

# Select the features for PCA
features = df[['NLC', 'CS', 'TFI', 'ANL', 'ANC', 'AVT', 'AVM']]
features.fillna(features.mean(), inplace=True)

# Standardize the features
scaler = StandardScaler()
standardized_features = scaler.fit_transform(features)

# Apply PCA
pca = PCA(n_components=1)  # You can experiment with the number of components
principal_components = pca.fit_transform(standardized_features)

# Create a DataFrame with the principal components
df_pca = pd.DataFrame(data=principal_components, columns=['Principal_Component'])

# Assign ranks based on the principal components
df_pca['Rank'] = df_pca['Principal_Component'].rank(ascending=False)

# Concatenate the original DataFrame with the PCA results and ranks
df_result = pd.concat([df, df_pca], axis=1)

# Display the resulting DataFrame with ranks
df_result[['NLC', 'CS', 'TFI', 'ANL', 'ANC', 'AVT', 'AVM', 'Rank']]
df_result.to_csv("one_new_components.csv", index=None)

df_result

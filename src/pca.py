import pandas as pd
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

# Load your data
data = "dataset_with_used_metric.csv"

# Load your data
df = pd.read_csv(data)  # Replace 'your_data.csv' with the actual filename

# Select the features for PCA
features = df[['CS', 'TFI', 'ANL', 'ANC', 'AVT', 'AVM', 'NLC']]
features.fillna(features.mean(), inplace=True)

# Standardize features
scaler = StandardScaler()
standardized_features = scaler.fit_transform(features)

# Apply PCA with n_components=None
pca = PCA(n_components=1)
principal_components = pca.fit_transform(standardized_features)

# Display the explained variance ratio to decide on the number of components to keep
print("Explained Variance Ratio:")
print(pca.explained_variance_ratio_)

# Concatenate the original DataFrame with the PCA results
df_pca = pd.concat([df, pd.DataFrame(data=principal_components, columns=[f'PC_{i+1}' for i in range(len(features.columns))])], axis=1)

df_pca.to_csv("all_seven_features.csv", index=None)

# Display the resulting DataFrame with principal components
df_pca.head()

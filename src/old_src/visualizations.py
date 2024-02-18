import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Your data statistics
data = {
    'ML SATD Type': ['MCM', 'Data Conf', 'MLKnow', 'MCR', 'DS Configuration', 'Weight Conf', 'MCC', 'Proto', 'UMC', 'MDepend', 'HP Conf', 'UMC', 'CDT', 'MLInter', 'Layer Conf'],
    'Mean Lines of Code End': [1103.25, 332.5217391, 209.8666667, 300.75, 268.8, 16.66666667, 230.25, 443, 326.75, 612.2857143, 232, 491, 285, 121, 277],
    'Mean Complexity End': [187.75, 78.39130435, 41.2, 78.5, 42.7, 4.666666667, 38, 115.25, 46.5, 94, 38, 72.36363636, 65.8, 19, 56],
    'Mean Commits Between Start End': [62.75, 116.173913, 245.8, 15.25, 339, 7, 61, 119.5, 31.25, 109.8571429, 252.75, 80, 253.4, 192, 124],
    'Median Lines of Code End': [960, 150, 166, 142.5, 159, 7, 204, 261.5, 326, 587, 114, 304, 283, 121, 174],
    'Median Complexity End': [139, 41, 31, 32.5, 22.5, 2, 34, 62.5, 38.5, 108, 15, 39, 47, 19, 21.5],
    'Median Commits Between Start End': [42, 12, 46, 4, 81, 8, 50, 12.5, 19.5, 145, 270.5, 16, 13, 192, 42.5],
    'STD Lines of Code End': [451.4395724, 383.4624713, 165.2278696, 316.2375492, 324.1233716, 16.57977349, 157.0435847, 356.8480069, 299.0671956, 425.9029783, 265.5569619, 508.7860776, 228.6140853, 0, 267.3153568],
    'STD Complexity End': [168.3825629, 98.36433568, 40.68119959, 89.43852637, 47.29704008, 5.249338583, 29.74054472, 111.8690641, 44.55614436, 62.50485695, 48.27007354, 84.29738778, 69.48784066, 0, 69.32171377]
}

df = pd.DataFrame(data)

# Visualizing feature distributions using box plots
features = ['Lines of Code End', 'Complexity End', 'Commits Between Start End']

for feature in features:
    plt.figure(figsize=(12, 6))
    sns.boxplot(x='ML SATD Type', y=f'Mean {feature}', data=df, color='blue', label='Mean')
    sns.boxplot(x='ML SATD Type', y=f'Median {feature}', data=df, color='green', label='Median')
    sns.boxplot(x='ML SATD Type', y=f'STD {feature}', data=df, color='orange', label='STD')
    plt.title(f'Distribution of {feature} for Different ML SATD Types')
    plt.legend()
    plt.show()

# Visualizing correlations using a heatmap
correlation_matrix = df.corr()
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=.5)
plt.title('Correlation Heatmap of Features')
plt.show()

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

# Load the iris dataset
url = "https://raw.githubusercontent.com/uiuc-cse/data-fa14/gh-pages/data/iris.csv"
iris = pd.read_csv(url)

# Inspect the dataset
print("First 5 rows of the dataset:")
print(iris.head())

# Select the features for clustering
X = iris.drop('species', axis=1)

# Standardize the features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Perform k-Means clustering
kmeans = KMeans(n_clusters=3, random_state=0)
kmeans.fit(X_scaled)
labels = kmeans.labels_

# Add the cluster labels to the original dataframe
iris['cluster'] = labels

# Reduce dimensions to 2D for visualization using PCA
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)
iris['pca1'] = X_pca[:, 0]
iris['pca2'] = X_pca[:, 1]

# Visualize the clusters
plt.figure(figsize=(10, 6))
sns.scatterplot(data=iris, x='pca1', y='pca2', hue='cluster', palette='viridis', style='species', s=100)
plt.title('K-Means Clustering of Iris Dataset')
plt.xlabel('PCA Component 1')
plt.ylabel('PCA Component 2')
plt.legend()
plt.show()

# Display the cluster centers
print("\nCluster Centers (standardized):")
print(kmeans.cluster_centers_)

# Optional: Display the original species vs clusters
species_vs_cluster = pd.crosstab(iris['species'], iris['cluster'], rownames=['Species'], colnames=['Cluster'])
print("\nSpecies vs Cluster:")
print(species_vs_cluster)

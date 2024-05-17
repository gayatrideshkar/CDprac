import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

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

# Perform K-means clustering
kmeans = KMeans(n_clusters=3, random_state=0)
kmeans.fit(X_scaled)
labels = kmeans.labels_

# Add the cluster labels to the original dataframe
iris['cluster'] = labels

# Visualize the clusters
plt.figure(figsize=(12, 6))

# Scatter plot for Sepal Length vs Sepal Width
plt.subplot(1, 2, 1)
sns.scatterplot(data=iris, x='sepal_length', y='sepal_width', hue='cluster', palette='viridis', style='species')
plt.title('Sepal Length vs Sepal Width')
plt.xlabel('Sepal Length')
plt.ylabel('Sepal Width')

# Scatter plot for Petal Length vs Petal Width
plt.subplot(1, 2, 2)
sns.scatterplot(data=iris, x='petal_length', y='petal_width', hue='cluster', palette='viridis', style='species')
plt.title('Petal Length vs Petal Width')
plt.xlabel('Petal Length')
plt.ylabel('Petal Width')

plt.tight_layout()
plt.show()

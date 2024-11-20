# Write a program of cluster analysis using simple k-means algorithm Python/R programming language. 

import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.datasets import load_iris
from sklearn.decomposition import PCA
# Load the Iris dataset
iris = load_iris()
X = iris.data
y = iris.target  # Actual labels (used here just for comparison)
# Initialize and fit the KMeans algorithm with 3 clusters
kmeans = KMeans(n_clusters=3, random_state=0)
kmeans.fit(X)
# Get cluster labels and centers
labels = kmeans.labels_
centers = kmeans.cluster_centers_
# Use PCA to reduce data to 2 dimensions for visualization
pca = PCA(2)
X_pca = pca.fit_transform(X)
# Plot the clusters
plt.figure(figsize=(8, 5))
plt.scatter(X_pca[:, 0], X_pca[:, 1], c=labels, cmap='viridis', marker='o', edgecolor='k')
plt.scatter(pca.transform(centers)[:, 0], pca.transform(centers)[:, 1], c='red', marker='X', s=200, label='Centroids')
plt.title("K-means Clustering on Iris Dataset")
plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")
plt.legend()
plt.show()
# Optional: Compare predicted clusters with actual labels
print("Predicted labels:", labels)
print("Actual labels:", y)

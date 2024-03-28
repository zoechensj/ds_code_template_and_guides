### What is it?
This project is to solve unsupervised learning problem. The dataset is from Kaggle. The goal is to cluster the customers based on their spending behaviours.

### Algorithm used
The algorithm used in this project is Kmeans clustering and Agglomerative clustering. The model also used PCA to reduce the dimensionality of the data.

Kmeans Clustering:
- The KMeans algorithm is a centroid-based technique. It's iterative, it starts by making random initial guesses of centroids, and then assigns each data point to the nearest cluster. It then calculates the centroids of the new clusters, and repeats the process until the centroids do not change significantly.
- Pros:
    - Simple and easy to implement.
    - Easy to interpret the clustering results.
    - Fast and efficient in terms of computational cost.
- Cons:
    - The algorithm is sensitive to the initial random selection of centroids.
    - Doesn't work well with non-spherical data. It assumes that the clusters are spherical and evenly sized, which is not always the case in real-world data. DBScan is better for non-spherical data.
    - The number of clusters must be specified beforehand. We can use the elbow method to find the optimal number of clusters, as well as what the business needs for the clustering results.

Agglomerative Clustering:
- Agglomerative clustering is a hierarchical clustering technique. It starts by treating each data point as a single cluster, and then successively merges pairs of clusters until all clusters have been merged into a single cluster that contains all data points.
- Pros:
    - No need to specify the number of clusters beforehand.
    - Can accommodate different shapes of clusters.
    - Can be used to create a dendrogram, which can help us understand the relationships between clusters.
  - Cons:
    - Computationally expensive, especially for large datasets.
    - Not suitable for large datasets.
  
DBScan (this algorithm is not used in this project):
- DBScan is a density-based clustering algorithm. It groups together points that are closely packed together, marking as outliers points that lie alone in low-density regions. Main concepts are core points, border points, and noise points to form clusters.
- Pros:
    - Can find arbitrarily shaped clusters.
    - Outlier detection. Capable of detecting outliers in the data making it robust to noise.
    - No need to specify the number of clusters beforehand.
- Cons:
    - Sensitive to the hyperparameters epsilon and min_samples. Need to be tuned correctly for the algorithm to work well.
    - Not suitable for clusters of varying densities.
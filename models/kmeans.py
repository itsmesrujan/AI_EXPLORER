import numpy as np
from sklearn.cluster import KMeans

class Kmeans:
    def __init__(self):
        'model class for K-Means clustering'
        pass

    def generate_synthetic_data(self, n_samples_per_cluster=150, random_state=42):
        try:
            np.random.seed(random_state)
            X = np.vstack([
                np.random.randn(n_samples_per_cluster, 2) + np.array([0, 0]),
                np.random.randn(n_samples_per_cluster, 2) + np.array([5, 5]),
                np.random.randn(n_samples_per_cluster, 2) + np.array([0, 5])
            ])
            return X
        except Exception as e:
            print(f"Error while generating synthetic data: {e}")
            return None
    
    def get_kmeans_cluster_data(self, clusters=3, r_state=42):
        try:
            ''' Returns synthetic data and fits KMeans model '''
            return KMeans(n_clusters=clusters, random_state=r_state)
        except Exception as e:
            print(f"Error while creating KMeans model: {e}")
            return None
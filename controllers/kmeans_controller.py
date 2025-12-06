from models.kmeans_clustering import KmeansClusterModel

class KMeansController:
    def __init__(self):
        'Controller class for Kmeans'
        pass

    def get_kmeans_data(self):
        kmeans_instance = KmeansClusterModel()
        x = kmeans_instance.get_synthetic_data()
        cluster_data = kmeans_instance.get_cluster_data()
        y = cluster_data.fit_predict(x)
        return x, cluster_data, y
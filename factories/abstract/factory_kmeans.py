from factories.abstract.ifactory_demo import IDemoFactory
from factories.abstract.concrete_kmeans_canvas import KMeansCanvas

class KMeanFactory(IDemoFactory):
    def __init__(self):
        'Interface class for KMeans Factory'
        super().__init__()
        pass

    def create_model(self):
        from models.kmeans_clustering import KmeansClusterModel
        return KmeansClusterModel()

    def create_canvas(self):
        return KMeansCanvas(self.create_model())
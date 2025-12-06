from views.factories.abstract.idemo_factory import IDemoFactory
from views.factories.abstract.kmeans_canvas_concrete import KMeansCanvas

class KMeanFactory(IDemoFactory):
    def __init__(self):
        'Interface class for KMeans Factory'
        super().__init__()
        pass

    def create_canvas(self):
        return KMeansCanvas()
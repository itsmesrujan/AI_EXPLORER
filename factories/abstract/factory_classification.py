from factories.abstract.ifactory_demo import IDemoFactory
from factories.abstract.concrete_classification_canvas import ClassificationCanvas

class ClassificationFactory(IDemoFactory):
    def __init__(self):
        'Interface class for Classification Factory'
        super().__init__()
        pass

    def create_model(self):
        from models.classification import Classification
        return Classification()

    def create_canvas(self):
        return ClassificationCanvas(self.create_model())
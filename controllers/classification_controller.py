from models.classification import Classification

class ClassificationController:
    def __init__(self):
        'Controller class for Classification'
        pass

    def get_classification_data(self):
        classification_instance = Classification()
        x, y = classification_instance.get_classification_data()
        return x, y
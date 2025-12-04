from factories.abstract.ifactory_demo import IDemoFactory
from factories.abstract.concrete_linear_regression_canvas import LinearRegressionCanvas

class LinearRegressionFactory(IDemoFactory):
    def __init__(self):
        'Interface class for Linear Regression Factory'
        super().__init__()
        pass

    def create_model(self):
        from models.linear_regression import LinearRegression
        return LinearRegression()

    def create_canvas(self):
        return LinearRegressionCanvas(self.create_model())
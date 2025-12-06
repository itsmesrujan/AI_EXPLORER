from views.factories.abstract.idemo_factory import IDemoFactory
from views.factories.abstract.linear_regression_canvas_concrete import LinearRegressionCanvas

class LinearRegressionFactory(IDemoFactory):
    def __init__(self):
        'Interface class for Linear Regression Factory'
        super().__init__()
        pass

    def create_canvas(self):
        return LinearRegressionCanvas()
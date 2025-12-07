from models.linear_regression import LinearRegression

class LinearRegressionController:
    def __init__(self):
        'Controller class for Linear Regression'
        pass

    def get_plot_data(self):
        lr_instance = LinearRegression()
        return lr_instance.get_linear_plot_data()
from sklearn.linear_model import LinearRegression as LinearModel
import numpy as np

class LinearRegression:
    def __init__(self):
        'model class for linear regression'
        self._model = LinearModel()

    def __get_random_value(self, n_samples=100):
        try:
            return np.random.rand(n_samples, 1)
        except Exception as e:
            print(f"Error while generating random values: {e}")
            return None

    def get_linear_plot_data(self, n_samples=100):
        try:
            x_axis = 2 * self.__get_random_value(n_samples)
            y_axis = 4 + 3 * x_axis + self.__get_random_value(n_samples)
            self._model.fit(x_axis, y_axis)
            x_new = np.array([[0], [2]])
            y_predict = self._model.predict(x_new)
            return x_axis, y_axis, x_new, y_predict
        except Exception as e:
            print(f"Error while generating linear plot data: {e}")
            return None, None, None, None
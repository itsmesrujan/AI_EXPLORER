from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton
from models.common import Common
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

class LinearRegressionDemo(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.setLayout(layout)
        __common_instance = Common()
        self.__figure = __common_instance.get_plot_figure()
        self.__canvas = FigureCanvas(self.__figure)
        self.__button = QPushButton("Generate Regression")
        self.__button.clicked.connect(self.run_demo)
        layout.addWidget(self.__canvas)
        layout.addWidget(self.__button)

    def run_demo(self):
        from models.linear_regression import LinearRegression
        linear_regression_instance = LinearRegression()
        x, y, x_new, y_predict = linear_regression_instance.get_linear_plot_data()
        self.__figure.clear()
        # Axes object to plot data onto the Figure
        ax = self.__figure.add_subplot(111)
        ax.scatter(x, y, color="blue")
        ax.plot(x_new, y_predict, color="red")
        ax.set_title("Linear Regression Demo")
        self.__canvas.draw()

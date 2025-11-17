from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

class LinearRegressionDemo(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.setLayout(layout)
        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        self.button = QPushButton("Generate Regression")
        self.button.clicked.connect(self.run_demo)
        layout.addWidget(self.canvas)
        layout.addWidget(self.button)

    def run_demo(self):
        X = 2 * np.random.rand(100, 1)
        y = 4 + 3 * X + np.random.randn(100, 1)
        model = LinearRegression()
        model.fit(X, y)
        X_new = np.array([[0], [2]])
        y_predict = model.predict(X_new)
        self.figure.clear()
        ax = self.figure.add_subplot(111)
        ax.scatter(X, y, color="blue")
        ax.plot(X_new, y_predict, color="red")
        ax.set_title("Linear Regression Demo")
        self.canvas.draw()

from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton
from models.common import Common
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

class ClassificationDemo(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.setLayout(layout)
        self.__classification_instance = None
        self.__figure = Common.get_classification_figure()
        self.__canvas = FigureCanvas(self.__figure)
        self.__button = QPushButton("Generate Classification Demo")
        self.__button.clicked.connect(self.__run_demo)
        layout.addWidget(self.__canvas)
        layout.addWidget(self.__button)

    def __run_demo(self):
        from models.classification import Classification
        self.__classification_instance = Classification()
        X, y = self.__classification_instance.get_classification_data()
        # Plot
        self.__figure.clear()
        ax = self.__figure.add_subplot(111)
        ax.scatter(X[:, 0], X[:, 1], c=y, cmap='bwr')
        ax.set_title("Decision Tree Classification Demo")
        self.__canvas.draw()
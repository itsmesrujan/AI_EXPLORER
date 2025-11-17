from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton
import matplotlib.pyplot as plt
from sklearn.datasets import make_classification
from sklearn.tree import DecisionTreeClassifier
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

class ClassificationDemo(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.setLayout(layout)
        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        self.button = QPushButton("Generate Classification Demo")
        self.button.clicked.connect(self.run_demo)
        layout.addWidget(self.canvas)
        layout.addWidget(self.button)

    def run_demo(self):
        X, y = make_classification(
            n_samples=200,
            n_features=2,
            n_redundant=0,
            n_clusters_per_class=1,
            random_state=42
        )
        model = DecisionTreeClassifier().fit(X, y)
        # Plot
        self.figure.clear()
        ax = self.figure.add_subplot(111)
        ax.scatter(X[:, 0], X[:, 1], c=y, cmap='bwr')
        ax.set_title("Decision Tree Classification Demo")
        self.canvas.draw()
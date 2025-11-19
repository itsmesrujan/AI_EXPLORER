from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton
import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import KMeans
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

class KMeansDemo(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.setLayout(layout)
        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        self.button = QPushButton("Run K-Means Clustering")
        self.button.clicked.connect(self.run_demo)
        layout.addWidget(self.canvas)
        layout.addWidget(self.button)

    def run_demo(self):
        # Generate synthetic data
        np.random.seed(42)
        X = np.vstack([
            np.random.randn(150, 2) + np.array([0, 0]),
            np.random.randn(150, 2) + np.array([5, 5]),
            np.random.randn(150, 2) + np.array([0, 5])
        ])
        kmeans = KMeans(n_clusters=3, random_state=42)
        labels = kmeans.fit_predict(X)
        self.figure.clear()
        ax = self.figure.add_subplot(111)
        ax.scatter(X[:, 0], X[:, 1], c=labels, cmap="viridis")
        ax.scatter(kmeans.cluster_centers_[:, 0],
                   kmeans.cluster_centers_[:, 1],
                   marker='X', s=200, c='red')
        ax.set_title("K-Means Clustering Demo")
        self.canvas.draw()

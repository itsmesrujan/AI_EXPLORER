from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton
from models.common import Common
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

class KMeansDemo(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.setLayout(layout)
        __common_instance = Common()
        self.__figure = __common_instance.get_plot_figure()
        self.__canvas = FigureCanvas(self.__figure)
        self.__button = QPushButton("Run K-Means Clustering")
        self.__button.clicked.connect(self.__run_demo)
        layout.addWidget(self.__canvas)
        layout.addWidget(self.__button)

    def __run_demo(self):
        from models.kmeans import Kmeans
        lKmeans = Kmeans()
        # get synthetic data
        X = lKmeans.generate_synthetic_data()
        kmeans_cluster = lKmeans.get_kmeans_cluster_data()
        labels = kmeans_cluster.fit_predict(X)
        self.__figure.clear()
        # Axes object to plot data onto the Figure
        ax = self.__figure.add_subplot(111)
        ax.scatter(X[:, 0], X[:, 1], c=labels, cmap="viridis")
        ax.scatter(kmeans_cluster.cluster_centers_[:, 0],
                   kmeans_cluster.cluster_centers_[:, 1],
                   marker='X', s=200, c='red')
        ax.set_title("K-Means Clustering Demo")
        self.__canvas.draw()

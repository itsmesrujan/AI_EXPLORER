from views.factories.abstract.icanvas_concrete import ICanvas

class KMeansCanvas(ICanvas):
    def __init__(self):
        super().__init__()
        self.button.setText("Run K-Means Clustering Demo")
        self.button.clicked.connect(self.__runDemo)

    def __runDemo(self):
        from controllers.kmeans_controller import KMeansController
        kmeans_instance = KMeansController()
        x, cluster_data, y = kmeans_instance.get_kmeans_data()
        self.figure.clear()
        # Axes object to plot data on to Figure
        ax = self.figure.add_subplot(111)
        ax.scatter(x[:, 0], x[:, 1], c=y, cmap='viridis')
        ax.scatter(cluster_data.cluster_centers_[:, 0],
                   cluster_data.cluster_centers_[:, 1],
                   marker='x',
                   s=200,
                   c='red')
        ax.set_title("K-Means Clustering Demo")
        self.canvas.draw()
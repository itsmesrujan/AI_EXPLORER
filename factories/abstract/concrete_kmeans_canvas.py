from factories.abstract.iconcrete_canvas import ICanvas

class KMeansCanvas(ICanvas):
    def __init__(self, model):
        super().__init__()
        self.model = model
        self.button.clicked.connect(self.__runDemo)

    def __runDemo(self):
        x = self.model.get_synthetic_data()
        cluster_data = self.model.get_cluster_data()
        y = cluster_data.fit_predict(x)
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
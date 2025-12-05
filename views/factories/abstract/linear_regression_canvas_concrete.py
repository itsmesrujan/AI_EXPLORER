from views.factories.abstract.icanvas_concrete import ICanvas

class LinearRegressionCanvas(ICanvas):
    def __init__(self, model):
        super().__init__()
        self.model = model
        self.button.clicked.connect(self.__runDemo)

    def __runDemo(self):
        x, y, x_new, y_predict = self.model.get_linear_plot_data()
        self.figure.clear()
        # Axes object to plot data onto the Figure
        ax = self.figure.add_subplot(111)
        ax.scatter(x, y, color="blue")
        ax.plot(x_new, y_predict, color="red")
        ax.set_title("Linear Regression Demo")
        self.canvas.draw()
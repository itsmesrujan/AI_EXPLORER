from views.factories.abstract.icanvas_concrete import ICanvas

class LinearRegressionCanvas(ICanvas):
    def __init__(self):
        super().__init__()
        self.button.setText("Run Linear Regression Demo")
        self.button.clicked.connect(self.__runDemo)

    def __runDemo(self):
        from controllers.linear_regression_controller import LinearRegressionController
        lr_instance = LinearRegressionController()
        x, y, x_new, y_predict = lr_instance.get_plot_data()
        self.figure.clear()
        # Axes object to plot data onto the Figure
        ax = self.figure.add_subplot(111)
        ax.scatter(x, y, color="blue")
        ax.plot(x_new, y_predict, color="red")
        ax.set_title("Linear Regression Demo")
        self.canvas.draw()
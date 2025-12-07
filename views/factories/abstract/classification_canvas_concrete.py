from views.factories.abstract.icanvas_concrete import ICanvas

class ClassificationCanvas(ICanvas):
    def __init__(self):
        super().__init__()
        self.button.clicked.connect(self.__runDemo)

    def __runDemo(self):
        from controllers.classification_controller import ClassificationController
        classification_instance = ClassificationController()
        x, y = classification_instance.get_classification_data()
        # plot
        self.figure.clear()
        ax = self.figure.add_subplot(111)
        ax.scatter(x[:, 0], x[:, 1], c=y, cmap='bwr')
        ax.set_title('Decision Tree Classification Demo')
        self.canvas.draw()

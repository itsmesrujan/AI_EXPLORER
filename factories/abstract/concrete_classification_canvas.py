from factories.abstract.iconcrete_canvas import ICanvas

class ClassificationCanvas(ICanvas):
    def __init__(self, model):
        super().__init__()
        self.model = model
        self.button.clicked.connect(self.__runDemo)

    def __runDemo(self):
        x, y = self.model.get_classification_data()
        # plot
        self.figure.clear()
        ax = self.figure.add_subplot(111)
        ax.scatter(x[:, 0], x[:, 1], c=y, cmap='bwr')
        ax.set_title('Decision Tree Classification Demo')
        self.canvas.draw()

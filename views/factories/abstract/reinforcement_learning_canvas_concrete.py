from views.factories.abstract.icanvas_concrete import ICanvas

class ReinforcementCanvas(ICanvas):
    def __init__(self):
        'Reinforcement Learning Canvas Concrete Implementation'
        super().__init__()
        self.button.setText("Run Reinforcement Learning Demo")
        self.button.clicked.connect(self._run_demo)

    def _run_demo(self):
        from controllers.reinforcement_learning_controller\
             import ReinforcementLearningController
        reinforcement_instance = ReinforcementLearningController()
        grid, cmap, norm = reinforcement_instance._get_learning_data()
        # plot
        self.figure.clear()
        ax = self.figure.add_subplot(111)
        ax.imshow(grid, cmap=cmap, norm=norm)
        ax.set_title("Reinforcement Learning (Q-Learning) Path")
        ax.grid(True, color="black", linewidth=1)
        self.canvas.draw()

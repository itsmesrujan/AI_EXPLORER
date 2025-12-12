from views.factories.abstract.idemo_factory import IDemoFactory
from views.factories.abstract.reinforcement_learning_canvas_concrete import ReinforcementCanvas

class ReinforcementLearningFactory(IDemoFactory):
    def __init__(self):
        'Interface class for Reinforcement Learning Factory'
        super().__init__()
        pass

    def create_canvas(self):
        return ReinforcementCanvas()
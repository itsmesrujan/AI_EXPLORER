# Demo Factory Interface
class IDemoFactory:
    def __init__(self):
        'Interface class for Demo Factories'
        pass

    def create_canvas(self):
        raise NotImplementedError

    def create_model(self):
        raise NotImplementedError
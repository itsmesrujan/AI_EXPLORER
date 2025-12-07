from models.neural_network import NeuralNetwork

class NeuralNetworkController:
    def __init__(self):
        'Controller class for Neural network'
        pass

    def get_neural_network_output(self):
        neural_network_instance = NeuralNetwork()
        return neural_network_instance.train_xor_network()
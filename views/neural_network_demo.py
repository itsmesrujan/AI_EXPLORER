from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel

class NeuralNetworkDemo(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.setLayout(layout)
        self.__label = QLabel("Click to train a neural network on XOR problem.")
        self.__button = QPushButton("Train Network")
        self.__button.clicked.connect(self.train_neural_network)
        layout.addWidget(self.__label)
        layout.addWidget(self.__button)

    def train_neural_network(self):
        from models.neural_network import NeuralNetwork
        neural_network_instance = NeuralNetwork()
        output = neural_network_instance.train_xor_network()
        self.__label.setText(f"Trained XOR Network Output:\n{output}")

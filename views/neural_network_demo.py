from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel
from utils.views.custom_push_button import CustomPushButton

class NeuralNetworkDemo(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.setLayout(layout)
        self.__label = QLabel("Click to train a neural network on XOR problem.")
        self.__button = CustomPushButton("Train Network")
        self.__button.clicked.connect(self.train_neural_network)
        layout.addWidget(self.__label)
        layout.addWidget(self.__button)

    def train_neural_network(self):
        from controllers.neural_network_controller import NeuralNetworkController
        neural_instance = NeuralNetworkController()
        self.__label.setText(f"Trained XOR Network Output:\n{neural_instance.get_neural_network_output()}")

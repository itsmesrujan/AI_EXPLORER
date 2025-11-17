from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel
import torch
import torch.nn as nn

class NeuralNetworkDemo(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.setLayout(layout)
        self.label = QLabel("Click to train a neural network on XOR problem.")
        self.button = QPushButton("Train Network")
        self.button.clicked.connect(self.train_nn)
        layout.addWidget(self.label)
        layout.addWidget(self.button)

    def train_nn(self):
        X = torch.tensor([[0,0],[0,1],[1,0],[1,1]], dtype=torch.float32)
        y = torch.tensor([[0],[1],[1],[0]], dtype=torch.float32)
        model = nn.Sequential(
            nn.Linear(2, 3),
            nn.ReLU(),
            nn.Linear(3, 1),
            nn.Sigmoid()
        )
        criterion = nn.MSELoss()
        optimizer = torch.optim.Adam(model.parameters(), lr=0.1)
        for _ in  range(2000):
            pred = model(X)
            loss = criterion(pred, y)
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()
        output = model(X).detach().numpy().round()
        self.label.setText(f"Trained XOR Network Output:\n{output}")

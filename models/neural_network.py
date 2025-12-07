import torch
import torch.nn as neural_network

class NeuralNetwork:
    def __init__(self):
        'model class for neural networks'
        pass
    
    def __get_tensor(self, data):
        return torch.tensor(data, dtype=torch.float32)

    def train_xor_network(self):
        try:
            # Simple xOR dataset
            x = self.__get_tensor([[0,0],[0,1],[1,0],[1,1]])
            y = self.__get_tensor([[0],[1],[1],[0]])
            model = neural_network.Sequential(
                neural_network.Linear(2, 3),
                neural_network.ReLU(),
                neural_network.Linear(3, 1),
                neural_network.Sigmoid()
            )
            criterion = neural_network.MSELoss()
            optimizer = torch.optim.Adam(model.parameters(), lr=0.1)
            for _ in  range(2000):
                pred = model(x)
                loss = criterion(pred, y)
                optimizer.zero_grad()
                loss.backward()
                optimizer.step()
            return model(x).detach().numpy().round()
        except Exception as e:
            print(f"Error during neural network training: {e}")
            return None
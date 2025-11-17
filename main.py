import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QHBoxLayout
from ui.sidebar import Sidebar
from modules.linear_regression_demo import LinearRegressionDemo
from modules.classification_demo import ClassificationDemo
from modules.neural_network_demo import NeuralNetworkDemo
from modules.nlp_sentiment_demo import NLPSentimentDemo
from modules.vision_edge_detection_demo import VisionEdgeDetectionDemo

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("AI Concepts Explorer")
        self.setMinimumSize(1000, 600)
        layout = QHBoxLayout()
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)
        # Sidebar
        self.sidebar = Sidebar()
        layout.addWidget(self.sidebar)
        # Default module
        self.demo_area = LinearRegressionDemo()
        layout.addWidget(self.demo_area)
        # Connect sidebar clicks
        self.sidebar.selection_changed.connect(self.load_module)

    def load_module(self, module_name):
        if module_name == "Linear Regression":
            new_widget = LinearRegressionDemo()
        elif module_name == "Classification":
            new_widget = ClassificationDemo()
        # [TODO] Enable these modules after fixing dependencies
        # elif module_name == "Neural Network":
        #     new_widget = NeuralNetworkDemo()
        # elif module_name == "NLP Sentiment":
        #     new_widget = NLPSentimentDemo()
        elif module_name == "Computer Vision Edges":
            new_widget = VisionEdgeDetectionDemo()
        else:
            return
        self.demo_area.setParent(None)
        self.demo_area = new_widget
        self.centralWidget().layout().addWidget(self.demo_area)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

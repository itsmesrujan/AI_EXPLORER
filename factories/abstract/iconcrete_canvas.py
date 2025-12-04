from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from models.common import Common

class ICanvas(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        __common_instance = Common()
        self.figure = __common_instance.get_plot_figure()
        self.canvas = FigureCanvas(self.figure)
        self.button = QPushButton("Run Demo")
        self.layout.addWidget(self.canvas)
        self.layout.addWidget(self.button)
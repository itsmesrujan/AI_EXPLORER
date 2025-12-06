from PySide6.QtWidgets import QWidget, QVBoxLayout
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from models.common import Common
from utils.views.custom_push_button import CustomPushButton

class ICanvas(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        __common_instance = Common()
        self.figure = __common_instance.get_plot_figure()
        self.canvas = FigureCanvas(self.figure)
        self.button = CustomPushButton("Run Demo")
        self.button.setStyleSheet("background-color: transparent; border: none; text-align: center; font-size: 16px; padding: 10px;")
        self.layout.addWidget(self.canvas)
        self.layout.addWidget(self.button)
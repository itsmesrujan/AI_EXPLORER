from PySide6.QtWidgets import QWidget, QVBoxLayout
from PySide6.QtCore import Signal
from utils.views.custom_push_button import CustomPushButton

class Sidebar(QWidget):
    selection_changed = Signal(str)
    def __init__(self, default_selection=None):
        super().__init__()
        layout = QVBoxLayout()
        self.setLayout(layout)
        concepts = [
            "Concepts Overview",
            "Linear Regression",
            "Classification",
            "Neural Network",
            "NLP Sentiment",
            "Computer Vision Edges",
            "K-Means Clustering",
            "Generative AI"
        ]
        for c in concepts:
            button = CustomPushButton(c)
            # [TODO] Style the buttons to be transparent background
            # button.setStyleSheet("text-background-color: transparent;")
            button.setStyleSheet("background-color: transparent; border: none; text-align: center; padding: 10px;")
            button.clicked.connect(lambda _, x=c: self.selection_changed.emit(x))
            layout.addWidget(button)
        if default_selection:
            self.selection_changed.emit(default_selection)
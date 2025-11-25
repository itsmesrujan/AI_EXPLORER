from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton
from PySide6.QtCore import Signal

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
            "K-Means Clustering"
        ]
        for c in concepts:
            button = QPushButton(c)
            button.clicked.connect(lambda _, x=c: self.selection_changed.emit(x))
            layout.addWidget(button)
        if default_selection:
            self.selection_changed.emit(default_selection)
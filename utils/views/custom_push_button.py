from PySide6.QtWidgets import QPushButton

class CustomPushButton(QPushButton):
    def __init__(self, label: str):
        super().__init__(label)
        self.setStyleSheet("background-color: transparent;\
                           border: none;\
                           text-align: center;\
                           padding: 10px;")
from PySide6.QtWidgets import QWidget, QVBoxLayout, QTextEdit, QLabel
from utils.views.custom_push_button import CustomPushButton

class NLPSentimentDemo(QWidget):
    def __init__(self):
        'View for NLP Sentiment Analysis Demo'
        super().__init__()
        layout = QVBoxLayout()
        self.setLayout(layout)
        self.__input_box = QTextEdit()
        self.__button = CustomPushButton("Analyze Sentiment")
        self.__result_label = QLabel("Sentiment score will appear here.")
        self.__button.clicked.connect(self.analyze)
        layout.addWidget(self.__input_box)
        layout.addWidget(self.__button)
        layout.addWidget(self.__result_label)

    def analyze(self):
        text = self.__input_box.toPlainText()
        from controllers.nlp_sentiment_controller import NLPSentimentController
        nlp_instance = NLPSentimentController()
        self.__result_label.setText(nlp_instance.get_scores(text))

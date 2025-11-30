from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QTextEdit, QLabel

class NLPSentimentDemo(QWidget):
    def __init__(self):
        'View for NLP Sentiment Analysis Demo'
        super().__init__()
        layout = QVBoxLayout()
        self.setLayout(layout)
        self.__input_box = QTextEdit()
        self.__button = QPushButton("Analyze Sentiment")
        self.__result_label = QLabel("Sentiment score will appear here.")
        self.__button.clicked.connect(self.analyze)
        layout.addWidget(self.__input_box)
        layout.addWidget(self.__button)
        layout.addWidget(self.__result_label)
        # Initialize NLPSentiment model instance
        from models.nlp_sentiment import NLPSentiment 
        self.__NLPSentiment_instance = NLPSentiment()

    def analyze(self):
        text = self.__input_box.toPlainText()
        self.__result_label.setText(self.__NLPSentiment_instance.get_polarity_scores(text))

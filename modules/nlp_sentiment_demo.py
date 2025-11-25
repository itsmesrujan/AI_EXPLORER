from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QTextEdit, QLabel
import ssl
from nltk.sentiment import SentimentIntensityAnalyzer
import nltk

# Ensure VADER is downloaded
try:
    nltk.data.find('sentiment/vader_lexicon')
except:
    '''
     In certain environments, SSL certificate verification may fail,
     preventing nltk from downloading resources. The following code
     creates an unverified SSL context to bypass this issue.
     But this is generally not recommended for production code due to security
     risks.
    '''
    try:
        _create_unverified_https_context = ssl._create_unverified_context
    except AttributeError:
        pass
    else:
        ssl._create_default_https_context = _create_unverified_https_context
    nltk.download('vader_lexicon')

class NLPSentimentDemo(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.setLayout(layout)
        self.input_box = QTextEdit()
        self.button = QPushButton("Analyze Sentiment")
        self.result_label = QLabel("Sentiment score will appear here.")
        self.button.clicked.connect(self.analyze)
        layout.addWidget(self.input_box)
        layout.addWidget(self.button)
        layout.addWidget(self.result_label)
        self.analyzer = SentimentIntensityAnalyzer()

    def analyze(self):
        text = self.input_box.toPlainText()
        scores = self.analyzer.polarity_scores(text)
        self.result_label.setText(str(scores))

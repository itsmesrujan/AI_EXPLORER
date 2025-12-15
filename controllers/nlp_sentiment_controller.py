from models.nlp_sentiment import NLPSentiment 

class NLPSentimentController:
    def __init__(self):
        'Controller class for NLP sentiment'
        # Initialize NLPSentiment model instance
        self.__NLPSentiment_instance = NLPSentiment()

    def get_scores(self, text):
        return self.__NLPSentiment_instance.get_sentiment_score(text)

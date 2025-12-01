import ssl
from nltk.sentiment import SentimentIntensityAnalyzer
import nltk

class NLPSentiment:
    def __init__(self):
        'model class for natural language processing sentiment analysis'
        # Ensure VADER is downloaded
        self.__download_vader()
        self.__analyzer = None
        try:
            self.__analyzer = SentimentIntensityAnalyzer()
        except Exception as e:
            print(f"Error while initializing SentimentIntensityAnalyzer: {e}")
            self.__analyzer = None

    def __download_vader(self):
        try:
            nltk.data.find('sentiment/vader_lexicon')
        except:
            '''
            In certain environments, SSL certificate verification may fail,
            preventing nltk from downloading resources. The following code
            creates an unverified SSL context to bypass this issue.
            But this is generally not recommended for production code due to security
            risks.[TODO: Find a better solution for SSL verification issues.]
            '''
            try:
                _create_unverified_https_context = ssl._create_unverified_context
            except AttributeError:
                pass
            else:
                ssl._create_default_https_context = _create_unverified_https_context
            nltk.download('vader_lexicon')

    def get_polarity_scores(self, text):
        try:
            return str(self.__analyzer.polarity_scores(text))
        except Exception as e:
            print(f"Error while getting polarity scores: {e}")
            return 'Error analyzing sentiment.'
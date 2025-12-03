from factories.model_factory import ModelFactory

from views.linear_regression_demo import LinearRegressionDemo
from views.classification_demo import ClassificationDemo
from views.neural_network_demo import NeuralNetworkDemo
from views.nlp_sentiment_demo import NLPSentimentDemo
from views.vision_edge_detection_demo import VisionEdgeDetectionDemo
from views.kmeans_demo import KMeansDemo
from views.generative_ai_demo import GenerativeAIDemo

def register_demo_models():
    ModelFactory.register_model("Linear Regression", LinearRegressionDemo)
    ModelFactory.register_model("Classification", ClassificationDemo)
    ModelFactory.register_model("Neural Network", NeuralNetworkDemo)
    ModelFactory.register_model("NLP Sentiment", NLPSentimentDemo)
    ModelFactory.register_model("Computer Vision Edges", VisionEdgeDetectionDemo)
    ModelFactory.register_model("K-Means Clustering", KMeansDemo)
    ModelFactory.register_model("Generative AI", GenerativeAIDemo)

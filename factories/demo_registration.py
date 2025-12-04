from factories.model_factory import ModelFactory
from factories.abstract.factory_classification import ClassificationFactory
from factories.abstract.factory_linear_regression import LinearRegressionFactory
from factories.abstract.factory_kmeans import KMeanFactory

from views.neural_network_demo import NeuralNetworkDemo
from views.nlp_sentiment_demo import NLPSentimentDemo
from views.vision_edge_detection_demo import VisionEdgeDetectionDemo
from views.generative_ai_demo import GenerativeAIDemo

def register_demo_models():
    ModelFactory.register_model("Linear Regression",\
                                LinearRegressionFactory().create_canvas())
    ModelFactory.register_model("Classification",\
                                ClassificationFactory().create_canvas())
    ModelFactory.register_model("K-Means Clustering",\
                                KMeanFactory().create_canvas())
    ModelFactory.register_model("Neural Network", NeuralNetworkDemo())
    ModelFactory.register_model("NLP Sentiment", NLPSentimentDemo())
    ModelFactory.register_model("Computer Vision Edges", VisionEdgeDetectionDemo())
    ModelFactory.register_model("Generative AI", GenerativeAIDemo())

from views.factories.model_factory import ModelFactory
from views.factories.abstract.classification_factory import ClassificationFactory
from views.factories.abstract.linear_regression_factory import LinearRegressionFactory
from views.factories.abstract.kmeans_factory import KMeanFactory
from views.factories.abstract.reinforcement_learning_factory import ReinforcementLearningFactory

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
    ModelFactory.register_model("Reinforcement Learning",\
                                ReinforcementLearningFactory().create_canvas())
    ModelFactory.register_model("Neural Network", NeuralNetworkDemo())
    ModelFactory.register_model("NLP Sentiment", NLPSentimentDemo())
    ModelFactory.register_model("Computer Vision Edges", VisionEdgeDetectionDemo())
    ModelFactory.register_model("Generative AI", GenerativeAIDemo())

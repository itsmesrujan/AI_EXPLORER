# [TODO] Enable these fixtures after updating UI tests to match recent code
# changes

# import pytest
# from PySide6.QtWidgets import QWidget

# @pytest.fixture(scope="module", autouse=True)
# def setup_environment():
#     # Setup code before any tests run
#     print("\nSetting up test environment...")
#     yield
#     # Teardown code after all tests run
#     print("\nTearing down test environment...")

# @pytest.fixture
# def classification_demo():
#     from views.classification_demo import ClassificationDemo
#     return ClassificationDemo(QWidget)

# @pytest.fixture
# def kmeans_demo():
#     from views.kmeans_demo import KMeansDemo
#     return KMeansDemo(QWidget)

# @pytest.fixture
# def linear_regression_demo():
#     from views.linear_regression_demo import LinearRegressionDemo
#     return LinearRegressionDemo(QWidget)

# @pytest.fixture
# def neural_network_demo():
#     from views.neural_network_demo import NeuralNetworkDemo
#     return NeuralNetworkDemo(QWidget)

# @pytest.fixture
# def nlp_sentiment_demo():
#     from views.nlp_sentiment_demo import NLPSentimentDemo
#     return NLPSentimentDemo(QWidget)

# @pytest.fixture
# def vision_edge_detection_demo():
#     from views.vision_edge_detection_demo import VisionEdgeDetectionDemo
#     return VisionEdgeDetectionDemo(QWidget)

# @pytest.fixture
# def generative_ai_ui():
#     from views.generative_ai.generative_ai_demo import GenerativeAIPage
#     return GenerativeAIPage()
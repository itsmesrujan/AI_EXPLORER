from models.vision_edge_detection import VisionEdgeDetection

class VisionEdgeDetectionController:
    def __init__(self):
        'Controller class for vision edge detection'
        self.__visionEdgeDetection_instance = VisionEdgeDetection()

    def get_image(self, path):
        return self.__visionEdgeDetection_instance.get_image_data(path)

    def get_edges(self):
        return self.__visionEdgeDetection_instance.get_edges_data()
from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QFileDialog
from PySide6.QtGui import QPixmap, QImage
from controllers.vision_edge_detection_controller import VisionEdgeDetectionController
from utils.views.custom_push_button import CustomPushButton

class VisionEdgeDetectionDemo(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.setLayout(layout)
        self.__button_load = CustomPushButton("Load Image")
        self.__button_detect = CustomPushButton("Detect Edges")
        self.__label_original = QLabel("Original Image")
        self.__label_edges = QLabel("Edges will appear here")
        self.__button_load.clicked.connect(self.load_image)
        self.__button_detect.clicked.connect(self.detect_edges)
        layout.addWidget(self.__button_load)
        layout.addWidget(self.__button_detect)
        layout.addWidget(self.__label_original)
        layout.addWidget(self.__label_edges)
        self.__visionEdgeInstance = VisionEdgeDetectionController()

    def load_image(self):
        path, _ = QFileDialog.getOpenFileName(self, "Choose an image")
        if not path:
            return
        height, width, rgbData = self.__visionEdgeInstance.get_image(path)
        if height == width == rgbData == None:
            return
        qimg = QImage(rgbData, width, height, 3*width, QImage.Format_RGB888)
        self.__label_original.setPixmap(QPixmap.fromImage(qimg).scaled(300, 300))

    def detect_edges(self):
        height, width, edgesData = self.__visionEdgeInstance.get_edges()
        if height == width == edgesData == None:
            return
        qimg = QImage(edgesData, width, height, width, QImage.Format_Grayscale8)
        self.__label_edges.setPixmap(QPixmap.fromImage(qimg).scaled(300, 300))

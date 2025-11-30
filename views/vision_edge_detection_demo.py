from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel, QFileDialog
from PySide6.QtGui import QPixmap, QImage
from models.vision_edge_detection import VisionEdgeDetection

class VisionEdgeDetectionDemo(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.setLayout(layout)
        self.__button_load = QPushButton("Load Image")
        self.__button_detect = QPushButton("Detect Edges")
        self.__label_original = QLabel("Original Image")
        self.__label_edges = QLabel("Edges will appear here")
        self.__button_load.clicked.connect(self.load_image)
        self.__button_detect.clicked.connect(self.detect_edges)
        layout.addWidget(self.__button_load)
        layout.addWidget(self.__button_detect)
        layout.addWidget(self.__label_original)
        layout.addWidget(self.__label_edges)
        self.__visionEdgeDetection_instance = VisionEdgeDetection()

    def load_image(self):
        path, _ = QFileDialog.getOpenFileName(self, "Choose an image")
        if not path:
            return
        height, width, rgbData = self.__visionEdgeDetection_instance.get_image_data(path)
        if height == width == rgbData == None:
            return
        qimg = QImage(rgbData, width, height, 3*width, QImage.Format_RGB888)
        self.__label_original.setPixmap(QPixmap.fromImage(qimg).scaled(300, 300))

    def detect_edges(self):
        height, width, edgesData = self.__visionEdgeDetection_instance.get_edges_data()
        if height == width == edgesData == None:
            return
        qimg = QImage(edgesData, width, height, width, QImage.Format_Grayscale8)
        self.__label_edges.setPixmap(QPixmap.fromImage(qimg).scaled(300, 300))

from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel, QFileDialog
from PySide6.QtGui import QPixmap, QImage
import cv2 as cv

class VisionEdgeDetectionDemo(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.setLayout(layout)
        self.button_load = QPushButton("Load Image")
        self.button_detect = QPushButton("Detect Edges")
        self.label_original = QLabel("Original Image")
        self.label_edges = QLabel("Edges will appear here")
        self.button_load.clicked.connect(self.load_image)
        self.button_detect.clicked.connect(self.detect_edges)
        layout.addWidget(self.button_load)
        layout.addWidget(self.button_detect)
        layout.addWidget(self.label_original)
        layout.addWidget(self.label_edges)
        self.img = None
        self.edges = None

    def load_image(self):
        path, _ = QFileDialog.getOpenFileName(self, "Choose an image")
        if not path:
            return
        self.img = cv.imread(path)
        rgb = cv.cvtColor(self.img, cv.COLOR_BGR2RGB)
        h, w, ch = rgb.shape
        qimg = QImage(rgb.data, w, h, 3*w, QImage.Format_RGB888)
        self.label_original.setPixmap(QPixmap.fromImage(qimg).scaled(300, 300))

    def detect_edges(self):
        if self.img is None:
            return
        self.edges = cv.Canny(self.img, 100, 200)
        h, w = self.edges.shape
        qimg = QImage(self.edges.data, w, h, w, QImage.Format_Grayscale8)
        self.label_edges.setPixmap(QPixmap.fromImage(qimg).scaled(300, 300))

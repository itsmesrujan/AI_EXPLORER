import cv2 as cv

class VisionEdgeDetection:
    def __init__(self):
        'model class for vision edge detection'
        self._image = None
        self._edges = None

    def get_image_data(self, imagePath):
        try:
            self._image = cv.imread(imagePath)
            rgb = cv.cvtColor(self._image, cv.COLOR_BGR2RGB)
            height, width, ch = rgb.shape
            return height, width, rgb.data
        except Exception as e:
            print(f"Error while getting the image data: {e}")
            return None,None,None

    def get_edges_data(self):
        try:
            if self._image is None:
                raise "Image data missing!"
            self._edges = cv.Canny(self._image, 100, 200)
            height, width = self._edges.shape
            return height, width, self._edges.data
        except Exception as e:
            print(f"Error while getting the edges data: {e}")
            return None,None,None
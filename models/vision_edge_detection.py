import cv2 as cv

class VisionEdgeDetection:
    def __init__(self):
        'model class for vision edge detection'
        self.__image = None
        self.__edges = None

    def get_image_data(self, imagePath):
        try:
            self.__image = cv.imread(imagePath)
            rgb = cv.cvtColor(self.__image, cv.COLOR_BGR2RGB)
            height, width, ch = rgb.shape
            return height, width, rgb.data
        except Exception as e:
            print(f"Error while getting the image data: {e}")
            return None,None,None

    def get_edges_data(self):
        try:
            if self.__image is None:
                raise "Image data missing!"
            self.__edges = cv.Canny(self.__image, 100, 200)
            height, width = self.__edges.shape
            return height, width, self.__edges.data
        except Exception as e:
            print(f"Error while getting the edges data: {e}")
            return None,None,None
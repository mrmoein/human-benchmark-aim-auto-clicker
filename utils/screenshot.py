from PIL import ImageGrab
from PIL.Image import Image

from utils.point import Point


class ScreenShot:
    def __init__(self, image_name: str):
        self.__image_name = image_name

    def take(self, point1: Point, point2: Point) -> Image:
        ss_img = ImageGrab.grab((point1.x, point1.y, point2.x, point2.y))
        # ss_img.save(self.__image_name)
        return ss_img

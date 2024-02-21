import time

from pynput.mouse import Button, Controller

from config import *
from utils.find_first_white_pixel import find_first_white_pixel
from utils.screenshot import ScreenShot

mouse = Controller()

time.sleep(3)

screenshot = ScreenShot(screenshot_name)
t0 = time.time()

mx, my = mouse.position

image = screenshot.take(screenshot_point1, screenshot_point2)
white_pixel_point = find_first_white_pixel(image)
mouse.move((image.width/2 + screenshot_point1.x) - mx,
                   (image.height/2 + screenshot_point1.y) - my)
mouse.click(Button.left)

for i in range(120):
    image = screenshot.take(screenshot_point1, screenshot_point2)
    white_pixel_point = find_first_white_pixel(image)
    if white_pixel_point is not None:
        mx, my = mouse.position
        mouse.move((white_pixel_point[0] + screenshot_point1.x) - mx,
                   (white_pixel_point[1] + screenshot_point1.y) - my)
        mouse.click(Button.left)
    # time.sleep(0.001)

t1 = time.time()

print(t1 - t0)

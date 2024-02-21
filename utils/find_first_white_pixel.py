from PIL.Image import Image


def find_first_white_pixel(image: Image):
    width, height = image.size
    pixels = image.getdata()

    for y in range(0, height, 4):
        for x in range(0, width, 4):
            pixel = pixels[y * width + x]
            if sum(pixel) > 700:
                return x, y
    return None

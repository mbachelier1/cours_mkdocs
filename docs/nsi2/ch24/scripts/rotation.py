

from PIL import Image
import numpy as np

step = 0


def rotation_image_2(img, x=None, y=None, t=None):
    if x is None:
        x, y = 0, 0
        t = image.size[0]
        img = img.copy()
    if t > step:
        t //= 2
        pixels = img.load()
        for i in range(x, x + t):
            for j in range(y, y + t):
                pixels[i, j], pixels[i, j + t], pixels[i + t, j + t], pixels[i + t, j] = pixels[i + t, j], pixels[i, j], \
                                                                                         pixels[i, j + t], pixels[
                                                                                             i + t, j + t]
        rotation_image_2(img, x, y, t)
        rotation_image_2(img, x + t, y, t)
        rotation_image_2(img, x, y + t, t)
        rotation_image_2(img, x + t, y + t, t)
    return img


def produce_gif(img):
    global step

    result = []
    step = img.size[0]

    while step > 1:
        result.append(rotation_image_2(img))
        step //= 2
    result[0].save('result.gif', save_all=True, append_images=result[1:], optimize=True, duration=1000, loop=0)


def rotation_image(img, x=None, y=None, t=None):
    if x is None:
        x, y = 0, 0
        t = image.size[0]
    if t > 1:
        t //= 2
        pixels = img.load()
        for i in range(x, x + t):
            for j in range(y, y + t):
                pixels[i, j], pixels[i, j + t], pixels[i + t, j + t], pixels[i + t, j] = pixels[i + t, j], pixels[i, j], \
                                                                                         pixels[i, j + t], pixels[
                                                                                             i + t, j + t]
        rotation_image(img, x, y, t)
        rotation_image(img, x + t, y, t)
        rotation_image(img, x, y + t, t)
        rotation_image(img, x + t, y + t, t)


image = Image.open('../img/fred.png')
produce_gif(image)
image.show()

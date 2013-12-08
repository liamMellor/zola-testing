from collections import namedtuple
from math import sqrt
import random
from PIL import Image

def get_main_color(most_present):
    img = Image.open("special.jpg")
    colors = img.getcolors(256) #put a higher value if there are many colors in your image
    max_occurence, most_present = 0, 0
    try:
        for c in colors:
            if c[0] > max_occurence:
                (max_occurence, most_present) = c
        return most_present
    except TypeError:
        raise Exception("Too many colors in the image")

print get_main_color
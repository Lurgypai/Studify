#!/bin/python3

from PIL import Image,ImageColor,ImageEnhance

import getpieces
import sys
import json

# https://stackoverflow.com/questions/19914509/python-pil-pixel-rgb-color-to-hex
def rgb2hex(r, g, b):
    return '{:02x}{:02x}{:02x}'.format(r, g, b)

def studify(img, palette_file, pieces):
    palette = Image.open(palette_file)

    target_image = Image.open(img)
    enhancer = ImageEnhance.Contrast(target_image)
    # target_image = enhancer.enhance(10)

    target_image = target_image.quantize(palette=palette, dither=Image.Dither.NONE)
    target_image = target_image.convert('RGB')
    target_image.save('output.png')

    colors = target_image.getcolors()
    colors.sort()

    for color in colors:
        r, g, b = color[1]
        heks = rgb2hex(r, g, b).upper()
        piece = list(filter(lambda piece: piece[0] == heks, pieces))[0]
        print('Piece: ' + piece[1] + ', Count: ' + str(color[0]))
        
if __name__ == '__main__':
    studify(sys.argv[1], sys.argv[2], getpieces.getpieces())


#!/bin/python3

from PIL import Image,ImageColor

import getpieces
import sys
import json
import colorsys

# https://stackoverflow.com/questions/19914509/python-pil-pixel-rgb-color-to-hex
def rgb2hex(r, g, b):
    return '{:02x}{:02x}{:02x}'.format(r, g, b)

def remove_under_threshold(pieces, threshold):
    print('Threshold for piece viability', threshold)
    return list(filter(lambda piece: piece[2] > threshold, pieces))
    
def save_palette(pieces, name):
    palette = Image.new('RGB', (len(pieces), 1))

    xpos = 0
    for piece in pieces:
        palette.putpixel((xpos, 0), ImageColor.getrgb('#' + piece[0]))
        xpos += 1

    palette = palette.convert('P', palette=Image.Palette.ADAPTIVE)
    palette.save(name)

def make_basic_palette(pieces):
    trans_removed = list(filter(lambda piece: "Trans" not in piece[1], pieces))
    silver_pearl_removed = list(filter(lambda piece: ("Silver" not in piece[1] and "Pearl" not in piece[1]), trans_removed))
    print('Basic pieces:')
    for piece in silver_pearl_removed:
        print('\t' + str(piece))
    save_palette(silver_pearl_removed, 'basic.png')

def make_shiny_palette(pieces):
    only_shiny = list(filter(lambda piece: ("Silver" in piece[1] or "Pearl" in piece[1] or piece[1] == "Black"), pieces))
    print('Shiny pieces:')
    for piece in only_shiny:
        print('\t' + str(piece))
    save_palette(only_shiny, 'shiny.png')

def make_trans_palette(pieces):
    only_trans = list(filter(lambda piece: "Trans" in piece[1], pieces))
    print('Trans pieces:')
    for piece in only_trans:
        print('\t' + str(piece))
    save_palette(only_trans, 'trans.png')

if __name__ == '__main__':
    pieces = getpieces.getpieces()
    pieces = remove_under_threshold(pieces, int(sys.argv[1]))
    make_basic_palette(pieces)
    make_shiny_palette(pieces)
    make_trans_palette(pieces)

    print('THE GENERATED PALETTES USE BROKEN INDEXED COLORS (BLACK IS ADDED) BE SURE TO REMOVE THIS BEFORE USAGE')


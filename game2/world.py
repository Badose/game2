import csv
import pygame as pg
from settings import *

class Map: 
    def __init__(self, csv_path, image_path, space=0):
        date_list = self._csv_to_list(csv_path)
        image_list = self._pars_image(image_path, space)
        
    def _csv_to_list(self, csv_path):
        with open(csv_path) as f:
            reader = csv.reader(f)
            data = list(reader)
        return data
    
    def _pars_image(self, image_path, space):
        image_list = []
        image = pg.image.load(image_path).convert()
        width, height = image.get_size
        for y in range(0, height, TILE_SIZE + space):
            for x in range(0, width, TILE_SIZE + space):
                tile = image.subsurface(x, y, TILE_SIZE, TILE_SIZE)
                image_list.append(tile)
        return image_list
        
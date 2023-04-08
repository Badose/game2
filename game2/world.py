import csv
import pygame as pg
from settings import *

class Map: 
    def __init__(self, game, csv_path, image_path, img_tile_size, space=0):
        data_list = self._csv_to_list(csv_path)
        image_list = self._pars_image(image_path, img_tile_size, space)
        self._load_tiles(game, data_list, image_list)
        self.width = len(data_list[0]) * TILE_SIZE 
        self.height = len(data_list) * TILE_SIZE 

        
    def _csv_to_list(self, csv_path):
        with open(csv_path) as f:
            reader = csv.reader(f)
            data = list(reader)
        return data
    
    def _pars_image(self, image_path, img_tile_size, space):
        image_list = []
        image = pg.image.load(image_path).convert()

        if img_tile_size != TILE_SIZE:
            scale = TILE_SIZE // img_tile_size
            space *= scale
            current_size = image.get_size()
            target_size = tuple(i * scale for i in current_size)
            image = pg.transform.scale(image, target_size)

        width, height = image.get_size()
        for y in range(0, height, TILE_SIZE + space):
            for x in range(0, width, TILE_SIZE + space):
                tile = image.subsurface(x, y, TILE_SIZE, TILE_SIZE)
                image_list.append(tile)
        return image_list
   
   
    def _load_tiles(self, game, data_list, image_list):
        for i, row in enumerate(data_list):
            for j, ind in enumerate(row):
                Tile(game, i, j, image_list[int(ind)])
    

class Tile(pg.sprite.Sprite):
    def __init__(self, game, x, y, image):
        self._layer = GROUND_LAY
        super().__init__(game.all_sprites) 
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x * TILE_SIZE
        self.rect.y = y * TILE_SIZE

class Camera:
    def __init__(self, map_width, map_height):
        self.offset = (0, 0)
        self.map_width = map_width
        self.map_height = map_height



    def aply(self, entity):
        return entity.rect.move(self.offset)
    

    def update(self, target):
        x = -target.rect.x + WIDTH//2
        y =  -target.rect.y + HEIGHT//2
        x = min(x, 0) #левая граница
        y = min(y, 0) #верхняя граница
        x = max(x, -self.map_width + WIDTH)
        y = max(y, -self.map_height + HEIGHT)
        self.offset = (x, y)

    
import csv
import pygame as pg
from settings import *

class Map: 
    
    WALL_LIST = [1, 2, 3, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16,
                18, 19, 20, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33,
                35, 36, 37, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50,
                52, 53, 54, 58, 59, 60, 61, 52, 53, 54, 65, 66, 67,
                69, 70, 75, 76, 77, 78, 79, 81, 82, 83, 84,
                92, 93, 94, 95, 96, 97, 98, 99, 100, 101,
                107, 108, 109, 110, 11, 112, 113, 114, 115, 116, 227, 118,
                119, 120, 121, 122, 123, 124, 125, 130, 131, 132, 133, 134, 135]

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
                collidable = int(ind) in Map.WALL_LIST
                Tile(game, j, i, image_list[int(ind)], collidable)
    

class Tile(pg.sprite.Sprite):
    def __init__(self, game, x, y, image, is_wall=False):
        self._layer = GROUND_LAY
        if is_wall:
            groups = game.all_sprites, game.walls
        else:
            groups = game.all_sprites
        super().__init__(groups) 
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x * TILE_SIZE
        self.rect.y = y * TILE_SIZE
        

class Camera:
    '''Конструктор камеры.'''
    def __init__(self, map_width, map_height):
        self.offset = (0, 0)
        self.map_width = map_width
        self.map_height = map_height



    def aply(self, entity):
        '''Движение камеры.'''
        return entity.rect.move(self.offset)
    

    def update(self, target):
        '''Координаты камеры.'''
        x = -target.rect.x + WIDTH//2
        y =  -target.rect.y + HEIGHT//2
        x = min(x, 0) #левая граница
        y = min(y, 0) #верхняя граница
        x = max(x, -self.map_width + WIDTH)
        y = max(y, -self.map_height + HEIGHT)
        self.offset = (x, y)

    
import csv
import pygame as pg
from settings import *

class Map: 
    def __init__(self, csv_path, image_path, space=0):
        date_list = self._csv_to_list(csv_path)
    
    def csv_to_list(self, csv_path):
        with open(csv_path) as f:
            reader = csv.reader(f)
            data = list(reader)
        return data
        
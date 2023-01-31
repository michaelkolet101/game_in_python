import pygame
from Characters.colors import Colors
import random

color = Colors()


class Tree:
    def __init__(self, x, y):
        self._x = x
        self._y = y
        self._img_location = r"C:\Users\micha\Desktop\game_in_python\IMAGES\tree.jpg" 
        self._img = self.load_img()


    def move_tree(self):
        self._x -= 10
        if self._x == -100:
            self._x = 500
          

    def get_img(self):
        return self._img

    def get_lication(self):
        return [self._x, self._y]

    def load_img(self):
        img = pygame.image.load(self._img_location)
        img.set_colorkey((255, 255, 255))
        img = pygame.transform.scale(img, (150, 300))
        return img
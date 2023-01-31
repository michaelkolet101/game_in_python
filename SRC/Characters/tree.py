import pygame
from SRC.Characters.colors import Colors

color = Colors()

class Tree:
    def __init__(self, x, y):
        self._x = x
        self._y = y
        self._img = pygame.image.load(r"C:\Users\micha\Desktop\my_first_game\IMAGES\tree.jpg")
        self._img.set_colorkey(color.WHITE)
        self._img = pygame.transform.scale(self._img, (150, 300))


    def move_tree(self):
        self._x -= 10
        if self._x == -100:
            self._x = 500

    def get_img(self):
        return self._img

    def get_lication(self):
        return [self._x, self._y]
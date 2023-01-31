import pygame


class Bg:

    def __init__(self, width, hight):
        self._width = width
        self._hight = hight
        self._poto = pygame.image.load(r"C:\Users\micha\Desktop\game_in_python\IMAGES\bg_1.jpg")

    def screen_size(self):
        screen = pygame.display.set_mode([self._width, self._hight])
        return screen

    def get_img(self):
        return self._poto

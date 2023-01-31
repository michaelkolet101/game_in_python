import pygame


class Hero:

    def __init__(self, x, y):
        self._x = x
        self._y = y
        self._poto = r"C:\Users\micha\Desktop\game_in_python\IMAGES\bird.png"


    def jump(self):
        self._y -= 10
        

    def down(self):
        self._y += 10

    def get_location(self):
        return [self._x, self._y]

    def get_img(self):
        return self._poto

    def player(self):
        
        player_img = pygame.image.load(self.get_img()).convert()
        player_img.set_colorkey((0, 0 ,0))
        player_img = pygame.transform.scale(player_img, (100, 100))

        return player_img


    def set_position(self, x, y):
        self._y = y
        self._x = x
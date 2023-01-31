import pygame

from Characters.back_graund import Bg

from Characters.hero import Hero
from Characters.tree import Tree

# הוספת שעון עצר לפקודות
clock = pygame.time.Clock()
REFRESH_RATE = 100

# back ground
bg = Bg(500, 500)

hero = Hero(20, 350)
tree = Tree(500, 200)

pygame.init()

screen = bg.screen_size()
pygame.display.set_caption("my first game")

# כך שמים תמונת רקע
img = bg.get_img().convert()

# נוסיף עכשיו את הדמות שלנו

finish = False

while finish != True:

    screen.blit(img, (0, 0))

    screen.blit(hero.player(), hero.get_location())
    screen.blit(tree.get_img(), tree.get_lication())

    hero.set_position(20, 350)
    tree.move_tree()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finish = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                hero.down()

            if event.key == pygame.K_UP:
                hero.jump()

    pygame.display.update()
    clock.tick(10)

import pygame as py
import random as r  # this is to enable the y parameter of the winning square's position to be randomised
from Play import level

"""
Creating globals
"""

width = 700
height = 500
screen = py.display.set_mode((700, 500))
level_ = level  # to distinguish between the preset level and manipulated level
pressed_keys = py.key.get_pressed()
Black = (0, 0, 0)
n = 0  # place holder for the text produced


"""
Producing the winning square
"""


class WinSquare(py.sprite.Sprite):
    global level_, width, height

    def __init__(self):
        super().__init__()
        self.surf = py.Surface((20, 100))
        self.rect = self.surf.get_rect()
        self.rect.x = width-20
        self.rect.y = r.randint(150, 250)

    def coll(self, player, level):  # Collide function
        if self.rect.colliderect(player):
            font = py.font.SysFont(n, 76)
            img = font.render('You Win!!', True, Black)
            text = img.get_rect(center=(width / 2, height/2))
            screen.blit(img, text)
            font_1 = py.font.SysFont(n, 36)
            img_1 = font_1.render('Press number "1" key to go to level ' + str(level_+1), True, (255, 0, 0))
            text_1 = img_1.get_rect(center=((width/2), (height/2) + 100))
            screen.blit(img_1, text_1)

    def movement(self):  # movement to either side
        if self.rect.x is (width-20) and 150 > self.rect.y:
            self.rect.y += 1
        elif self.rect.x is (width-20) and 250 < self.rect.y:
            self.rect.y -= 1
        else:
            pass
        return self.rect.y

    def draw(self, surface):  # Drawing the winsquare to the screen 
        surface.blit(self.surf, self.rect)

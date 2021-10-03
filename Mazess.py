import pygame as py
import random as r
from Question_screen import level

"""
Creating globals
"""

width = 700
height = 500
screen = py.display.set_mode((700, 500))
Black = (0, 0, 0)
n = None
collide_test = True  # test for the loop in the player module - to detect whether or not collision has occurred, and to lock the players movement if

# print(level)  # testing whether or not the level is recieved


class Maze(py.sprite.Sprite):
    global height, width, Black, n

    def __init__(self):
        super().__init__()
        self.surf = py.Surface((10, 35))
        # rectangle for walls
        self.rectangle = self.surf.get_rect()
        self.img = py.image.load('opps.png')  # maze sprite
        self.resize_sprite = py.transform.scale(self.img, (20, 50))

        if level == 2 or level == 3:  # constructing where the mazes can operate for each level
            self.rectangle.x = r.randint(50, width - 50)
            self.rectangle.y = r.randint(50, height - 50)

        elif level > 10:
            self.rectangle.x = r.randint(50, width -50)
            self.rectangle.y = r.randint(0, height-50)

        else:
            self.rectangle.x = r.randint(100, width - 100)
            self.rectangle.y = r.randint(100, 350)

    def coll(self, player):  # collision mechanic
        if self.rectangle.colliderect(player):
            font = py.font.SysFont(n, 76)
            img = font.render('You died', True, Black)
            text = img.get_rect(center=(width/2, height/2))
            screen.blit(img, text)
            font_1 = py.font.SysFont(n, 36)
            img_1 = font_1.render('Press space key to reset', True, (255, 0, 0))
            text_1 = img_1.get_rect(center=((width/2), (height/2) + 100))
            screen.blit(img_1, text_1)
            collide_test = False
            return collide_test

    def draw(self, surface):
        surface.blit(self.resize_sprite, self.rectangle)


"""
Creating basic columns on the side
"""


class Columns(py.sprite.Sprite):
    global width, height, Black, n

    def __init__(self):
        super().__init__()
        self.surf = py.Surface((width - 100, height // 2 - 150))
        redone_width = width - 100
        redone_height = height // 2 - 150
        self.img = py.image.load('pixil_columns.png')
        self.resize_sprite = py.transform.scale(self.img, (redone_width, redone_height))
        self.rectangle = self.surf.get_rect()

    def coll(self, player):
        if self.rectangle.colliderect(player):
            player.kill()
            font = py.font.SysFont(n, 76)
            img = font.render('You died', True, Black)
            text = img.get_rect(center=(width/2, height/2))
            screen.blit(img, text)
            font_1 = py.font.SysFont(n, 36)
            img_1 = font_1.render('Press space key to reset', True, (255, 0, 0))
            text_1 = img_1.get_rect(center=((width/2), (height/2) + 100))
            screen.blit(img_1, text_1)
            collide_test = False
            return collide_test

    def draw(self, surface):
        surface.blit(self.resize_sprite, self.rectangle)

    def position(self, one, two):
        if one is True and two is False:
            self.rectangle.x = 100
            self.rectangle.y = 0
        elif one is False and two is True:
            self.rectangle.x = 100
            self.rectangle.bottom = 500

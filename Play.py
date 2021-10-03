import pygame as py
from pygame.display import update
from pygame.locals import *
from Question_screen import level
import random as r
from Mazess import collide_test

"""
Creating globals
"""

width = 700
height = 500
screen = py.display.set_mode((700, 500))
pressed_keys = py.key.get_pressed()
# print(level)  # unit test to test whether or not the level is recieved
running_test = False

""" 
Creating player class 
"""


class Player(py.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.standing_sprite = py.image.load('pixil_player.png')
        self.surf = py.Surface((40, 40))
        self.resize_sprite = py.transform.scale(self.standing_sprite, (40, 40))
        self.forward_sprite = py.image.load('pixil_player_forward.png')
        self.other_forward_sprite = py.image.load('pixil_other_forward.png')
        self.backward_sprite = py.image.load('pixil_player_backward.png')
        self.other_backward_sprite = py.image.load('pixil_other_backward.png')
        self.rect = self.surf.get_rect()
        self.player_x = self.rect.x
        self.player_y = self.rect.y
        global level
        self.level = level

    def update(self):
        global width, height, level, running_test
        pressed_keys = py.key.get_pressed()

        def forward():  # forward running character
            random_integer = r.randint(0,1)
            if random_integer == 0:
                self.resize_sprite = py.transform.scale(self.forward_sprite, (40, 40))
            elif random_integer == 1:
                self.resize_sprite = py.transform.scale(self.other_forward_sprite, (40, 40))
            return self.resize_sprite

        def backward():  # backward running character
            random_integer = r.randint(0,1)
            if random_integer == 0:
                self.resize_sprite = py.transform.scale(self.backward_sprite, (40, 40))
            elif random_integer == 1:
                self.resize_sprite = py.transform.scale(self.other_backward_sprite, (40, 40))
            return self.resize_sprite

        global collide_test
        # while collide_test is True:
        if self.rect.left > 0 and pressed_keys[K_LEFT]:  # character movement left
            self.rect.move_ip(-1, 0)
            backward()

        if self.rect.right < width and pressed_keys[K_RIGHT]:  # character movement right
            self.rect.move_ip(1, 0)
            forward()

        if self.rect.bottom > 50 and pressed_keys[K_UP]:  # character movement upwards
            self.rect.move_ip(0, -1)
            forward()

        if self.rect.top < (height-50) and pressed_keys[K_DOWN]:  # character movement down
            self.rect.move_ip(0, 1)
            forward()

        if self.rect.top < (height - 50) and self.rect.bottom < 550 and pressed_keys[K_SPACE]:  # going to beginning
            self.rect.x, self.player_x = 0, 0
            self.rect.y, self.player_y = 0, 0

        # if pressed_keys[K_1]:  # increase level
        #     level += 1
        # return level

        if pressed_keys[K_1]:
            running_test = True
            # print(running_test) # test to see whether or not function is called
        return running_test

    def draw(self, surface):
        surface.blit(self.resize_sprite, self.rect)

    def onscreen_level(self):
        n = None
        text_colour = (0, 230, 230)
        bottom_left = (30, 485)
        font = py.font.SysFont(n, 20)
        img = font.render('Level: {}'.format(level), True, text_colour)
        text = img.get_rect(center=(bottom_left))
        screen.blit(img, text)

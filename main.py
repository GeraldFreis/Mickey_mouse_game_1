import pygame as py
from Mazess import Maze, Columns
from win import WinSquare
from Play import Player, level
from Question_screen import Window, Database, name


"""
Creating globals
"""


width = 700
height = 500
screen = py.display.set_mode((700, 500))
pressed_keys = py.key.get_pressed()
player_1 = Player()

other = list()  # list to store the appended mazes which are produced by the iteration beneath

for i in range(0, level):  # iteration of levels to produce multiple mazes, which is equal to the amount of levels
    i = Maze()
    other.append(i) 
    
# print(other)  # test to see whether or not the mazes are being created

win_block = WinSquare()  # win_square

column_1 = Columns()  # columns on either side of the screen for initial rounds
column_2 = Columns()

win = Window()  # tkinter input windows


"""
Initialising the screen and adding the closing loop
"""


py.init()
py.display.set_mode((width, height))


# background = py.image.load("pixil background.png")

finish = False  # testing value to close the loop
running_test = False  # condition to be changed, and updated when the player wishes to increase the level

while running_test == False:
    from Play import running_test # allows level to be updated, must be within loop, otherwise it will not continually check the condition
    for event in py.event.get():  # creating a finish function to close the window
        if event.type == py.QUIT:
            print("*" * 40 + '\n' + "Game Terminated" + '\n' + '*' * 40)
            running_test = True

    # finish = False
    screen.fill("White")  # when images move they leave a trace - this is to ensure that this does not occur
    player_1.onscreen_level()
    player_1.update()  # to update player movement
    player_1.draw(screen)

    if level == 2 or level == 3 or level > 10:  # reading input and returning the level
        for obj in other:
            obj.draw(screen)
            obj.coll(player_1)

    else:  # all other levels
        column_1.position(True, False)
        column_1.draw(screen)
        column_1.coll(player_1)
        column_2.position(False, True)
        column_2.coll(player_1)
        column_2.draw(screen)
        for obj in other:
            obj.draw(screen)
            obj.coll(player_1)

    win_block.movement()  # movement of the winning square
    win_block.draw(screen)
    win_block.coll(player_1, level)
    py.display.update()

database = Database()  # simply initialised to enable the increasing level function run
database.increasing_level_for_player_if_returned(name)

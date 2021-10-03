# Mickey_mouse_game_1
Game with mickey mouse - But just weird and with an AI

This program is split into multiple components, being an attempt at overoptimising everything - whilst also overengineering everything.
The program begins with a tkinter input screen, soon becoming a screen when values are inputed into the fields
This returns a level value and name to a database file, which then records this information, either welcoming the character back or introducing them.
The level is the number of mazes which are randomly constructed, but only 75 units away from the walls and columns
Columns are automatically constructed
The final point, which the user must reach is randomised between the two columns


This program includes elements of sqlite3, tkinter, pygame, pandas, randint and the pytz modules


What occurs between the modules:
* Main file uses global variables and imports data and variables from other modules
---> Uses the programmed classes and produces screen and writes everything to the screen
* Play file is the player class file, including its size, update function and movement
* Mazess file constructs both the mazes and the columns, including their colliding function and their rendering abilities
* db file is the file for the database, including writing to the database and retrieving values from the database
* tkinterinput file constructs and enables recording of the information from the initial input fields
* win file constructs the winsquare enabling it to be of a randomized position and for a collision to produce the effect it does


Notes:
* The idea to imbed the collision function into the mazes, columns and winsquare was a decision made to avoid
--> producing a loop of data, as the player module would have needed to link and access each of the other files


Things that must be done:
* Make everything look better
* Add function to increase level rather than having to restart
* Make database caching easier, and integrate a grasping tool into the db file
* Implement spacing between the mazes
* Increase screen size
* Slow character and make an animation for the character
---> Use 3D paint

Things that must be done in every file:
* re_tkinterinput:
--> Redo inputs and make it cleaner x
---> Possibly use a different background, make the text cleaner / introduce text welcoming x
---> Make the buttons able to move / vibrating on the spot
* Play:
--> Make player movement slower x
---> Add animation for the player's movement (x):
------> Potentially redo the player's movement as a whole x
---> Add functionality to increase the player's current level
----> Add function to change level backwards as well
--> To kill player movement upon collision:
***** Objects when detecting collision can change a variable which will be boolean
------> this variable is used as a statement in the player module to allow the player to move, other than to redo, once redo is completed, the character returns the boolean function that was changed by the collision model (not work)
---> Move collision methods of the other objects into this file - to make it universal
* DB:
--> Rename and refactor, because rn it is kinda shit x
---> Enable accessing of previous names x
----> Change format to a xlsx as it is viewable whereas sqlite3 is not (not going to do)
-----> Abstract
------> Find out how to iterate through the rows of a file: (uneeded)
***** Perhaps it didn't work with a db file because it does not have finite rows: excel may be better for this x
---> Work with Pandas to get the code to iterate through multiple rows, by creating a dataframe x
* Mazess:
--> Produce function to distance the mazess from one another by calling it inside of the production loop in the main frame
---> Completely kill character on contact with the maze:
----> This may be done through a function in the character to stop updating:
*** May present itself as a procedure rather than a function (try... if not...)
**** Or this may be done through a while loop, and if the character collides with an object
----> Clean up the images for the walls and choose a nicer colour for the mazes: something that does not look to apprehensive x
* Main:
----> Make everything clearer, (refactor) x
----> Add a timer to make the updates to the game slower  x
-----> Find a way to reduce the ram usage x
* Win:
----> Make the win square slowly moving - shouldn't be too hard to do


Overall:
* Clean up code and make sections smaller

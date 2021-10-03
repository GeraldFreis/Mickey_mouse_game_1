import tkinter as tk
import sqlite3 as sq



"""
Things that must be done in this file
"""


# produce a smaller and centralised input (tick)
# Enable the inputs to be accessible and to retrieve things from the file written to (tick)
# ** first step to enable this is to make the database an excel file through the db file path (will not do)
# refactor the code to make it cleaner because rn it is ass (tick)
# ensure that the returned level is correct (tick)

name = str()
level = int()


""" 
Making a database to be accessed by the input
"""


class Database():  # creating the database
    def __init__(self):
        self.db = sq.connect("player_database.db")
        self.cursor = self.db.cursor()
        # self.db.execute("create table names(name, level)")  #commented out because the database has been created
    
    def adding_data_for_new_player(self, name, player_level):  # adding information for new players
        sq_insert = """INSERT INTO names (name, level) VALUES (?, ?);"""
        data = name, player_level
        self.db.execute(sq_insert, data)
        self.db.commit()
        print("Hi {} your level of: {} will now be played".format(name, player_level))
    
    def retrieve_data_for_returned_player(self, name, player_level):  # retrieving information for existing players
        names = list(self.cursor.execute("""SELECT * FROM names""".format(name)))
        refined_list = list()  # list to store player names from the names list which is essentially just a dictionary
        for player in names:  # iterating through the original player list
            # print(player)
            if player[0] == name:  # checking if the first element of the player (the name) is equal to the user's provided name
                refined_list.append(player)  # adding the player element to the refined list
                # print(player)  # test condition met - code reaches this
            else:
                pass
        refined_list.sort(reverse=True)  # this is to ensure that the order of names is ascending from high to low; which means a low iteration will be made - reducing run time
        # print(refined_list)  # code passed this test condition
        last_time_played = refined_list[0]  # this returns the first value / name-level tuple in the list
        latest_level = last_time_played[1]  # this returns the level of the first name-level tuple in the list
        # print(latest_level)  # code successfully provided the highest level
        print("Your highest level played is {} \n this level will now be played".format(str(latest_level)))
        player_level = latest_level
        global level
        level = player_level  # rewriting the global variable
        # print(level)  # just another unit test
        return level
    
    def increasing_level_for_player_if_returned(self, name):
        global level
        query = """INSERT INTO names (name, level) Values (?, ?);"""
        increased_level = level + 1
        data = name, increased_level
        self.db.execute(query, data)
        self.db.commit()
        print("Your increased level of {} has been added to the database".format(increased_level))


"""
Globals
"""

db = Database()


"""
Creating a tkinter input window
"""


class Window:
    def __init__(self):
        self.win = tk.Tk()  # intialising the window
        self.win.geometry('150x60+650+400')
        self.win.config(bg='White')  # creating a colour to match that of the pygame gui
    
    def first_window(self):
        def play_status_yes():  # function to show whether or not the player has played before
            self.win.destroy() # to destroy old window

            """
            Making a new window for the player
            """

            new_win = tk.Tk()
            new_win.geometry('300x75+600+400')
            new_win.config(bg='White')

            # making labels

            tk.Label(new_win, text="Enter name: ", background="White").grid(row=1)
            tk.Label(new_win, text="Enter level to play: ", background="White").grid(row=5)

            e = tk.Entry(new_win)
            en = tk.Entry(new_win)

            e.grid(row=1, column=1)
            en.grid(row=5, column=1)

            def get_values():  # returning values to use within the main script
                name_ = e.get()
                level_ = en.get()
                global name, level
                level = int(level_)
                name = str(name_)
                new_win.destroy()
                db.adding_data_for_new_player(name, player_level=level)
                return name, level

            tk.Button(new_win, text='Play Game', command=get_values, background="White").grid(row=6, column=1)
            new_win.mainloop()
            return name, level

        def play_status_no():  # function to show whether or not the player has played before
            self.win.destroy() # destroying the old window

            """
            Creating a new window for the player
            """

            new_win = tk.Tk()
            new_win.geometry('200x75+600+400')
            new_win.config(bg='White')

            tk.Label(new_win, text="Enter name: ", background="White").grid(row=4)
            e = tk.Entry(new_win)
            e.grid(row=4, column=2)
            
            def get_values():  # returning values to use within the main script
                name_ = e.get()
                global name, level
                name = str(name_)
                new_win.destroy()
                db.retrieve_data_for_returned_player(name, player_level=level)
                return name, level

            tk.Button(new_win, text='Play Game', command=get_values, background="White").grid(row=6, column=2)
            new_win.mainloop()
            self.win.quit()

        tk.Label(self.win, text="Are You New?", background="White").grid(row=2, column=4)
        tk.Button(self.win, text="YES", command=play_status_yes, background="White").grid(row=3, column=2)
        tk.Button(self.win, text="NO", command=play_status_no, background="White").grid(row=3, column=6)

        self.win.mainloop()

win = Window()
win.first_window()
# print(name + '\n' + str(level)) #---> to test whether or not the functions will work

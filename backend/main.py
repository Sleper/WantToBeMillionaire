# from questions import questions
from Interface import *


root = game_window()

width_of_window = 1280
height_of_window = 720

screen_width = root.winfo_screenwidth()
screen_heigth = root.winfo_screenheight()

x_coordinate = (screen_width/2) - (width_of_window/2)
y_coordinate = (screen_heigth/2) - (height_of_window/2)

root.geometry("%dx%d+%d+%d" % (width_of_window, height_of_window, x_coordinate, y_coordinate))
root.resizable(0, 0)
root.mainloop()

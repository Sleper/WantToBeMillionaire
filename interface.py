# from tkinter import *
# import tkFont


# class startGame:
#     def __init__(self, master):
#         self.master = master
#         master.title("Who wants to be a millionare")


#         # logo = Label(self.master, image = "C:\Users\salia\OneDrive\Desktop\Who Wants to Be a Millionaire\logo.jgp")
#         # logo.pack()

#         startGame = Button(self.master, text="Start game", height = 3, width = 25, font=('helvetica', 15,'bold'))
#         startGame.grid(row=0, columnspan=2)

#         quitGame = Button(self.master, text="Quit",font=('helvetica', 15,'bold'), command=self.master.destroy, height = 3, width = 25 )
#         quitGame.grid(row=1)


# root = Tk()
# root.geometry("650x400")
# game = startGame(root)
# root.mainloop()
try:
    # Python2
    import Tkinter as tk
except ImportError:
    # Python3
    import tkinter as tk
root = tk.Tk()
root.title('background image')
# pick a .gif image file you have in the working directory
fname = "C:\\Users\\salia\\OneDrive\\Desktop\\WantToBeMillionaire\\WantToBeMillionaire\\interface\\71VpHPnLOjL.png"
bg_image = tk.PhotoImage(file=fname)
# get the width and height of the image
w = bg_image.width()
h = bg_image.height()
# size the window so the image will fill it
root.geometry("%dx%d+50+30" % (w, h))
cv = tk.Canvas(width=w, height=h)
cv.pack(side='top', fill='both', expand='yes')
cv.create_image(0, 0, image=bg_image, anchor='nw')
# add canvas text at coordinates x=500, y=400
# anchor='nw' implies upper left corner coordinates
cv.create_text(
    w-115, h-80, text="Made by:\nAlgirdas Saliamonas\nDominykas Okas\nRobertas Kivyta", fill="red", anchor='nw')
# now add some button widgets
btn1 = tk.Button(cv, text="Start game")
btn1.pack(side='left', padx=10, pady=5, anchor='sw')
btn2 = tk.Button(cv, text="Quit", command=root.destroy)
btn2.pack(side='left', padx=10, pady=5, anchor='sw')
root.mainloop()


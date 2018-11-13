from tkinter import *
import tkFont


class startGame:
    def __init__(self, master):
        self.master = master
        master.title("Who wants to be a millionare")
        master.config(bg="#1c60cc")

        # logo = Label(self.master, image = "C:\\Users\\Robertas-PC\\WantToBeMillionaire\\interface\\71VpHPnLOjL.png")
        # logo.pack()
        # background_image=PhotoImage("C:\\Users\\Robertas-PC\\WantToBeMillionaire\\logo.jgp")
        fname = "C:\\Users\\Algirdas\\Desktop\\Millionaire\\WantToBeMillionaire\\interface\\71VpHPnLOjL.png"
        image_background = PhotoImage(file=fname)
        w = image_background.width()
        h = image_background.height()
        # cv = Canvas(width=w, height=h)
        # cv.pack
        # greeting = Label(self.master, text="Welcome!", font=('helvetica', 25,'bold'), bg="#1c60cc", fg="white")
        # greeting.pack(side=TOP, fill=X, expand=1)

        # quitGame = Button(self.master, text="Quit",font=('helvetica', 15,'bold'), command=self.master.destroy, height = 2, width = 20, bg="#42a1f4")
        # quitGame.pack(side=BOTTOM)

        # startGame = Button(self.master, text="Start game", height = 2, width = 20, font=('helvetica', 15,'bold'), bg="#42a1f4")
        # startGame.pack(side=BOTTOM)


root = Tk()

# root.geometry("%dx%d+50+30" % (w, h))
root.geometry("600x500")
game = startGame(root)
root.mainloop()

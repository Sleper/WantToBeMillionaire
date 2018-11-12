from tkinter import *
import tkFont


class startGame:
    def __init__(self, master):
        self.master = master
        master.title("Who wants to be a millionare")

        
        # logo = Label(self.master, image = "C:\Users\salia\OneDrive\Desktop\Who Wants to Be a Millionaire\logo.jgp")
        # logo.pack()

        startGame = Button(self.master, text="Start game", height = 3, width = 25, font=('helvetica', 15,'bold'))
        startGame.grid(row=0, columnspan=2)

        quitGame = Button(self.master, text="Quit",font=('helvetica', 15,'bold'), command=self.master.destroy, height = 3, width = 25 )
        quitGame.grid(row=1)


root = Tk()
root.geometry("650x400")
game = startGame(root)
root.mainloop()
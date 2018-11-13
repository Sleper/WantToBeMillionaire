from tkinter import *


class startGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Who wants to be a millionare")
        # self.master.config(bg="#1c60cc")
        
        self.fname = "C:\\Users\\salia\\OneDrive\\Desktop\\WantToBeMillionaire\\WantToBeMillionaire\\interface\\71VpHPnLOjL.png"
        self.bg_image = PhotoImage(file=self.fname)

        # get the width and height of the image
        w = self.bg_image.width()
        h = self.bg_image.height()

        # size the window so the image will fill it
    
        cv = Canvas(width=w, height=h, bg="#1d0859")
        cv.pack(side='top', fill='both', expand='yes')
        cv.create_image((1100)//2, 0, image=self.bg_image, anchor='nw')

        cv.create_text(w+400, h+80, text="Made by:\nAlgirdas Saliamonas\nDominykas Okas\nRobertas Kivyta", fill="red", anchor='se')
        # greeting = Label(self.master, text="Welcome!", font=('helvetica', 25,'bold'), bg="#1c60cc", fg="white")
        # greeting.pack(side=TOP, fill=X, expand=1)

        quitGame = Button(cv, text="Quit",font=('helvetica', 15,'bold'), command=self.master.destroy, height = 2, width = 20, bg="#42a1f4")
        quitGame.pack(side=BOTTOM, padx=10, pady=4,anchor='s')

        startGame = Button(cv, text="Start game", height = 2, width = 20, font=('helvetica', 15,'bold'), bg="#42a1f4", command=self.start_Game)
        startGame.pack(side=BOTTOM, padx=10, pady=4,anchor='s')
        startGame.bind('<Button-1>', self.start_Game)

    def start_Game(self):
        x = self.master.destroy()
        root = Tk()
        root.state('zoomed')
        game = gamePlay(root)


       


class gamePlay:
    def __init__(self, master):
        self.master = master
        self.master.title("Who wants to be a millionare")
        self.master.config(bg="#1d0859")


root = Tk()
game = startGame(root)
root.state('zoomed')
root.mainloop()
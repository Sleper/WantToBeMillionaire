import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from answers import Answers

import sys
import os


answer = Answers()

LARGE_FONT = ("Verdana", 12)
small_font = ("Verdana", 8)


class game_window(tk.Tk):
    # args - any number of arguments
    # kwargs - any number of key word arguments
    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)

        tk.Tk.wm_title(self, "Who wants to be a millionare")

        container = tk.Frame(self)
        container.grid(row=0, columnspan=2, sticky="nsew")
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (startGame, playGame):
            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        # First window to start
        self.show_frame(startGame)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class startGame(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label = ttk.Label(self, text="Welcome!", font=LARGE_FONT)
        label.pack(pady=300)

        quitButton = ttk.Button(self, text="Quit",
                                command=quit)
        quitButton.pack(pady=5, side="bottom")

        startButton = ttk.Button(self, text="Start game",
                                 command=lambda: controller.show_frame(playGame))
        startButton.pack(pady=5, side="bottom")


class playGame(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        # Quit\Leave with money won
        quitButton = ttk.Button(self, text="Quit",
                                command=lambda: self.button_pressed("q"))
        quitButton.grid(row=0, sticky="w")

        # Question
        self.label = tk.Label(self, text=answer.get_question(),
                              font=LARGE_FONT, wraplength=750, justify="center", width=90, height=30)
        self.label.grid(row=1, columnspan=2, pady=10, padx=53)

        # Get new answers
        answer.set_answers()
        ans = answer.randomAnswers()
        # Getting answers value on the buttons
        self.button1 = ttk.Button(self, text="A - " + ans[0],
                                  command=lambda: self.button_pressed(ans[0]))
        self.button1.grid(row=2, column=0, sticky="we", pady=10, padx=5)

        self.button2 = ttk.Button(self, text="B - " + ans[1],
                                  command=lambda: self.button_pressed(ans[1]))
        self.button2.grid(row=2, column=1, sticky="we", pady=10, padx=5)

        self.button3 = ttk.Button(self, text="C - " + ans[2],
                                  command=lambda: self.button_pressed(ans[2]))
        self.button3.grid(row=3, column=0, sticky="we", pady=10, padx=5)

        self.button4 = ttk.Button(self, text="D - " + ans[3],
                                  command=lambda: self.button_pressed(ans[3]))
        self.button4.grid(row=3, column=1, sticky="we", pady=10, padx=5)

        # Help
        helpAsk_the_Audience = ttk.Button(self, text="Ask the Audience",
                                          command=lambda: self.button_pressed(5))
        helpAsk_the_Audience.grid(row=0, column=3)

        help50_50 = ttk.Button(self, text="50:50",
                               command=lambda: self.button_pressed(6))
        help50_50.grid(row=0, column=4)

        helpPhone_a_Friend = ttk.Button(self, text="Phone a Friend",
                                        command=lambda: self.button_pressed(7))
        helpPhone_a_Friend.grid(row=0, column=5)

        self.corect_answer = 0
        self.prize()
        self.money_won = "0"
        self.money_won_save = "0"

    def prize(self):
        # Money won
        labelsFrame = ttk.LabelFrame(self, text="Prize")
        labelsFrame.grid(row=1, column=3, columnspan=3, rowspan=15)

        prize = ["100", "200", "300", "500", "1,000", "2,000", "4,000", "8,000",
                 "16,000", "32,000", "64,000", "125,000", "250,000", "500,000", "1,000,000"]
        count = 0

        number = 15
        for money in prize[::-1]:
            text = str(number) + " - " + str(money)
            if self.corect_answer == number:
                self.money_won = money
                if money in ["1,000", "32,000"]:
                    self.money_won_save = money
                tk.Label(labelsFrame, text=text, fg="red").grid(
                    row=1+count, columnspan=3, sticky="w")
            else:
                if money in ["1,000", "32,000", "1,000,000"]:
                    tk.Label(labelsFrame, text=text, fg="blue").grid(
                        row=1+count, columnspan=3,  sticky="w")
                else:
                    tk.Label(labelsFrame, text=text).grid(
                        row=1+count, columnspan=3,  sticky="w")
            count += 1
            number -= 1

    def button_pressed(self, button):
        if button == "q":
            if messagebox.showinfo("Thanks for playing", "You won " + self.money_won + ".\nSee you soon.") == "ok":
                self.quit()
        elif button == answer.get_correct_answer():
            self.corect_answer += 1
            if answer.gameLength == self.corect_answer:
                self.prize()
                if messagebox.askyesno(
                        "You won!", "Congratulations!\nYou won 1,000,000!") == True:
                    python = sys.executable
                    os.execl(python, python, * sys.argv)
                else:
                    self.quit()
            else:
                answer.set_answers()
                ans = answer.randomAnswers()
                q = answer.get_question()
                self.change_buttons_value(ans, q)
                self.prize()
        elif button in [5, 6, 7]:
            messagebox.showinfo("Help", "Not implemented yet.")
        else:
            if messagebox.askyesno(
                    "Game over", "Game is over. You won " + self.money_won_save + ".\nDo you wanna try again?") == True:
                python = sys.executable
                os.execl(python, python, * sys.argv)
            else:
                self.quit()

    def change_buttons_value(self, ans, question):
        self.label["text"] = question
        self.button1["text"] = "A - " + ans[0]
        self.button1["command"] = lambda: self.button_pressed(ans[0])
        self.button2["text"] = "B - " + ans[1]
        self.button2["command"] = lambda: self.button_pressed(ans[1])
        self.button3["text"] = "C - " + ans[2]
        self.button3["command"] = lambda: self.button_pressed(ans[2])
        self.button4["text"] = "D - " + ans[3]
        self.button4["command"] = lambda: self.button_pressed(ans[3])

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from answers import Answers
from Counter import Counter

import sys
import os


answer = Answers()
largeFont = ("Verdana", 12)

class GameWindow(tk.Tk):
    # args - any number of arguments
    # kwargs - any number of key word arguments
    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)

        tk.Tk.wm_title(self, "Who wants to be a millionare")

        self.container = tk.Frame(self)
        self.container.grid(row=0, columnspan=2, sticky="nsew")
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        frame = StartGame(self.container, self)
        frame.grid(row=0, column=0, sticky="nsew")
        frame.tkraise()

    def startNewGame(self):
        frame = PlayGame(self.container, self)
        frame.grid(row=0, column=0, sticky="nsew")
        frame.tkraise()


class StartGame(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label = ttk.Label(self, text="Welcome!", font=largeFont, width=120, anchor="center")
        label.grid(row=0, column=0, sticky="we", pady=300, padx=5)

        quitButton = ttk.Button(self, text="Quit",
                                command=quit)
        quitButton.grid(row=2, pady=10, padx=5)

        startButton = ttk.Button(self, text="Start game",
                                 command=controller.startNewGame)
        startButton.grid(row=1, pady=10, padx=5)


class PlayGame(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        # Quit\Leave with money won
        self.quitButton = ttk.Button(self, text="Quit",
                                command=lambda: self.buttonPressed("q"))
        self.quitButton.grid(row=0, sticky="w")

        # Counter
        self.timeLabel = tk.Label(self, text="", justify="left", font=largeFont)
        self.timeLabel.grid(row=1, columnspan=2)
        self.counter = Counter(30, self.timeLabel, self)

        # Question
        self.label = tk.Label(self, text=answer.get_question(),
                              font=largeFont, wraplength=750, justify="center", width=90, height=30)
        self.label.grid(row=2, columnspan=2, pady=10, padx=53)

        # Get new answers
        answer.set_answers()
        ans = answer.randomAnswers()
        # Getting answers value on the buttons
        self.button1 = ttk.Button(self, text="A - " + ans[0],
                                  command=lambda: self.buttonPressed(ans[0]))
        self.button1.grid(row=3, column=0, sticky="we", pady=10, padx=5)

        self.button2 = ttk.Button(self, text="B - " + ans[1],
                                  command=lambda: self.buttonPressed(ans[1]))
        self.button2.grid(row=3, column=1, sticky="we", pady=10, padx=5)

        self.button3 = ttk.Button(self, text="C - " + ans[2],
                                  command=lambda: self.buttonPressed(ans[2]))
        self.button3.grid(row=4, column=0, sticky="we", pady=10, padx=5)

        self.button4 = ttk.Button(self, text="D - " + ans[3],
                                  command=lambda: self.buttonPressed(ans[3]))
        self.button4.grid(row=4, column=1, sticky="we", pady=10, padx=5)

        # Help
        helpAskTheAudience = ttk.Button(self, text="Ask the Audience",
                                          command=lambda: self.buttonPressed(5))
        helpAskTheAudience.grid(row=0, column=3)

        help50_50 = ttk.Button(self, text="50:50",
                               command=lambda: self.buttonPressed(6))
        help50_50.grid(row=0, column=4)

        helpPhoneAFriend = ttk.Button(self, text="Phone a Friend",
                                        command=lambda: self.buttonPressed(7))
        helpPhoneAFriend.grid(row=0, column=5)

        self.corectAnswer = 0
        self.prize()
        self.moneyWon = "0"
        self.moneyWonSave = "0"

        self.gameOver()

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
            if self.corectAnswer == number:
                self.moneyWon = money
                if money in ["1,000", "32,000"]:
                    self.moneyWonSave = money
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

    def buttonPressed(self, button):
        if button == "q":
            if messagebox.showinfo("Thanks for playing", "You won " + self.moneyWon + ".\nSee you soon.") == "ok":
                self.quit()
        elif button == answer.get_correct_answer():
            self.corectAnswer += 1
            if answer.gameLength == self.corectAnswer:
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
                self.changeButtonsValue(ans, q)
                self.prize()
                if self.corectAnswer in (1 ,2 , 3, 4):
                    self.counter.reset(30)
                elif self.corectAnswer in (5 ,6 , 7, 8, 9):
                    self.counter.reset(45)
                else:
                    self.counter.reset(60)
        elif button in [5, 6, 7]:
            self.counter.stop()
            if messagebox.showinfo("Help", "Not implemented yet.") == "ok":
                self.counter.resume()
        else:
            if messagebox.askyesno(
                    "Game over", "Game is over. You won " + self.moneyWonSave + ".\nDo you wanna try again?") == True:
                python = sys.executable
                os.execl(python, python, * sys.argv)
            else:
                self.quit()

    def changeButtonsValue(self, ans, question):
        self.label["text"] = question
        self.button1["text"] = "A - " + ans[0]
        self.button1["command"] = lambda: self.buttonPressed(ans[0])
        self.button2["text"] = "B - " + ans[1]
        self.button2["command"] = lambda: self.buttonPressed(ans[1])
        self.button3["text"] = "C - " + ans[2]
        self.button3["command"] = lambda: self.buttonPressed(ans[2])
        self.button4["text"] = "D - " + ans[3]
        self.button4["command"] = lambda: self.buttonPressed(ans[3])

    def gameOver(self):
        if self.counter.sec == 0:
            if messagebox.askyesno(
                    "Game over", "Game is over. You won " + self.moneyWon + ".\nDo you wanna try again?") == True:
                python = sys.executable
                os.execl(python, python, * sys.argv)
            else:
                self.quit()
        self.after(1000, self.gameOver)

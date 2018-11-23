from random import randint


class Help:
    def __init__(self, button1, button2, button3, button4, correct_asnwer):
        self.button1 = button1
        self.button2 = button2
        self.button3 = button3
        self.button4 = button4
        self.correct_answer = correct_asnwer
        self.button_array = [button1, button2, button3, button4]

    def fifty_fifty(self):
        copy_button_array = self.button_array.copy()
        for button in copy_button_array:
            if button['text'][4:] == self.correct_answer.get_correct_answer():
                copy_button_array.remove(button)

        rand = randint(0, 2)
        copy_button_array.pop(rand)
        for button in copy_button_array:
            button["state"] = "disabled"

    def ask_audience(self):
        correct_ans = ""
        wrong_array = []
        precent = 0
        temp = 0
        for button in self.button_array:
            if button['text'][4:] == self.correct_answer.get_correct_answer():
                correct_ans = button['text'][0]
            else:
                wrong_array.append(button['text'][0])

        for index in range(len(wrong_array)):
            temp = randint(10, 30)
            precent += temp
            wrong_array[index] = wrong_array[index] + " : " + str(temp) + "%"

        correct_ans = correct_ans + " : " + str(100 - precent) + "%"
        wrong_array.append(correct_ans)
        wrong_array.sort()
        return '\n'.join(wrong_array)

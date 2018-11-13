from questions import questions
from random import randint


class Answers:
    def __init__(self):
        self.answers = []
        self.counter = 0
        self.correct_answer = questions[self.counter].get_correct_answer()
        self.question = questions[self.counter].get_question()

    def set_answers(self):
        self.answers = []
        for answer in questions[self.counter].get_wrong_answers():
            self.answers.append(answer)
        self.answers.append(questions[self.counter].get_correct_answer())
        self.set_counter(1)

    def set_counter(self, num):
        self.counter += num

    def get_answers(self):
        return(self.answers)

    def get_correct_answer(self):
        return self.correct_answer

    def get_question(self):
        return self.question


def populateAnswers(question, counter):
    answers = []
    for answer in question.get_wrong_answers():
        answers.append(answer)
    answers.append(question.get_correct_answer())
    print(answers)


def randomAnswers(answers):
    counter = 0
    newAnswers = []
    truths = [True, True, True, True]
    while counter < 4:
        value = randint(0, 3)
        if truths[0] and value == 0:
            newAnswers.append(answers[value])
            counter += 1
            truths[0] = False
        if truths[1] and value == 1:
            newAnswers.append(answers[value])
            counter += 1
            truths[1] = False
        if truths[2] and value == 2:
            newAnswers.append(answers[value])
            counter += 1
            truths[2] = False
        if truths[3] and value == 3:
            newAnswers.append(answers[value])
            counter += 1
            truths[3] = False
    return newAnswers


def seeAnswers(answers):
    print(answer.get_question())
    for index in range(len(answers)):
        print(index, answers[index])
    print("select your decision")
    choice = input()
    choice = int(choice)
    if answers[choice] == answer.get_answers()[3]:
        return "You're right"
    else:
        return "You're Wrong"


answer = Answers()
print(answer.set_answers())
print(answer.get_answers())
arr = randomAnswers(answer.get_answers())
print(seeAnswers(arr))

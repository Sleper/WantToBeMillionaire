from questions import questions
from random import randint
import html


class Answers:
    def __init__(self):
        self.answers = []
        self.counter = 0
        self.correct_answer = questions[self.counter].get_correct_answer()
        self.question = questions[self.counter].get_question()
        self.gameLength = len(questions)

    def set_answers(self):
        self.answers = []
        self.get_data()

    def set_counter(self, num):
        self.counter += num

    def set_question(self):
        self.question = questions[self.counter].get_question()

    def set_correct_answer(self):
        self.correct_answer = questions[self.counter].get_correct_answer()

    def get_answers(self):
        return(self.answers)

    def get_correct_answer(self):
        return self.correct_answer

    def get_question(self):
        return self.question

    def randomAnswers(self):
        counter = 0
        newAnswers = []
        truths = [True, True, True, True]
        while counter < 4:
            value = randint(0, 3)
            if truths[0] and value == 0:
                newAnswers.append(self.answers[value])
                counter += 1
                truths[0] = False
            if truths[1] and value == 1:
                newAnswers.append(self.answers[value])
                counter += 1
                truths[1] = False
            if truths[2] and value == 2:
                newAnswers.append(self.answers[value])
                counter += 1
                truths[2] = False
            if truths[3] and value == 3:
                newAnswers.append(self.answers[value])
                counter += 1
                truths[3] = False
        return newAnswers

    def get_data(self):
        for answer in questions[self.counter].get_wrong_answers():
            self.answers.append(html.unescape(answer))
        self.answers.append(questions[self.counter].get_correct_answer())
        self.set_question()
        self.set_correct_answer()
        self.set_counter(1)


# answer = Answers()

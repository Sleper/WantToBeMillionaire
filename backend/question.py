import html


class Question:
    def __init__(self, question="", difficulty_type="", correct_answer="", wrong_answers=[]):
        self.question = html.unescape(question)
        self.difficulty_type = difficulty_type
        self.correct_answer = html.unescape(correct_answer)
        self.wrong_answers = wrong_answers

    def set_question(self, question):
        self.question = question

    def set_difficulty(self, difficulty):
        self.difficulty_type = difficulty

    def set_correct_answer(self, answer):
        self.correct_answer = answer

    def set_wrong_answers(self, answers):
        for answer in answers:
            self.correct_answer.append(answer)

    def get_question(self):
        return self.question

    def get_difficulty_type(self):
        return self.difficulty_type

    def get_correct_answer(self):
        return self.correct_answer

    def get_wrong_answers(self):
        return self.wrong_answers

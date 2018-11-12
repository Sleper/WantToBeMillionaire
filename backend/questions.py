import requests
import json


parameters = {"amount": 5, "category": 10,
              "difficulty": "easy", "type": "multiple"}

headers = {'Content-Type': 'application/json'}


class Question:
    def __init__(self, question="", difficulty_type="", correct_answer="", wrong_answers=[]):
        self.question = question
        self.difficulty_type = difficulty_type
        self.correct_answer = correct_answer
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


questions = []

# Getting the data from the API.
response = requests.get(
    "https://opentdb.com/api.php", params=parameters, headers=headers)


# Checking if the Status code was 200, if it was store it in a variable
if response.status_code == 200:
    data = json.loads(response.content.decode('utf-8'))
else:
    print("Something went Wrong!")


# Check if data was not an empty object, if it wasn't store it into the array of objects
if data is not None:
    print("Here is your info: ")
    for index in range(len(data["results"])):
        questions.append(Question(
            data["results"][index]["question"], data["results"][index]["difficulty"], data["results"][index]["correct_answer"], data["results"][index]["incorrect_answers"]))

else:
    print("Data was not taken.")


print(questions[1].get_wrong_answers())


#secondQuestions = data["results"][2]["question"]

import requests
import json
from question import Question


questions = []


def load_questions(parameters):
    headers = {'Content-Type': 'application/json'}
    # Getting the data from the API.
    for parameter in parameters:
        response = requests.get(
            "https://opentdb.com/api.php", params=parameter, headers=headers)

        # Checking if the Status code was 200, if it was store it in a variable
        if response.status_code == 200:
            data = json.loads(response.content.decode('utf-8'))
        else:
            print("Couldn't connect to the server!")

        # Check if data was not an empty object, if it wasn't store it into the array of objects
        if data is not None:
            for index in range(len(data["results"])):
                questions.append(Question(
                    data["results"][index]["question"], data["results"][index]["difficulty"], data["results"][index]["correct_answer"], data["results"][index]["incorrect_answers"]))

        else:
            print("Data was not taken.")

        #secondQuestions = data["results"][2]["question"]


parameters = [{"amount": 5, "difficulty": "easy", "type": "multiple"},
              {"amount": 5, "difficulty": "medium", "type": "multiple"},
              {"amount": 5, "difficulty": "hard", "type": "multiple"}]

load_questions(parameters)

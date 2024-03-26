import json
import os

def first_power():
    if os.path.isfile("bd_question.json"):
        print("Файл существует")
    else:
        session = []
        with open("bd_question.json", 'w') as file:
            # Записываем данные в JSON-файл
            json.dump(session, file)

first_power()

def read_json(filename):
    with open(filename, "r", encoding='utf-8') as file:
        questions = json.load(file)
    return questions

print(read_json("bd_question.json"))

questions = [
  {
    "question":"Сам вопрос непосредственно",
    "answer_right": "Правельный ответ",
    "answer_1": "Не правельный ответ"
  },
  {
    "question":"Сам вопрос непосредственно",
    "answer_right": "Правельный ответ",
    "answer_1": "Не правельный ответ"
  },
  {
    "question":"Сам вопрос непосредственно",
    "answer_right": "Правельный ответ",
    "answer_1": "Не правельный ответ"
  },
  {
    "question":"Сам вопрос непосредственно",
    "answer_right": "Правельный ответ",
    "answer_1": "Не правельный ответ"
  }
]

with open("bd_question.json", 'w') as file:
    # Записываем данные в JSON-файл
    json.dump(questions, file)

print(read_json("bd_question.json"))






import inquirer
import json
import numpy as np
import os


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


correctAnswers = 0
wrongAnswers = 0

selectKana = [
    inquirer.List('kana',
                  message="What do you want to practice?",
                  choices=['Hiragana', 'Katakana'],
                  ),
]

answers = inquirer.prompt(selectKana)

with open('data/' + answers['kana'] + '.json') as jsonFile:
    jsonObject = json.load(jsonFile)
    jsonFile.close()

for character, answers in jsonObject['characters'].items():
    cls()
    print('Correct answers: ' + str(correctAnswers) +
          '\nWrong answers: ' + str(wrongAnswers) + '\n\n')
    character = character
    answer = input(u'Enter ' + character + ' in romaji: ')
    if answer in answers:
        correctAnswers += 1
    else:
        wrongAnswers += 1

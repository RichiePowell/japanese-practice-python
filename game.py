import inquirer
import json
import sys
import signal
import os
from random import shuffle


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


# Avoid stacktrace on CTRL + C
signal.signal(signal.SIGINT, lambda x, y: sys.exit(0))

# Get data sets
filenames = sorted([".".join(f.split(".")[:-1])
                    for f in os.listdir('./data') if f.endswith('.json')])

# If there are none, exit the app
if len(filenames) == 0:
    print("No data sets found. Please add json files to the data folder.")
    exit()

# Ask for which data set to practice
while True:
    stats = {'correct': 0, 'incorrect': 0}

    while True:
        datasetChoice = [
            inquirer.Checkbox('dataset',
                              message="What do you want to practice?",
                              choices=filenames,
                              ),
        ]
        askDataset = inquirer.prompt(datasetChoice)['dataset']

        # Make sure the user has selected at least one dataset
        if(len(askDataset) > 0):
            break

    # Load each selected dataset
    currentDataset = 0
    loadedData = dict()
    for dataset in askDataset:
        with open('data/' + dataset + '.json') as jsonFile:
            loadedData.update(json.load(jsonFile)['characters'])
            jsonFile.close()

    # Shuffle the loaded data
    loadedData = list(loadedData.items())
    shuffle(loadedData)
    loadedData = dict(loadedData)

    # Loop through each character in the loaded datasets
    for character, answers in loadedData.items():
        cls()
        print('Correct answers: ' + str(stats['correct']) +
              '\nWrong answers: ' + str(stats['incorrect']) + '\n\n')
        answer = input(u'Enter ' + character + ' in romaji: ')
        if answer in answers:
            stats['correct'] += 1
        else:
            stats['incorrect'] += 1

    cls()

    # Calculate and display the percentages of correct and incorrect answers
    correctPercentage = (stats['correct'] / len(loadedData) * 100)
    incorrectPercentage = (stats['incorrect'] / len(loadedData) * 100)
    print('Correct answers: %s (%s%%)' %
          (str(stats['correct']), int(correctPercentage)))
    print('Incorrect answers: %s (%s%%)' %
          (str(stats['incorrect']), int(incorrectPercentage)))

    # Show different outputs depending on results
    if correctPercentage == 100:
        print("\nCongratulations! You've achieved a perfect score!")
    elif correctPercentage > 75:
        print("\nWell done - you're doing really well!")
    elif correctPercentage > 50:
        print("\nOver 50%% correct - keep practicing!")
    else:
        print("\nKeep learning and you'll get there! :)\n\n")

    # Ask if the user wants to play again
    while True:
        playAgain = input('Would you like to play again? (Y/n) ')
        if playAgain[:1].lower() == 'y':
            cls()
            break
        elif playAgain[:1].lower() == 'n':
            exit()
        else:
            print('Please enter "Y" or "N".')

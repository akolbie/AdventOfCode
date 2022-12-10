"""
A is rock
B is Paper
C is Scissors

X is rock
Y is Paper
Z is Scissors
"""

import csv

LOCATION = 'day2_input.csv'

def calc_results(location):
    total_score = 0

    with open(location) as f:
        csv_reader = csv.reader(f)
        for match in csv_reader:
            #total_score += round_1(match[0][0], match[0][2])
            total_score += round_2(match[0][0], match[0][2])
    return total_score

def round_2(opponent, your_result):
    max_dict = {
        'A' : {'X' : 3 + 0, 'Y' : 1 + 3, 'Z': 2 + 6},
        'B' : {'X' : 1 + 0, 'Y' : 2 + 3, 'Z' : 3 + 6},
        'C' : {'X' : 2 + 0, 'Y' : 3 + 3, 'Z' : 1 + 6}
    }
    return max_dict[opponent][your_result]


def round_1(opponent, you):
    dict = {'A' : 'R', 'X' : 'R', 'B' : 'P', 'Y' : 'P', 'C' : 'S', 'Z': 'S'}
    score_dict = {'R' : 1, 'P': 2, 'S' : 3}
    opponent = dict[opponent]
    you = dict[you]
    score = 0

    if opponent == you:
        score = 3
    elif opponent == "R":
        if you == 'P': # you beat opponent
            score = 6
        else:
            score = 0
    elif opponent == 'P':
        if you == 'S':
            score = 6
        else:
            score = 0
    else:
        if you == 'R':
            score = 6
        else:
            score = 0
    return score + score_dict[you]

if __name__ == "__main__":
    print(calc_results(LOCATION))
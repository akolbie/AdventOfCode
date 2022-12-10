import csv
from math import floor

LOCATION = 'day9_input.csv'
MOVE_DICT = {'L' : [-1, 0], 'R': [1, 0], 'U' : [0, 1], 'D' : [0, -1]}

#[X, Y]
def import_data(location):
    output = []
    with open(location) as f:
        csv_reader = csv.reader(f)
        for row in csv_reader:
            output.append(row[0].split(' '))
    return output


class Board():
    def __init__(self):
        self.head_pos = [0, 0]
        self.tail_pos = [0, 0]
        self.historical_tail_pos = [[0,0]]

    def move_head(self, move):
        for i in range(int(move[1])):
            self.head_pos[0] += MOVE_DICT[move[0]][0]
            self.head_pos[1] += MOVE_DICT[move[0]][1]
            self.move_tail()

    def move_tail(self):
        # if self.head_pos == self.tail_pos: #on top of each other
        #     pass
        # elif abs(self.head_pos[0] - self.tail_pos[0]) <= 1 and abs(self.head_pos[1] - self.tail_pos[1]) <= 1: #within accepable distance
        #     pass
        # elif self.head_pos[0] == self.tail_pos[0]: # same column
        #     if self.head_pos[1] - 2 == self.tail_pos[1]: #head 2 spaces higher than tail
        #         self.tail_pos[1] += 1
        #     else: #head pos 2 spaces lower than tail
        #         self.tail_pos[1] -= 1
        #     self.check_tail_pos()
        #     return
        # elif self.head_pos[1] == self.tail_pos[1]: #same row
        #     if self.head_pos[0] - 2 == self.tail_pos[1]: # head 2 spaces to the right of tail
        #         self.tail_pos[0] += 1
        #     else: #head 2 spaces to the left of tail
        #         self.tail_pos[0] -= 1
        # else:
        #     vector = [self.head_pos[0]-self.tail_pos[0], self.head_pos[1] - self.tail_pos[1]]
        #     self.tail_pos[0] += int(vector[0] / 2)
        #     self.tail_pos[1] += int(vector[1] / 2)
        #     self.check_tail_pos()
        vector = [self.head_pos[0]-self.tail_pos[0], self.head_pos[1] - self.tail_pos[1]]
        if abs(vector[0]) + abs(vector[1]) == 3:
            vector = [2 * vector[0] / abs(vector[0]), 2 * vector[1] / abs(vector[1])]
        self.tail_pos[0] += floor(int(vector[0] / 2))
        self.tail_pos[1] += floor(int(vector[1] / 2))
        self.check_tail_pos()

    def check_tail_pos(self):
        if not self.tail_pos in self.historical_tail_pos:
            self.historical_tail_pos.append(self.tail_pos[:])

class Knot():
    def __init__(self, head, index):
        self.pos = [0, 0]
        self.head = head
        self.historical_tail_pos = [[0,0]]
        self.index = index

    def move(self):
        vector = [self.head.pos[0]-self.pos[0], self.head.pos[1] - self.pos[1]]
        if abs(vector[0]) + abs(vector[1]) == 3:
            vector = [2 * vector[0] / abs(vector[0]), 2 * vector[1] / abs(vector[1])]
        self.pos[0] += floor(int(vector[0] / 2))
        self.pos[1] += floor(int(vector[1] / 2))
        self.check_pos()
        if hasattr(self, 'tail'):
            self.tail.move()
        return
    
    def check_pos(self):
        if not self.pos in self.historical_tail_pos:
            self.historical_tail_pos.append(self.pos[:])

class Head():
    def __init__(self):
        self.pos = [0, 0]
    
    def move(self, move):
        for i in range(int(move[1])):
            self.pos[0] += MOVE_DICT[move[0]][0]
            self.pos[1] += MOVE_DICT[move[0]][1]
            self.tail.move()
        

if __name__ == "__main__":
    data = import_data(LOCATION)
    head = Head()
    knots = []
    for i in range(9):
        if i == 0:
            knots.append(Knot(head, i))
        else:
            knots.append(Knot(knots[-1],i))
    
    head.tail = knots[0]
    
    for ik, knot in enumerate(knots):
        if ik == len(knots) - 1:
            pass
        else:
            knot.tail = knots[ik + 1]

    for move in data:
        head.move(move)

    print(len(knots[-1].historical_tail_pos))
import csv
import pprint

LOCATION = 'day5_input.csv'

def get_data(location):
    with open(location) as f:
        output = []
        csv_reader = csv.reader(f)
        for row in csv_reader:
            output.append(row)
    return output

def split_stacks_from_moves(data):
    split_point = data.index([])
    stacks = data[:split_point -1]
    stacks_numbering = data[split_point - 1][0]
    moves = data[split_point + 1:]

    return stacks, stacks_numbering, moves

def create_stacks(stack_data, numbering):
    stacks = []
    i = 0
    while True:
        index = 1 + i * 4
        if index >= len(numbering):
            break
        stacks.append(Stack())
        i += 1
    for stack in stack_data:
        j = 0
        while True:
            jndex = 1 + j * 4
            if jndex >= len(numbering):
                break
            if stack[0][jndex] != ' ':
                stacks[j].add_to_stack(stack[0][jndex])
            j += 1
    for stack in stacks:
        stack.stack = stack.stack[::-1]

    return stacks


class Stack():
    def __init__(self):
        self.stack = []

    def add_to_stack(self, letter):
        self.stack = [letter, *self.stack[:]]
    
    def move_to(self, letter):
        if letter == '':
            return
        self.stack = [letter, *self.stack[:]]

    def move_from(self):
        if len(self.stack) == 0:
            return ''
        letter_removed = self.stack.pop(0)

        return letter_removed

    def move_to_all(self, letters):
        self.stack = [*letters, *self.stack]
    
    def move_from_all(self, number):
        removed = self.stack[:number]
        self.stack = self.stack[number:]

        return removed
    

def move_letters1(moves, stacks):
    for move in moves:
        if move[0][6] != ' ':
            amount = int(move[0][5] + move[0][6])
            comming_from = int(move[0][13])
            to = int(move[0][18])
        else:
            amount = int(move[0][5])
            comming_from = int(move[0][12])
            to = int(move[0][17])
        
        for i in range(amount):
            stacks[to - 1].move_to(stacks[comming_from - 1].move_from())
    
    return stacks

def move_letters2(moves, stacks):
    for move in moves:
        if move[0][6] != ' ':
            amount = int(move[0][5] + move[0][6])
            comming_from = int(move[0][13])
            to = int(move[0][18])
        else:
            amount = int(move[0][5])
            comming_from = int(move[0][12])
            to = int(move[0][17])
        
        stacks[to - 1].move_to_all(stacks[comming_from - 1].move_from_all(amount))
    
    return stacks
        
def calc_quatities_after_move(moves):
    quatity = [5,8,8,6,7,7,3,8,4]
    for move in moves:
        if move[0][6] != ' ':
            amount = int(move[0][5] + move[0][6])
            comming_from = int(move[0][13])
            to = int(move[0][18])
        else:
            amount = int(move[0][5])
            comming_from = int(move[0][12])
            to = int(move[0][17])
        quatity[comming_from - 1] -= amount
        quatity[to - 1] += amount
        if amount == 13:
            print('')
        if quatity[comming_from - 1] < 0:
            print('error')
    print(quatity)

if __name__ == "__main__":
    data = get_data(LOCATION)
    stack_data, numbering, moves = split_stacks_from_moves(data)
    stacks = create_stacks(stack_data, numbering)
    #calc_quatities_after_move(moves)
    #final1_stacks = move_letters1(moves, stacks)
    final2_stacks = move_letters2(moves, stacks)

    # output = ""
    # for final1_stack in final1_stacks:
    #     if len(final1_stack.stack):
    #         output += final1_stack.stack[0]
    # print(output)
    output = ""
    for final2_stack in final2_stacks:
        if len(final2_stack.stack):
            output += final2_stack.stack[0]
    print(output)
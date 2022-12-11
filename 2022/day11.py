import csv
from math import floor

LOCATION = 'day11_input.csv'

def import_data(location):
    output = []
    with open(location) as f:
        csv_reader = csv.reader(f)
        for row in csv_reader:
            output.append(row)
    return output

class Monkey():
    def __init__(self, starting_items, operation, test, results):
        self.items = starting_items
        self.operation = operation
        self.test = test
        self.results = {True: results[0], False : results[1]}
        self.inspections = 0
    
    def execute_turn(self):
        for item in self.items:
            level = self.operation_execution(item)
            level %= self.mod
            #level = floor(level / 3)
            send_to = self.results[level % self.test == 0]
            self.inspections += 1
            monkey.group[send_to].items.append(level)
        self.items = []

    def operation_execution(self, item):
        if '*' in self.operation:
            multiple = self.operation.split('*')[-1]
            if multiple == ' old':
                return item ** 2
            return item * int(multiple)
        elif '+' in self.operation:
            addition = self.operation.split('+')[-1]
            return item + int(addition)

def parse_data(data):
    monkeys = []
    #for i in range(4):
    for i in range(8):
        item = list(map(int,data[i*7 +1][0][18:].split(',')))
        item = [*item, *list(map(int,data[i * 7 + 1][1:]))]
        
        monkeys.append(Monkey(
            item, 
            data[i *7 + 2][0].split('=')[1], 
            int(data[i *7 + 3][0][-2:]), 
            [int(data[i *7 + 4][0][-1]), int(data[i *7 + 5][0][-1])]
            ))
    
    return monkeys
        


if __name__ == '__main__':
    data = import_data(LOCATION)
    monkeys = parse_data(data)

    mod = 1
    for monkey in monkeys:
        mod *= monkey.test

    for monkey in monkeys:
        monkey.group = monkeys
        monkey.mod = mod
    

    
    for i in range(10000):
        for monkey in monkeys:
            monkey.execute_turn()
    
    for monkey in monkeys:
        print(monkey.inspections)
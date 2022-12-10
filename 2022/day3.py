import csv 

LOCATION = 'day3_input.csv'

def get_data(location):
    rucksacks = []
    counter = 0
    groups = []
    with open(location) as f:
        csv_reeader = csv.reader(f)
        for sack in csv_reeader:
            rucksacks.append(Rucksack(sack[0]))
            counter += 1
            if counter == 3:
                groups.append(Group(rucksacks[-3:]))
                counter = 0
    return rucksacks, groups

class Rucksack:
    def __init__(self, data):
        self.contents = data
        self.first_pouch = self.contents[:len(self.contents) // 2]
        self.second_pouch = self.contents[len(self.contents) //2: ]

    def get_matches(self):
        self.matches = ''
        for char in self.first_pouch:
            if char in self.second_pouch and not char in self.matches:
                self.matches += char

    def calc_worth(self):
        self.worth = 0
        for char in self.matches:
            if ord(char) >= 97: #lower case
                self.worth += ord(char) - 96
            else: # upper case 
                self.worth += ord(char) - 64 + 26

class Group():
    def __init__(self, rucks):
        self.rucksack_1 = rucks[0]
        self.rucksack_2 = rucks[1]
        self.rucksack_3 = rucks[2]

    def find_badge(self):
        for char in self.rucksack_1.contents:
            if char in self.rucksack_2.contents and char in self.rucksack_3.contents:
                return char
        print("ERROR")
    
    def calc_worth(self, char):
        if ord(char) >= 97: #lower case
            return(ord(char) - 96)
        else: # upper case 
            return(ord(char) - 64 + 26)

def find_priorities_sum(rucksakes):
    priorities = 0
    for ruck in rucksakes:
        ruck.get_matches()
        ruck.calc_worth()
        priorities += ruck.worth
    return priorities

def find_group_priorities(groups):
    worth = 0
    for group in groups:
        worth += group.calc_worth(group.find_badge())
    return worth

if __name__ == '__main__':
    rucksakes, groups = get_data(LOCATION)
    print(find_priorities_sum(rucksakes))
    print(find_group_priorities(groups))
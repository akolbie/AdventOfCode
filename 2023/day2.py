location = 'day2.txt'

MAX = {'blue' : 14, 'red' : 12, 'green' : 13}

data = []

class Game():
    def __init__(self, data):
        if data[-1:] == '\n':
            self.data = data[0:-1]
        else:
            self.data = data

    def split(self):
        self.game_number = int(self.data.split(':')[0][5:])
        self.pulls = self.data.split(':')[1].split(';')

    def check_possible(self):
        for pull in self.pulls:
            pull_mod = pull.split(',')
            for colour in pull_mod:
                colour = colour.split(' ')
                if int(colour[1]) > MAX[colour[2]]:
                    return False
        return True

    def check_min_cubes(self):
        self.min = {'blue' : 0, 'red' : 0, 'green' : 0}
        for pull in self.pulls:
            pull_mod = pull.split(',')
            for colour in pull_mod:
                colour = colour.split(' ')
                if int(colour[1]) > self.min[colour[2]]:
                    self.min[colour[2]] = int(colour[1])

    def ret_power_cubes(self):
        self.power = 1
        for line in self.min:
            self.power *= self.min[line]
    

output_P1 = 0
with open(location) as f:
    for line in f:
        game = Game(line)
        game.split()
        if game.check_possible():
            output_P1 += game.game_number

output_P2 = 0
with open(location) as f:
    for line in f:
        game = Game(line)
        game.split()
        game.check_min_cubes()
        game.ret_power_cubes()
        output_P2 += game.power

print('Part 1: ', output_P1)
print('Part 2: ', output_P2)

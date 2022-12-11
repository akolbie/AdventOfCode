import csv

LOCATION = 'day6_input.csv'

def import_data(location):
    output = []
    with open(location) as f:
        csv_reader = csv.reader(f)
        for row in csv_reader:
            output.append([[*row[0].split(' '),*row[1].split(' '), *row[2].split(' ')]])
    return output

class Board():
    def __init__(self):
        self.lights_simple = [[False for i in range(1000)] for j in range(1000)]
        self.lights_complex = [[0 for i in range(1000)] for j in range(1000)]

    def execute_instruction(self, instruction):
        if instruction[0] == 'toggle':
            top_corner = [int(instruction[1]), int(instruction[2])]
            bottom_corner = [int(instruction[4]), int(instruction[5])]
            set = None
        else:
            top_corner = [int(instruction[2]), int(instruction[3])]
            bottom_corner = [int(instruction[5]), int(instruction[6])]
            if instruction[1] == 'on':
                set = True
            else:
                set = False
        self.set_lights_simple(top_corner, bottom_corner, set)
        self.set_lights_complex(top_corner, bottom_corner, set)

    def set_lights_simple(self, top_corner, bottom_corner, set):
        for i in range(top_corner[1], bottom_corner[1] + 1):
            for j in range(top_corner[0], bottom_corner[0] + 1):
                if set == None:
                    self.lights_simple[j][i] = not self.lights_simple[j][i]
                else:
                    self.lights_simple[j][i] = set

    def set_lights_complex(self, top_corner, bottom_corner, set):
        for i in range(top_corner[1], bottom_corner[1] + 1):
            for j in range(top_corner[0], bottom_corner[0] + 1):
                if set == None:
                    self.lights_complex[j][i] += 2
                elif set:
                    self.lights_complex[j][i] += 1
                else:
                    if self.lights_complex[j][i] != 0:
                        self.lights_complex[j][i] -= 1
                    

if __name__ == '__main__':
    instructions = import_data(LOCATION)

    light = Board()
    
    for instruction in instructions:
        light.execute_instruction(instruction[0])
    
    on = 0
    brightness = 0
    for row in light.lights_simple:
        on += sum(row)
    for row in light.lights_complex:
        brightness += sum(row)

    print(on, brightness)
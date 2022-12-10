import csv

LOCATION = 'day10_input.csv'

def import_data(location):
    output = []
    with open(location) as f:
        csv_reader = csv.reader(f)
        for row in csv_reader:
            output.append(row[0].split(' '))
    return output

class Computer():
    def __init__(self):
        self.X = 1
        self.cycle_value = []
    
    def complete_cycle(self, instruction):
        if instruction[0] == 'noop':
            self.cycle_value.append(self.X)
        else:
            for i in range(2):
                self.cycle_value.append(self.X)
            self.X += int(instruction[1])
        
def draw_screen(comp):
    screen = [*'.'*40], [*'.'*40], [*'.'*40], [*'.'*40], [*'.'*40], [*'.'*40]
    for cycle_less_one, sprite_position in enumerate(comp.cycle_value):
        draw_position = (cycle_less_one) % 40
        screen_position = (cycle_less_one + 1) // 40
        if abs(sprite_position - draw_position) <= 1:
            screen[screen_position][draw_position] = '#'
    return screen

if __name__ == '__main__':
    instructions = import_data(LOCATION)

    comp = Computer()

    for instruction in instructions:
        comp.complete_cycle(instruction)

    print((comp.cycle_value[19]*20) + (comp.cycle_value[59]*60) + (comp.cycle_value[99]*100) + (comp.cycle_value[139]*140) + (comp.cycle_value[179]*180) + (comp.cycle_value[219]*220))

    screen = draw_screen(comp)
    for row in screen:
        print(row)

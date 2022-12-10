import csv

LOCATION = 'day2_input.csv'

def import_data(location):
    output = []
    with open(location) as f:
        csv_reader = csv.reader(f)
        for row in csv_reader:
            output.append(list(map(int, row[0].split('x'))))
    return output

def calc_total_area_ribbon(present_sizes):
    area = 0
    ribbon = 0
    for present_size in present_sizes:
        area += 2 * present_size[0] * present_size[1] + 2 * present_size[1] * present_size[2] + 2 * present_size[2] * present_size[0]
        area += present_size[0] * present_size[1] * present_size[2] / max(present_size)

        ribbon += 2 * present_size[0] + 2 * present_size[1] + 2 * present_size[2] - 2 * max(present_size)
        ribbon += present_size[0] * present_size[1] * present_size[2]
    
    return area, ribbon

if __name__ == '__main__':
    present_sizes = import_data(LOCATION)
    area, ribbon = calc_total_area_ribbon(present_sizes)

    print(area, ribbon)
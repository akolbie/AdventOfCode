import csv

LOCATION = 'day8_input.csv'

def import_data(location):
    forrest = []
    with open(location) as f:
        csv_reader = csv.reader(f)
        for row in csv_reader:
            forrest.append(list(map(int, list(row[0]))))
    
    return forrest

def check_forrest(forrest):
    tally = 0
    for i, row in enumerate(forrest):
        for j, tree in enumerate(row):
            if i == 0 or j == 0 or i == len(forrest) - 1 or j == len(row) - 1:
                tally += 1
            else:
                if check_row(row, tree, j):
                    tally += 1
                    continue
                if check_row([row[j] for row in forrest], tree, i):
                    tally += 1                
    return tally


def check_row(row, tree, index):
    visible1 = True
    visible2 = True
    for i in row[:index]:
        if i >= tree:
            visible1 = False
    for i in row[index + 1:]:
        if i >= tree:
            visible2 = False
    return visible1 or visible2


def check_best_view(forrest):
    max_vis = 0
    for i, row in enumerate(forrest):
        for j, tree in enumerate(row):
            if i == 0 or j == 0 or i == len(forrest) - 1 or j == len(row) - 1:
                continue
            else:
                col = [row[j] for row in forrest]
                vis = find_vis(row, col, j, i)
                max_vis = max(max_vis, vis)
    return max_vis

def find_vis(row, col, row_index, col_index):
    total = 0
    tally = 0
    tree = row[row_index]

    for i in row[row_index + 1:]:
        if i >= tree:
            break
        tally += 1

    total += tally
    tally = 0

    for i in row[:row_index: -1]:
        if i >= tree:
            break
        tally += 1

    total *= tally
    tally = 0

    for i in col[col_index + 1:]:
        if i >= tree:
            break
        tally += 1
    
    total *= tally
    tally = 0

    for i in col[:col_index: -1]:
        if i >= tree:
            break
        tally += 1
    total *= tally

    return total

if __name__ == '__main__':
    forrest = import_data(LOCATION)
    tally = check_forrest(forrest)
    view = check_best_view(forrest)
    
    print(tally)
    print(view)
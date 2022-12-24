import csv

LOCATION = 'day12_input.csv'
JUMP_HEIGHT = 1
POSSIBLE_MOVES = [1, 0], [-1, 0], [0, 1], [0, -1]

def import_data(location):
    data = []
    with open(location) as f:
        csv_reader = csv.reader(f)
        for row in csv_reader:
            data.append(row[0])
    return data

def find_key_locations(height_map):
    for row_index, row in enumerate(height_map):
        if 'S' in row and 'E' in row:
            start_location = [row_index, row.index('S')]
            end_location = [row_index, row.index('E')]
            height_map[row_index] = row[ :row.index('S')] + 'a' + row[row.index('S') + 1: row.index('E') ] + 'z' + row[row.index('E') + 1: ]
        elif 'S' in row:
            start_location = [row_index, row.index('S')]
            height_map[row_index] = row[ :row.index('S')] + 'a' + row[row.index('S') + 1: ]
        elif 'E' in row:
            end_location = [row_index, row.index('E')]
            height_map[row_index] = row[ :row.index('E')] + 'z' + row[row.index('E') + 1: ]
    return start_location, end_location, height_map[:]

def get_possible_moves(height_map, loc, pos_height):
    moves = []
    for move in POSSIBLE_MOVES:
        move_loc = [loc[0] + move[0], loc[1] + move[1]]
        try:
            move_height = height_map[move_loc[0]][move_loc[1]]
        except:
            continue
        if move_loc[0] < 0 or move_loc[1] < 0:
            continue
        if abs(ord(move_height) - ord(pos_height)) == 1 or ord(move_height) - ord(pos_height) == 0:
            moves.append(move_loc)

    return moves

def breadth_first_search(height_map, start_location, end_location):
    explored = []
    que = [start_location]
    solution_found = False
    while True:
        loc = que.pop(0)
        pos_height = height_map[loc[0]][loc[1]]

        moves = get_possible_moves(height_map, loc, pos_height)

        for move in moves:
            if move == end_location:
                solution_found = True
                break
            elif move in explored or move in que:
                continue
            else:
                que.append(move)
        if solution_found:
            break
        explored.append(loc)

    moves = [end_location]

    while True:
        open_moves = get_possible_moves(height_map, moves[-1], height_map[moves[-1][0]][moves[-1][1]])
        min_index = len(explored)
        for move in open_moves:
            if move == start_location:
                moves.append(start_location)
                break
            if move in explored:
                min_index = min(min_index, explored.index(move))
        if start_location in moves:
            break
        moves.append(explored[min_index])
    
    return moves


if __name__ == '__main__':
    data = import_data(LOCATION)
    start_loc, end_loc, height_map = find_key_locations(data)
    moves = breadth_first_search(height_map, start_loc, end_loc)

    print(len(moves))
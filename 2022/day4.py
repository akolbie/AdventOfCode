import csv

LOCATION = 'day4_input.csv'

def get_data(location):
    with open(location) as f:
        output = []
        csv_reader = csv.reader(f)
        for row in csv_reader:
            output.append(row)
    return output

def check_complete_overlap_pair(set_one, set_two):
    set_one = [int(set_one[0]), int(set_one[1])]
    set_two = [int(set_two[0]), int(set_two[1])]
    
    if set_one[0] == set_two[0] or set_one[1] == set_two[1]: #if either beginning or ending values match, then one must contain the other 
        return 1
    elif set_one[0] > set_two[0]: #inital value of set to is lower than set one
        set_one, set_two = set_two, set_one
    
    if set_one[1] > set_two[1]:
        return 1
    return 0

def check_semi_overlap_pair(set_one, set_two):
    set_one = [int(set_one[0]), int(set_one[1])]
    set_two = [int(set_two[0]), int(set_two[1])]

    if set_one[0] in set_two or set_one[1] in set_two:
        return 1
    elif set_one[0] > set_two[0]: #inital value of set to is lower than set one
        set_one, set_two = set_two, set_one

    if set_one[1] >= set_two[0]:
        return 1
    return 0



if __name__ == '__main__':
    pairs = get_data(LOCATION)
    tally1 = 0
    tally2 = 0
    for pair in pairs:
        tally1 += check_complete_overlap_pair(pair[0].split('-'),pair[1].split('-'))
        tally2 += check_semi_overlap_pair(pair[0].split('-'),pair[1].split('-'))

    print(tally1, tally2)
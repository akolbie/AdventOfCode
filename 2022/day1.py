import csv

LOCATION = "day1_input.csv"

# def get_data():
#     highest = 0
#     tally = 0
#     with open("day_1_1_input.csv") as f:
#         csv_reader = csv.reader(f)
#         for line in csv_reader:
            

def find_highest(data):
    highest = 0
    tally = 0
    for row in data:
        if row == []:
            if tally > highest:
                highest = tally
            tally = 0
        else:
            tally += int(row[0])
    return highest

def get_top_three(location):
    first = 0
    second = 0
    third = 0
    tally = 0
    with open(location) as f:
        csv_reader = csv.reader(f)
        for row in csv_reader:
            if row == []:
                if tally > first:
                    first, second, third = tally, first, second
                elif tally > second:
                    second, third = tally, second
                elif tally > third:
                    third = tally
                tally = 0
            else:
                tally += int(row[0])
    return first + second + third


if __name__ == "__main__":
    print(get_top_three(LOCATION))
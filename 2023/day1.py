import csv

file = "day1.csv"
file = 'day1_bommel.csv'

words = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

with open(file) as f:
    data = []
    csv_reader = csv.reader(f)
    for line in csv_reader:
        data.append(line[0])

output = 0
for line in data:
    row_data = []
    for loc, char in enumerate(line):
        try:
           row_data.append(int(char))
        except:
            for word_value, word in enumerate(words):
                if word == line[loc:loc + len(word)]:
                    row_data.append(word_value + 1)


    output += row_data[0] * 10 + row_data[-1]

print(output)
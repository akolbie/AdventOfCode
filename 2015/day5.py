import csv

LOCATION = 'day5_input.csv'
C3_LIST = ['ab', 'cd', 'pq', 'xy']
VOWELS = ['a', 'e', 'i', 'o', 'u']

def import_data(location):
    output = []
    with open(location) as f:
        csv_reader = csv.reader(f)
        for row in csv_reader:
            output.append(row[0])
    return output

def check_word(word):
    c2 = False
    vowels = 0

    for c3_list_item in C3_LIST:
        if c3_list_item in word:
            return 0
    
    for char_index, character in enumerate(word):
        if char_index == 0:
            continue
        if character == word[char_index - 1]:
            c2 = True
            break

    if not c2:
        return 0

    for vowel in VOWELS:
        vowels += word.count(vowel)
    
    if vowels >= 3:
        return 1
    return 0

def check_word_extra_nice(word):
    c2 = False

    for char_index, character in enumerate(word):
        if char_index == 0 or char_index == 1:
            continue
        if character == word[char_index - 2]:
            c2 = True
            break
    
    if not c2:
        return 0

    for char_index, character in enumerate(word):
        if char_index == len(word) - 3:
            return 0 
        if word[char_index:char_index + 2] in word[char_index + 2:]:
            return 1
    return 0


if __name__ == '__main__':
    data = import_data(LOCATION)
    tally1, tally2 = 0, 0

    for word in data:
        tally1 += check_word(word)
        tally2 += check_word_extra_nice(word)

    print(tally1, tally2)
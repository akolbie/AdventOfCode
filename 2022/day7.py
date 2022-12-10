import csv

LOCATION = 'day7_input.csv'
FILE_SYSTEM_SIZE = 70000000
REQUIRED_SPACE = 30000000


class File():
    def __init__(self, file_name, folder, size):
        self.name = file_name
        self.size = size
        self.folder = folder

class Folder():
    def __init__(self, name, parent_folder, contents):
        self.folder_name = name
        self.parent_folder = parent_folder
        self.contents = contents

    def calc_size(self):
        self.size = 0
        for item in self.contents:
            if type(item) == type(self): # its a folder
                self.size += item.get_size()
            else:
                self.size += item.size

    def get_size(self):
        if not hasattr(self, 'size'):
            self.calc_size()
        return self.size

def import_data(location):
    data = []
    with open(location) as f:
        csv_reader = csv.reader(f)
        for row in csv_reader:
            data.append(row[0])
    return data

def navigation(data, folders):
    current_directory = folders[0]
    for row in data:
        if data.index(row) == 0:
            next
        if row[0] == '$': #instruction
            if row[2:4] == "cd": #goto directory
                if row[5:] == '..': #go up a level
                    current_directory = current_directory.parent_folder
                else:
                    folders.append(Folder(row[4:], current_directory, []))
                    current_directory.contents.append(folders[-1])
                    current_directory = folders[-1]
            else: #list contents
                pass
        else:
            if row[:3] != 'dir': #file
                temp = row.split(' ')
                current_directory.contents.append(File(temp[1], current_directory, int(temp[0])))
    return folders

def calc_sizes(folders):
    tally = 0
    folders[0].get_size()
    for folder in folders:
        if folder.size <= 100000:
            tally += folder.size
    return tally

def find_closest_folder_size(folders, space_to_free_up):
    min_folder_size = folders[0].size
    for folder in folders:
        if folder.size >= space_to_free_up:
            if folder.size < min_folder_size:
                min_folder_size = folder.size
    return min_folder_size

if __name__ == '__main__':
    folders = navigation(import_data(LOCATION),[Folder('Root', None, [])])
    tally = calc_sizes(folders)
    print(tally)
    space_to_free_up = REQUIRED_SPACE - (FILE_SYSTEM_SIZE - folders[0].size)
    print(find_closest_folder_size(folders, space_to_free_up))

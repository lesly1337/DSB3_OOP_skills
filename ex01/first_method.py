class Research:
    def file_reader(self):
        with open("../ex00/data.csv", "r") as fr:
            lines = fr.readlines()
            return lines
                
if __name__ == '__main__':
    reader = Research()
    list_of_lines = reader.file_reader()
    for line in list_of_lines:
        print(line.strip())

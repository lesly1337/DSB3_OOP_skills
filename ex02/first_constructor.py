import sys
import os

class Research:
    def __init__(self, filename):
        if (os.path.exists(filename)):
            self.file_name = filename
        else:
            raise ValueError("No such file is found")

    def file_reader(self):
        with open(self.file_name, "r") as fr:
            lines = fr.readlines()
            for index, line in enumerate(lines):
                line = line.strip()
                words = line.split(',')#['head','tail']
                if len(words) != 2:
                    raise ValueError("Wrong structure")
                for word in words:
                    if words[0] == words[1]:
                        raise ValueError("Not possible")
                    if word != '0' and word != '1' and index != 0:
                        raise ValueError("Wrong structure")
            return lines
        
        
if __name__ == '__main__':
    if (len(sys.argv) == 2):
        research = Research(sys.argv[1]) #получаем название файла
        list_of_lines = research.file_reader() #["head,tail/n", "0,1/n", ...
        for line in list_of_lines:
            print(line.strip())
    else:
            raise ValueError("Wrong number of arguments!")
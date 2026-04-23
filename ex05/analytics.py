import sys
import os
from random import randint

class Research:
    def __init__(self, filename):
        if (os.path.exists(filename)):
            self.file_name = filename
        else:
            raise ValueError("No such file is found")

    def file_reader(self, has_header=True):
        with open(self.file_name, "r") as fr:
            lines = fr.readlines()
            if lines[0].strip() != "head,tail" and has_header == True:
                has_header = False
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
            if has_header:
                lines.pop(0)
            return lines

    class Calculations:

        def __init__(self, data):
            self.data = data

        def counts(self):
            counts_list = [0,0]
            for results in self.data:
                if results[0] == '1':
                    counts_list[0] = counts_list[0] + 1
                else:
                    counts_list[1] = counts_list[1] + 1
            return counts_list
        def fractions(self, counts_list):
            fractions_list = [0,0]
            fractions_list[0] = counts_list[0]/ (counts_list[0] + counts_list[1] )
            fractions_list[1] = counts_list[1]/ (counts_list[0] + counts_list[1] )
            return fractions_list  

class Analytics(Research.Calculations):

    def __init__(self, data):
        super().__init__(data)

    def predict_random(self, steps_count):
        result_list = []
        for i in range (steps_count):
            pos = randint(0, len(self.data) - 1)
            result_list.append(self.data[pos].strip())
        return result_list
        

    def predict_last(self):
        return self.data[-1].split(',')

    def save_file(self, data, file_name, extension):
        with open(file_name + "." + extension, "w") as fw:
            fw.write(data)
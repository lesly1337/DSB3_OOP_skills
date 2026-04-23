import sys
import os

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
        def counts(self, file_reader_data):
            counts_list = [0,0]
            for results in file_reader_data:
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


        
        
if __name__ == '__main__':
    if (len(sys.argv) == 2):
        research = Research(sys.argv[1])
        calc = research.Calculations()
        list_of_lines = research.file_reader()
        print("[", end = "") 
        for index, line in enumerate(list_of_lines):
            print(f"[{line.strip()}]", end = "")
            if ( index != len(list_of_lines) - 1 ):
                print(", ", end = "")
        print("]") 
        print(f"{calc.counts(list_of_lines)[0]} {calc.counts(list_of_lines)[1]}")
        print(f"{calc.fractions(calc.counts(list_of_lines))[0]:.{3}f} {calc.fractions(calc.counts(list_of_lines))[1]:.{3}f}")
    else:
            raise ValueError("Wrong number of arguments!")
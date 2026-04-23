class Must_Read:
    with open("data.csv", "r") as fr:
        lines = fr.readlines()
        for line in lines:
            print(line.strip())
if __name__ == '__main__':
    Must_Read()

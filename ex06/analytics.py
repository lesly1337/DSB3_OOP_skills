import sys
import os
import logging
import config
import requests
from random import randint
class Research:
    logging.basicConfig(level=logging.INFO, filename="analytics.log", format='%(asctime)s %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

    def send_message_telegram(self, text):
        logging.info("Sending message in telegram")
        send_url = f"{config.API_url}/sendMessage"
        payload = {
                'chat_id': config.CHAT_ID,
                'text': text
            }
        response = requests.post(send_url, json=payload)
        response.raise_for_status()
        return response.json()

    def __init__(self, filename):
        logging.info("Research object has been created")
        if (os.path.exists(filename)):
            self.file_name = filename
        else:
            self.send_message_telegram("The report hasn't been created due to an error.")
            raise ValueError("No such file is found")
    
    def file_reader(self, has_header=True):
        logging.info("Reading our file")
        with open(self.file_name, "r") as fr:
            lines = fr.readlines()
            if lines[0].strip() != "head,tail" and has_header == True:
                has_header = False
            for index, line in enumerate(lines):
                line = line.strip()
                words = line.split(',')#['head','tail']
                if len(words) != 2:
                    self.send_message_telegram("The report hasn't been created due to an error.")
                    raise ValueError("Wrong structure")
                for word in words:
                    if words[0] == words[1]:
                        self.send_message_telegram("The report hasn't been created due to an error.")
                        raise ValueError("Not possible")
                    if word != '0' and word != '1' and index != 0:
                        self.send_message_telegram("The report hasn't been created due to an error.")
                        raise ValueError("Wrong structure")
            if has_header:
                lines.pop(0)
            return lines

    class Calculations:

        def __init__(self, data):
            logging.info("Calculation object has been created")
            self.data = data

        def counts(self):
            logging.info("Counting heads and tails")
            counts_list = [0,0]
            for results in self.data:
                if results[0] == '1':
                    counts_list[0] = counts_list[0] + 1
                else:
                    counts_list[1] = counts_list[1] + 1
            return counts_list
        def fractions(self, counts_list):
            logging.info("Fractions of heads and tails")
            fractions_list = [0,0]
            fractions_list[0] = counts_list[0]/ (counts_list[0] + counts_list[1] )
            fractions_list[1] = counts_list[1]/ (counts_list[0] + counts_list[1] )
            return fractions_list  

class Analytics(Research.Calculations):

    def __init__(self, data):
        logging.info("Analytics object has been created")
        super().__init__(data)

    def predict_random(self, steps_count):
        logging.info("Taking random predictions")
        result_list = []
        for i in range (steps_count):
            pos = randint(0, len(self.data) - 1)
            result_list.append(self.data[pos].strip())
        return result_list
        

    def predict_last(self):
        logging.info("Taking last prediction")
        return self.data[-1].split(',')

    def save_file(self, data, file_name, extension):
        logging.info("Saving file")
        with open(file_name + "." + extension, "w") as fw:
            fw.write(data)
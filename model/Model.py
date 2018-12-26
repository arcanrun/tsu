from interfaces.IModel import IModel
import re
from datetime import datetime


class Model(IModel):
    def __init__(self, data_base=None):
        self.data_base = data_base
        self.subscribers = []

    def subscribe(self, observer):
        self.subscribers.append(observer)

    def notify_subscribers(self, msg):
        for i in self.subscribers:
            i.update(msg)


    def add(self, center_name, file_path):
        pattern_time_key = r'^(([01]\d|2[0-3]):([0-5]\d)|24:00)$'
        self.time = ''
        self.body = ''

        # search last line to make EOF
        file_for_last_line = open(file_path)
        last_line = Model.findLastLine(file_for_last_line)
        file_for_last_line.close()
        # =============================

        file = open(file_path)
        try:
            for line in file:

                isKey = line.split(' ')[0]
                if re.match(pattern_time_key, isKey):
                    if len(self.time) != 0:
                        self.data_base.add_message(center_name, self.time, self.body)
                        self.time = ''
                        self.body = ''

                    self.time = isKey
                    self.body += line[len(isKey):]
                else:
                    self.body += line


                if last_line == line:
                    self.data_base.add_message(center_name, self.time, self.body)
                self.notify_subscribers('[New reports has been added!]')
        except:
                self.notify_subscribers('[Some errors occured while adding msg!]')



        file.close()



    def show_all(self):
        res = self.data_base.show_all()

        return res

    def show_by_center(self, center_name):
        res = self.data_base.find_by_key(center_name)

        return res

    def list_centers(self):
        res = self.data_base.get_keys()
        return res

    @staticmethod
    def findLastLine(file):
        for line in file:
            pass
        last_line = line
        return last_line

    def show_message_by_time(self, center_name, time):
        center = self.show_by_center(center_name)
        self.notify_subscribers('[Name not found!]')
        
        arr_time = time.split('-')
        first_time = arr_time[0]
        last_time = arr_time[1]

        # converter to time object:
        first_time = datetime.strptime(first_time, '%H:%M').time()
        last_time = datetime.strptime(last_time, '%H:%M').time()
        # print(first_time, last_time)



        if first_time > last_time:
            temp = first_time
            first_time = last_time
            last_time = temp


        output = {}
        for key, val in center.items():
            keyTime = datetime.strptime(key, '%H:%M').time()
            if keyTime >= first_time and keyTime <= last_time:
                output[key] = val

        return output
    def show_by_phrase(self, center_name, phrase):
        center = self.show_by_center(center_name)

        output = {}
        for k,v in center.items():
            if phrase in v:
                output[k] = v


        return output




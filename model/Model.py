from interfaces.IModel import IModel
import re

class Model(IModel):
    def __init__(self, data_base=None):
        self.data_base = data_base

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



        file.close()



    def show_all(self):
        res = self.data_base.show_all()
        # for i in res:
        #     print(i)
        return res

    @staticmethod
    def findLastLine(file):
        for line in file:
            pass
        last_line = line
        return last_line




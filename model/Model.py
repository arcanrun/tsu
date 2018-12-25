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
        # print(len(res))
        # for k,v in res.items():
        #     print('\t \t=====',k,'======')
        #     if type(v).__name__ == 'dict':
        #         for k2,v2 in v.items():
        #             print('\t{} : {}'.format(k2,v2))

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

    def show_message_by_time(self):
        pass

    def show_by_phrase(self):
        pass



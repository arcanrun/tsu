from model.db.interfaces.IDb import IDb
import shelve


class Db(IDb):
    def add_message(self, center_name, time, body):

        db = shelve.open(center_name)
        db[time] = body.strip()

        db.close()

    def show_all(self):
        all_data = {}
        db = shelve.open('south')

        for k, v in db.items():

            print(k,v)
            all_data[k] = v

        return all_data


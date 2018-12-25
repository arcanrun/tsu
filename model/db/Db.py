from model.db.interfaces.IDb import IDb
import shelve


class Db(IDb):
    def __init__(self):
        self.dbName = 'shelveBd'

    def add_message(self, center_name, time, body):
        db = shelve.open(self.dbName)
        if not center_name in db:
            db[center_name] = {}
            temp = db[center_name]
            temp[time] = body.strip()
            db[center_name] = temp
        else:
            temp = db[center_name]

            temp[time] = body.strip()
            db[center_name] = temp
            # print(db[center_name])

        db.close()

    def show_all(self):

        db = shelve.open(self.dbName)
        res = Db.deepCicrle(db)
        # print(res['south'])
        return res

    def find_by_key(self, key):
        db = shelve.open(self.dbName)
        return db[key]
    def get_keys(self):
        db = shelve.open(self.dbName)
        res = {'length': len(list(db.keys())), 'keys': list(db.keys())}
        return res

    @staticmethod
    def deepCicrle(dict):
        all_data = {}
        # inner_data = {}
        for k,v in dict.items():
            all_data[k] = v

        return all_data
            # if type(v).__name__ == 'dict':
            #     print(k, v)
            #
            #     for innK, innV in v.items():
            #         # print(k,innK)
            #         inner_data[innK] = innV
            #
            #     all_data[k] = inner_data
            # else:
            #     all_data[k] = v


        return all_data



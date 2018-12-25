import abc


class IDb(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def add_message(self, center_name, time, body):
        pass

    @abc.abstractmethod
    def show_all(self):
       pass

    @abc.abstractmethod
    def find_by_key(self, key):
        pass

    @abc.abstractmethod
    def get_keys(self):
        pass
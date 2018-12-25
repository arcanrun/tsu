import abc


class IDb(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def add_message(self, center_name, time, body):
        pass
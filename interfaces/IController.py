import abc


class IController(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def add_report(self, center_name, file_path):
        pass
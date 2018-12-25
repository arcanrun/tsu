import abc


class IModel(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def add(self, center_name, file_path):
        pass

    @abc.abstractmethod
    def show_all(self):
        pass
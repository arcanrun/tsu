import abc


class IModel(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def add(self, center_name, file_path):
        pass

    @abc.abstractmethod
    def show_all(self):
        pass

    @abc.abstractmethod
    def show_by_center(self, center_name):
        pass

    @abc.abstractmethod
    def list_centers(self):
        pass

    @abc.abstractmethod
    def show_message_by_time(self):
        pass

    @abc.abstractmethod
    def show_by_phrase(self):
        pass
import abc


class IModel(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def subscribe(self, observer):
        pass

    @abc.abstractmethod
    def notify_subscribers(self, msg):
        pass

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
    def show_message_by_time(self, center_name, time):
        pass

    @abc.abstractmethod
    def show_by_phrase(self, center_name, phrase):
        pass


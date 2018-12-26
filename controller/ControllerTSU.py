from interfaces.IController import IController

class ControllerTSU(IController):
    def __init__(self, model):
        self.model = model

    def add_report(self, center_name, file_path):
        self.model.add(center_name, file_path)

    def show_message_by_time(self, center_name, time):
        return self.model.show_message_by_time(center_name, time)


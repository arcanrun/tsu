from  interfaces.IObserver import IObserver

class CLIView(IObserver):
    def __init__(self, model, controller):
        self.model = model
        self.controller = controller

    def update(self, msg):
        print('[SYSTEM MESSAGE]:'.format(msg))

    def main_menu(self):
        print(
            """
            1. Add report
            2. Show all reports
            3. Search by time
            4. Exit
            """
        )
        n = input()
        dict = {
            '1': self.add_report,
            '2': self.show_all_reports,
            '3': self.show_message_by_time,


        }
        dict.get(n, self.main_menu)()

    def add_report(self):
        try:
            print('Введите отправителя:')
            center_name = input()
            print('Введите путь к файлу')
            file_path = input()
            self.controller.add_report(center_name, file_path)
        except:
            print('[SYSTEM MESSAGE]:[Errors while adding new report!]')
            self.main_menu()

    def show_all_reports(self):
        res = self.model.show_all()
        centers_common = self.model.list_centers()

        if len(res) == 0:
            print('No reports!')

        print('| Количество подразделений: {}'.format( centers_common['length']) )
        print('| Подразделения:')
        for i in centers_common['keys']:
            print('--',i)
        print()
        for k,v in res.items():
            print('=====',k,'======')
            if type(v).__name__ == 'dict':
                for k2,v2 in v.items():
                    print('\t{} : {}'.format(k2,v2))

        self.main_menu()

    def show_message_by_time(self):
        print('Введите подразделение:')
        center_name = input()
        print('Введите промежуток времени:')
        time = input()
        res = self.controller.show_message_by_time(center_name, time)

        for k,v in res.items():
            print('{}:{}'.format(k,v))
        self.main_menu()

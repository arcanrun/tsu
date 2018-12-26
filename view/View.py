from  interfaces.IObserver import IObserver
import sys


class CLIView(IObserver):
    def __init__(self, model, controller):
        self.model = model
        self.controller = controller

    def update(self, msg):
        print('[SYSTEM MESSAGE]:'.format(msg))

    def main_menu(self):
        print(
            """
            1. Добавить вводную
            2. Показать все вводные
            3. Поиск по времени
            4. Список всех подразделений
            5. Вводные по подразделению
            6. Поиск по фразе
            7. Exit
            """
        )
        n = input()
        dict = {
            '1': self.add_report,
            '2': self.show_all_reports,
            '3': self.show_message_by_time,
            '4': self.display_list_centers,
            '5': self.show_by_center,
            '6': self.show_by_phrase,
            '7': self.exit


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
        arr_centers = self.show_list_centers()
        print('Введите подразделение:')

        center_name = ''
        try:
            n = int(input()) - 1
            center_name = arr_centers[n]
        except:
            print(['Input Error!'])
            self.main_menu()
        print('Введите промежуток времени:')
        time = input()
        try:
            res = self.controller.show_message_by_time(center_name, time)
        except:
            print('[Erroe while fetchng!]')
            self.main_menu()
        CLIView.showCentersMessages(res)
        self.main_menu()


    def show_by_center(self):
        centers_arr = self.show_list_centers()
        try:
            n = int(input())-1
        except:
            print("[Input error]")
            self.main_menu()
        center = self.model.show_by_center(centers_arr[n])
        CLIView.showCentersMessages(center)
        self.main_menu()

    def show_list_centers(self):

        res = self.model.list_centers()

        if res['length'] == 0 or len(res) == 0:
            print('Нет вводных')

        print('Всего: {}'.format(res['length']))
        counter = 1
        for i in res['keys']:
            print('{}) {}'.format(counter,i))
            counter += 1
        return res['keys']

    def display_list_centers(self):
        res = self.model.list_centers()

        if res['length'] == 0 or len(res) == 0:
            print('Нет вводных')

        print('Всего: {}'.format(res['length']))
        counter = 1
        for i in res['keys']:
            print('{}) {}'.format(counter, i))
            counter += 1
        self.main_menu()

    def show_by_phrase(self):
        print("Выбирите подразделние:")
        arr_centers = self.show_list_centers()
        center_name = ''
        try:
            n = int(input())-1
            center_name = arr_centers[n]
        except:
            print(['Input error!'])
            self.main_menu()
        print('Введите фразу:')
        phrase = input()
        res = self.model.show_by_phrase(center_name, phrase)
        CLIView.showCentersMessages(res)
        self.main_menu()


    def exit(self):
        sys.exit('')

    @staticmethod
    def showCentersMessages(dict):
        if(len(dict) == 0):
            print('[Nothing found!]')
            return False
        for k,v in dict.items():
            print('{} : {}'.format(k,v))
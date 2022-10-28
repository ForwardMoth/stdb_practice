import sys

sys.path.append('tables')

from project_config import *
from dbconnection import *
from tables.people_table import *
from tables.phones_table import *
from tables.groups_table import *

class Main:
    config = ProjectConfig()
    connection = DbConnection(config)

    def __init__(self):
        self.person_id = None
        self.person_obj = None
        self.phone_id = None
        self.phone_obj = None
        DbTable.dbconn = self.connection
        return

    def db_init(self):
        peopleTable = PeopleTable()
        phonesTable = PhonesTable()
        peopleTable.create()
        phonesTable.create()
        # Добавление новой таблицы
        groupsTable = GroupsTable()
        groupsTable.create()
        return

    def db_insert_somethings(self):
        pt = PeopleTable()
        pht = PhonesTable()
        gt = GroupsTable()
        pt.insert_one(["Test", "Test", "Test"])
        pt.insert_one(["Test2", "Test2", "Test2"])
        pt.insert_one(["Test3", "Test3", "Test3"])
        pht.insert_one([1, "123"])
        pht.insert_one([2, "123"])
        pht.insert_one([3, "123"])
        # Добавление новой таблицы
        gt.insert_one(["C19-702", "ИАСБ", "75"])
        gt.insert_one(["C19-712", "ИАСБ", "75"])
        gt.insert_one(["C19-711", "ЭКБЕЗ", "75"])

    def db_drop(self):
        pht = PhonesTable()
        pt = PeopleTable()
        gt = GroupsTable()
        pht.drop()
        gt.drop()
        pt.drop()
        return

    def show_main_menu(self):
        menu = """Добро пожаловать!
Основное меню (выберите цифру в соответствии с необходимым действием):
    1 - просмотр людей;
    2 - просмотр групп;
    8 - сброс и инициализация таблиц;
    9 - выход."""
        print(menu)
        return

    def read_next_step(self):
        return input("=> ").strip()

    def db_drop_init(self):
        self.db_drop()
        self.db_init()
        self.db_insert_somethings()
        print("Таблицы созданы заново!")
        return "0"

    def show_people(self):
        self.person_id = -1
        menu = """Просмотр списка людей!
№\tФамилия\tИмя\tОтчество"""
        print(menu)
        lst = PeopleTable().all()
        for i in lst:
            print(str(i[0]) + "\t" + str(i[1]) + "\t" + str(i[2]) + "\t" + str(i[3]))
        return

    # Форма ввода имени
    def form_first_name(self):
        while True:
            first_name = input("Введите имя (1 - отмена): ").strip()
            if first_name == "1":
                return
            if len(first_name.strip()) == 0:
                print("Имя не может быть пустым!")
            elif len(first_name.strip()) > 32:
                print("Имя имеет недопустимую длину!")
            else:
                return first_name
    # Форма ввода фамилии
    def form_last_name(self):
        while True:
            last_name = input("Введите фамилию (1 - отмена): ").strip()
            if last_name == "1":
                return
            if len(last_name.strip()) == 0:
                print("Фамилия не может быть пустой!")
            elif len(last_name.strip()) > 32:
                print("Фамилия имеет недопустимую длину!")
            else:
                return last_name
    # Форма ввода отчества
    def form_second_name(self):
        while True:
            second_name = input("Введите отчество (1 - отмена): ").strip()
            if second_name == "1":
                return
            if len(second_name.strip()) == 0:
                print("Отчество не может быть пустым!")
            elif len(second_name.strip()) > 32:
                print("Отчество имеет недопустимую длину!")
            else:
                return second_name
    # Добавление человека
    def show_add_person(self):
        data = [self.form_last_name(), self.form_first_name(), self.form_second_name()]
        # Проверяем элементы на пустоту (в случае отмены ввода)
        for i in data:
            if i is None:
                return "-1"
        PeopleTable().insert_one(data)
        return "-1"

    def find_phone_by_person(self):
        while True:
            num = input("Укажите номер строки, в которой записана интересующая Вас персона (0 - отмена): ")
            if num == "0":
                return "-1"
            if len(num.strip()) == 0:
                print("Пустая строка. Повторите ввод! ")
            # проверка на то, что строка состоит из цифр
            if not num.strip().isnumeric():
                print("Неверный данные. Повторите ввод! ")
            person = PeopleTable().find_by_position(int(num))
            if not person:
                print("Введено число, неудовлетворяющее количеству людей!")
            else:
                self.person_id = int(person[1])
                self.person_obj = person
                return "0"

    def show_phones_by_people(self):
        if self.person_id != -1:
            print("Выбран человек: " + self.person_obj[2] + " " + self.person_obj[0] + " " + self.person_obj[3])
            lst = PhonesTable().all_by_person_id(self.person_id)
            # Проверяем есть ли в таблице номера телефонов для человека
            if len(lst) == 0:
                print("Нет телефонов")
            else:
                phone_show_text = """Просмотр списка телефонов!\n№\tТелефон"""
                print(phone_show_text)
                for i in range(len(lst)):
                    print(str(i + 1) + "\t" + lst[i][1])
        return

    # Форма ввода для телефона
    def phone_form(self):
        while True:
            phone = input("Введите номер телефона (1 - отмена): ").strip()
            if phone == "1":
                return
            elif len(phone.strip()) == 0:
                print("Телефон не может быть пустым! Введите телефон заново")
            elif len(phone.strip()) > 12:
                print("Телефон не может быть длиннее 12 символов! Введите телефон заново")
            else:
                return phone

    # Новая функция для добавление телефонов
    def add_phone(self):
        data = [self.person_id, self.phone_form()]
        PhonesTable().insert_one(data)
        return "-1"

    # Вспомогательная функция, которая находит нужный номер телефона человека
    def find_phone_by_id(self):
        num = -1
        while True:
            num = input("Укажите номер строки, в которой записан интересующий Вас номер телефона (0 - отмена): ")
            if len(num.strip()) == 0:
                print("Пустая строка. Повторите ввод! ")
            if num == "0":
                return "1"
            if not num.strip().isnumeric():
                print("Неверные данные. Повторите ввод! ")

            phone = PhonesTable().find_by_position(int(num), self.person_id)
            if not phone:
                print("Введено число, неудовлетворяющее количеству телефонов!")
            else:
                self.phone_id = int(phone[0])
                self.phone_obj = phone
                break

    # Новая функция для редактирования номера телефона
    def edit_phone(self):
        phone = self.phone_form()
        PhonesTable().update(phone, self.phone_obj[1])
        return "-1"

    # Новая функция для удаления номера телефона
    def delete_phone(self):
        PhonesTable().delete(self.phone_obj[1])
        return "-1"

    def show_phones_menu(self):
        menu = """Дальнейшие операции:
        0 - возврат в главное меню;
        1 - возврат в просмотр людей;
        3 - ? СОЗДАНИЕ ЧЕЛОВЕКА ?
        4 - не реализовано
        5 - ? ПРОСМОТР СПИСКА ТЕЛЕФОНОВ ?
        6 - добавление нового телефона (для выбранного человека);
        7 - редактирование номера телефона;
        8 - удаление телефона;
        9 - выход."""
        print(menu)
        return

    def phone_actions(self):
        code = "-1"
        if self.person_id == -1:
            code = self.find_phone_by_person()

        if code == "0":
            current_step = "-1"
            while True:
                if current_step == "-1":
                    self.show_phones_by_people()
                    self.show_phones_menu()
                    current_step = self.read_next_step()
                elif current_step == "3":
                    print("Не реализовано! ")
                    current_step = "-1"
                elif current_step == "4":
                    print("Не реализовано! ")
                    current_step = "-1"
                elif current_step == "5":
                    print("Не реализовано! ")
                    current_step = "-1"
                elif current_step == "6":
                    current_step = self.add_phone()
                elif current_step == "7":
                    self.find_phone_by_id()
                    current_step = self.edit_phone()
                elif current_step == "8":
                    self.find_phone_by_id()
                    current_step = self.delete_phone()
                elif current_step == "1":
                    return "-1"
                elif current_step == "0":
                    return "0"
                elif current_step == "9":
                    return "9"
                else:
                    print("Выбрано неверное значение! Повторите ввод!")
                    current_step = self.read_next_step()

        return "-1"

    def show_people_menu(self):
        menu = """Дальнейшие операции:
    0 - возврат в главное меню;
    3 - добавление нового человека;
    4 - удаление человека;
    5 - просмотр телефонов человека;
    6 - ВВОДИМ НОМЕР и потом смотрим номера человека, но у него нет этого номера(?);
    7 - вводим номер телефона, потом новый номер, потом номер человека, потом этого номера нет ???
    8 - требует ввести позицию телефона, потом позицию человека и выводит всю инфу о человеке ???
    9 - выход."""
        print(menu)
        return

    def people_actions(self):
        current_step = "-1"
        while True:
            if current_step == "-1":
                self.show_people()
                self.show_people_menu()
                current_step = self.read_next_step()
            elif current_step == "3":
                current_step = self.show_add_person()
            elif current_step == "4":
                print("Не реализовано! ")
                current_step = "-1"
            elif current_step == "5":
                current_step = self.phone_actions()
            elif current_step == "6":
                print("Не реализовано! ")
                current_step = "-1"
            elif current_step == "7":
                print("Не реализовано! ")
                current_step = "-1"
            elif current_step == "8":
                print("Не реализовано! ")
                current_step = "-1"
            elif current_step == "0":
                return "0"
            elif current_step == "9":
                return "9"
            else:
                print("Выбрано неверное значение! Повторите ввод!")
                current_step = self.read_next_step()

    def main_cycle(self):
        current_menu = "0"
        while current_menu != "9":
            if current_menu == "0":
                self.show_main_menu()
                current_menu = self.read_next_step()
            elif current_menu == "1":
                current_menu = self.people_actions()
            elif current_menu == "2":
                print("Не реализовано! ")
                current_menu = "0"
            elif current_menu == "8":
                current_menu = self.db_drop_init()
            else:
                print("Выбрано неверное значение! Повторите ввод!")
                current_menu = self.read_next_step()
        print("До свидания!")
        return


m = Main()
m.main_cycle()



#     def show_groups(self):
#         menu = """Просмотр списка групп!\nГруппа\tСпециальность\tКафедра"""
#         print(menu)
#         lst = GroupsTable().all()
#         print(lst)
#     #     lst = PeopleTable().all()
#     #     for i in lst:
#     #         # 0 - имя
#     #         # 1 - id
#     #         # 2 - Фамилия
#     #         # 3 - Отчество
#     #         print(str(i[0]) + "\t" + str(i[1]) + "\t" + str(i[2]) + "\t" + str(i[3]))
#     #     menu = """Дальнейшие операции:
#     # 0 - возврат в главное меню;
#     # 3 - добавление нового человека;
#     # 4 - удаление человека;
#     # 5 - просмотр телефонов человека;
#     # 6 - ВВОДИМ НОМЕР и потом смотрим номера человека, но у него нет этого номера(?);
#     # 7 - вводим номер телефона, потом новый номер, потом номер человека, потом этого номера нет ???
#     # 8 - требует ввести позицию телефона, потом позицию человека и выводит всю инфу о человеке ???
#     # 9 - выход."""
#     #     print(menu)
#     #     return
#
#
#





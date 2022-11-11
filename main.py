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
        self.group_obj = None
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

    def find_people_by_lastname(self):
        while True:
            l_name = input("Укажите фамилию человека, которого надо найти: (0 - отмена) ")
            if len(l_name.strip()) == 0:
               print("Пустая строка. Повторите ввод! ")

            if len(l_name.strip()) > 32:
               print("Слишком длинная фамилия. Повторите ввод! ")

            if l_name == "0":
               return "0"

            lastname = PeopleTable().find_by_last_name(l_name)

            if lastname is not None:
                self.person_id = lastname[0]
                self.person_obj = lastname
                print("Найдена запись: " + self.person_obj[2] + " " + self.person_obj[0] + " " + self.person_obj[3])
                return "0"
            else:
                print("Запись не найдена! Повторите ввод! ")

    def show_main_menu(self):
        menu = """Добро пожаловать!
Основное меню (выберите цифру в соответствии с необходимым действием):
    1 - просмотр людей;
    2 - просмотр групп;
    3 - поиск человека по фамилии;
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
        menu = """Просмотр списка людей!"""
        print(menu)
        columns = ["№", "Фамилия", "Имя", "Отчество"]
        self.formatted_print(columns)
        lst = PeopleTable().all()
        for i in range(len(lst)):
            a = list(lst[i])[1:]
            a.insert(0, i+1)
            self.formatted_print(a)
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
    def add_person(self):
        last_name = self.form_last_name()
        if last_name is None:
            return "-1"
        first_name = self.form_first_name()
        if first_name is None:
            return "-1"
        second_name = self.form_second_name()
        if second_name is None:
            return "-1"
        data = [last_name, first_name, second_name]
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
                phone_show_text = """Просмотр списка телефонов!"""
                print(phone_show_text)
                columns = ["№", "Телефон"]
                self.formatted_print(columns)
                for i in range(len(lst)):
                    a = [i+1, lst[i][1]]
                    self.formatted_print(a)
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
                return "-1"
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
        if phone is not None:
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
        6 - добавление нового телефона (для выбранного человека); 
        7 - редактирование номера телефона; 
        8 - удаление телефона; 
        9 - выход."""
        print(menu)
        return

    def form_group_name(self):
        while True:
            group_name = input("Введите номер группы (1 - отмена): ").strip()
            if group_name == "1":
                return
            if len(group_name.strip()) == 0:
                print("Номер группы не может быть пустым!")
            elif len(group_name.strip()) > 7:
                print("Номер группы имеет недопустимую длину!")
            else:
                return group_name

    def form_speciality(self):
        while True:
            speciality = input("Введите специальность (1 - отмена): ").strip()
            if speciality == "1":
                return
            if len(speciality.strip()) == 0:
                print("Специальность не может быть пустой!")
            elif len(speciality.strip()) > 128:
                print("Специальность имеет недопустимую длину!")
            else:
                return speciality

    def form_department(self):
        while True:
            second_name = input("Введите кафедру (1 - отмена): ").strip()
            if second_name == "1":
                return
            if len(second_name.strip()) == 0:
                print("Отчество не может быть пустым!")
            elif len(second_name.strip()) > 3:
                print("Отчество имеет недопустимую длину!")
            else:
                return second_name

    def add_group(self):
        data = [self.form_group_name(), self.form_speciality(), self.form_department()]
        for i in data:
            if i is None:
                return "-1"
        GroupsTable().insert_one(data)
        return "-1"

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
                    # current_step = self.add
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
                elif current_step in ["7", "8"]:
                    step = self.find_phone_by_id()
                    if step is None:
                        if current_step == "7":
                            current_step = self.edit_phone()
                        else:
                            current_step = self.delete_phone()
                    else:
                        current_step = step
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

    def show_edit_person_menu(self):
        menu = """Дальнейшие операции:
        0 - Отмена;
        1 - Изменение фамилии;
        2 - Изменение имени;
        3 - Изменение отчества;
        """
        print(menu)
        return

    def edit_person(self):
        if self.find_phone_by_person() == "0":
            values_for_edit = []
            step = "-1"
            while True:
                if step == "-1":
                    self.show_edit_person_menu()
                    step = self.read_next_step()
                elif step in ["1", "2", "3"]:
                    break
                elif step == "0":
                    return "-1"
                else:
                    print("Выбрано неверное значение! Повторите ввод!")

            if step == "1":
                last_name = self.form_last_name()
                if last_name is None:
                    return "-1"
                values_for_edit = [last_name, self.person_id, "last_name"]
            elif step == "2":
                first_name = self.form_first_name()
                if first_name is None:
                    return "-1"
                values_for_edit = [first_name, self.person_id, "first_name"]
            else:
                second_name = self.form_second_name()
                if second_name is None:
                    return "-1"
                values_for_edit = [second_name, self.person_id, "second_name"]
            if len(values_for_edit) == 3:
                PeopleTable().update(values_for_edit)
        return "-1"

    def delete_person(self):
        if self.find_phone_by_person() == "0":
            PeopleTable().delete(self.person_id)
        return "-1"

    def show_people_menu(self):
        menu = """Дальнейшие операции:
    0 - возврат в главное меню;
    3 - добавление нового человека;
    4 - удаление человека;
    5 - просмотр телефонов человека;
    6 - Редактирование информации о человеке
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
                current_step = self.add_person()
            elif current_step == "4":
                current_step = self.delete_person()
            elif current_step == "5":
                current_step = self.phone_actions()
            elif current_step == "6":
                current_step = self.edit_person()
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

    def show_group_menu(self):
        menu = """Дальнейшие операции:
        0 - Возврат в главное меню;
        3 - Добавление новой группы;
        4 - Изменение номера группы
        5 - Изменение специальности группы;
        6 - Изменение кафедры; 
        7 - Удаление группы;
        9 - Выход."""
        print(menu)
        return

    def formatted_print(self, columns):
        row = ""
        for i in columns:
            x = i
            if type(x) is not str:
                x = str(x)
            row += '{:<15}'.format(x)
        print(row)


    def show_groups(self):
        self.person_id = -1
        menu = """Просмотр списка групп!\n"""
        columns = ["№", "Группа", "Специальность", "Кафедра"]
        self.formatted_print(columns)
        lst = GroupsTable().all()
        for i in range(len(lst)):
            a = list(lst[i])[::-1]
            a.insert(0, i+1)
            self.formatted_print(a)
        return

    def find_group_by_id(self):
        num = -1
        while True:
            num = input("Укажите номер строки, в которой записан интересующий Вас номер группы (0 - отмена): ")
            if len(num.strip()) == 0:
                print("Пустая строка. Повторите ввод! ")
            if num == "0":
                return "1"
            if not num.strip().isnumeric():
                print("Неверные данные. Повторите ввод! ")

            group = GroupsTable().find_by_position(int(num))
            if not group:
                print("Введено число, неудовлетворяющее количеству телефонов!")
            else:
                self.group_obj = group
                break

    def edit_group(self, step):
        if self.find_group_by_id() is None:
            values_for_edit = []
            if step == "4":
                group_name = self.form_group_name()
                if group_name is None:
                    return "-1"
                values_for_edit = [group_name, self.group_obj[0], "group_name"]
            elif step == "5":
                speciality = self.form_speciality()
                if speciality is None:
                    return "-1"
                values_for_edit = [speciality, self.group_obj[0], "speciality"]
            else:
                department = self.form_department()
                if department is None:
                    return "-1"
                values_for_edit = [department, self.group_obj[0], "department"]
            if len(values_for_edit) == 3:
                GroupsTable().update(values_for_edit)
        return "-1"

    def delete_group(self):
        if self.find_group_by_id() is None:
            GroupsTable().delete(self.group_obj[0])
        return "-1"

    def group_actions(self):
        current_step = "-1"
        while True:
            if current_step == "-1":
                self.show_groups()
                self.show_group_menu()
                current_step = self.read_next_step()
            elif current_step == "3":
                current_step = self.add_group()
            elif current_step in ["4", "5", "6"]:
                current_step = self.edit_group(current_step)
            elif current_step == "7":
                current_step = self.delete_group()
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
                current_menu = self.group_actions()
            elif current_menu == "3":
                current_menu = self.find_people_by_lastname()
            elif current_menu == "8":
                current_menu = self.db_drop_init()
            else:
                print("Выбрано неверное значение! Повторите ввод!")
                current_menu = self.read_next_step()
        print("До свидания!")
        return


m = Main()
m.main_cycle()

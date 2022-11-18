from tables.people_table import *
from helpers.readWriterHelper import *
from controllers.phones_controller import *
from controllers.groups_controller import *
from controllers.people_groups_controller import *
from helpers.peopleHelper import *


class PeopleController:
    def __init__(self):
        self.gc = GroupsController()
        self.ph = PeopleHelper()
        self.group_obj = None
        self.person_id = None
        self.person_obj = None

    def find_people_by_lastname(self):
        while True:
            last_name = input("Укажите фамилию человека, которого надо найти: (0 - отмена) ")
            if len(last_name.strip()) == 0:
                print("Пустая строка. Повторите ввод! ")
            if len(last_name.strip()) > 32:
                print("Слишком длинная фамилия. Повторите ввод! ")
            if last_name == "0":
                return "0"
            person = PeopleTable().find_by_last_name(last_name)
            if person is not None:
                print("Выбран человек: " + person[3] + " " + person[0] + " " + person[4])
                return "0"
            else:
                print("Запись не найдена! Повторите ввод! ")

    def show_people(self):
        self.person_id = -1
        menu = """Просмотр списка людей!"""
        print(menu)
        columns = ["№", "Фамилия", "Имя", "Отчество", "Группа"]
        ReadWriter().formatted_print(columns)
        lst = PeopleTable().all()
        for i in range(len(lst)):
            a = list(lst[i])[1:]
            a.insert(0, i + 1)
            ReadWriter().formatted_print(a)
        return

    # Добавление человека
    def add_person(self):
        last_name = self.ph.form_last_name()
        if last_name is None:
            return "-1"
        first_name = self.ph.form_first_name()
        if first_name is None:
            return "-1"
        second_name = self.ph.form_second_name()
        if second_name is None:
            return "-1"
        data = [last_name, first_name, second_name, "NULL"]
        # Проверяем элементы на пустоту (в случае отмены ввода)
        for i in data:
            if i is None:
                return "-1"
        PeopleTable().insert_one(data)
        return "-1"

    def delete_person(self):
        if self.find_person() == "0":
            PeopleTable().delete(self.person_id)
        return "-1"

    def find_person(self):
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
                self.person_id = int(person[2])
                self.person_obj = person
                return "0"

    def edit_person(self):
        if self.find_person() == "0":
            values_for_edit = []
            step = "-1"
            while True:
                if step == "-1":
                    self.ph.show_edit_person_menu()
                    step = ReadWriter().read_next_step()
                elif step in ["1", "2", "3"]:
                    break
                elif step == "0":
                    return "-1"
                else:
                    print("Выбрано неверное значение! Повторите ввод!")

            if step == "1":
                last_name = self.ph.form_last_name()
                if last_name is None:
                    return "-1"
                values_for_edit = [last_name, self.person_id, "last_name"]
            elif step == "2":
                first_name = self.ph.form_first_name()
                if first_name is None:
                    return "-1"
                values_for_edit = [first_name, self.person_id, "first_name"]
            else:
                second_name = self.ph.form_second_name()
                if second_name is None:
                    return "-1"
                values_for_edit = [second_name, self.person_id, "second_name"]
            if len(values_for_edit) == 3:
                PeopleTable().update(values_for_edit)
        return "-1"

    def add_person_in_group(self):
        if self.find_person() == "0":
            self.gc.show_groups()
            if self.gc.find_group_by_id() is None:
                PeopleTable().update([self.group_obj[0], self.person_id, "group_name"])
        return "-1"

    def people_actions(self):
        current_step = "-1"
        while True:
            if current_step == "-1":
                self.show_people()
                self.ph.show_people_menu()
                current_step = ReadWriter().read_next_step()
            elif current_step == "3":
                current_step = self.add_person()
            elif current_step == "4":
                current_step = self.delete_person()
            elif current_step == "5":
                code = "-1"
                if self.person_id == -1:
                    code = self.find_person()
                current_step = PhonesController(self.person_obj).phone_actions(code)
            elif current_step == "6":
                current_step = self.edit_person()
            elif current_step == "7":
                current_step = self.add_person_in_group()
            elif current_step == "8":
                print("Не реализовано! ")
                current_step = "-1"
            elif current_step == "0":
                return "0"
            elif current_step == "9":
                return "9"
            else:
                print("Выбрано неверное значение! Повторите ввод!")
                current_step = ReadWriter.read_next_step()

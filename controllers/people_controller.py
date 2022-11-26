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
        self.pgc = PeopleGroupController()
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
            records = PeopleTable().find_by_last_name(last_name)
            if records is not None:
                print("Найдены записи")
                for person in records:
                    print(person.last_name + " " + person.first_name + " " + person.second_name)
                return "0"
            else:
                print("Запись не найдена! Повторите ввод! ")

    def show_people(self):
        self.person_id = -1
        menu = """Просмотр списка людей!"""
        print(menu)
        columns = ["id", "Фамилия", "Имя", "Отчество", "Группа"]
        ReadWriter().formatted_print(columns)
        lst = PeopleGroupsTable().get_people_groups()
        i = 0
        for people_group, people, groups in lst:
            group_name = None
            if groups is not None:
                group_name = groups.group_name
            a = [people.id, people.last_name, people.first_name, people.second_name, group_name]
            ReadWriter().formatted_print(a)
            i += 1
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
        data = {"last_name": last_name, "first_name": first_name, "second_name": second_name}
        person = PeopleTable()
        person.set_attributes(data)
        person.add()
        return "-1"

    def delete_person(self):
        if self.find_person() == "0":
            PhonesTable().delete_depended(self.person_id)
            PeopleGroupsTable().delete_depended(self.person_id)
            self.person_obj.delete()
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
            person = PeopleTable().find_by_id(int(num))
            if not person:
                print("Введено число, неудовлетворяющее количеству людей!")
            else:
                self.person_id = person.id
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
            data = {}
            if step == "1":
                data['last_name'] = self.ph.form_last_name()
                if data['last_name'] is None:
                    return "-1"
            elif step == "2":
                data['first_name'] = self.ph.form_first_name()
                if data['first_name'] is None:
                    return "-1"
            else:
                data['second_name'] = self.ph.form_second_name()
                if data['second_name'] is None:
                    return "-1"
            if len(data) > 0:
                PeopleTable().update_value(data, self.person_id)
        return "-1"

    def add_person_in_group(self):
        if self.find_person() == "0":
            lst = GroupsTable().all()
            if lst is not None:
                self.gc.show_groups(lst)
                if self.gc.find_group_by_id() is None:
                    data = {"person_id": self.person_id, "group_id": self.gc.group_obj.id}
                    person_group = PeopleGroupsTable()
                    person_group.set_attributes(data)
                    person_group.add()
            else:
                print("Группы не найдены!")
        return "-1"
    """Доработать функцию"""
    def delete_person_in_group(self):
        if self.find_person() == "0":
            lst = PeopleGroupsTable().get_groups_by_person(self.person_id)
            if lst is not None:
                lst_group = []
                for people_group, people, groups in lst:
                    lst_group.append(groups)
                self.gc.show_groups(lst_group)
                if self.pgc.find_person_group(self.person_id) is None:
                    self.pgc.people_group_obj.delete()
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
                current_step = PhonesController(self.person_obj).phone_actions(code) # не готово
            elif current_step == "6":
                current_step = self.edit_person()
            elif current_step == "7":
                current_step = self.add_person_in_group()
            elif current_step == "8":
                current_step = self.delete_person_in_group()
            elif current_step == "0":
                return "0"
            elif current_step == "9":
                return "9"
            else:
                print("Выбрано неверное значение! Повторите ввод!")
                current_step = ReadWriter.read_next_step()

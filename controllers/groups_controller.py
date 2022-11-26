from tables.groups_table import *
from tables.people_groups_table import *
from helpers.readWriterHelper import *
from helpers.groupsHelper import *

class GroupsController:
    def __init__(self):
        self.gh = GroupsHelper()
        self.group_obj = None

    def group_actions(self):
        current_step = "-1"
        while True:
            if current_step == "-1":
                lst = GroupsTable().all()
                self.show_groups(lst)
                self.gh.show_group_menu()
                current_step = ReadWriter().read_next_step()
            elif current_step == "2":
                current_step = self.show_people_in_group()
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
                current_step = ReadWriter().read_next_step()


    def show_groups(self, lst):
        menu = """Просмотр списка групп!"""
        print(menu)
        columns = ["№", "Группа", "Специальность", "Кафедра"]
        ReadWriter().formatted_print(columns)
        for group in lst:
            a = [group.id, group.group_name, group.speciality, group.department]
            ReadWriter().formatted_print(a)
        return

    def add_group(self):
        group_name = self.gh.form_group_name()
        if group_name is None:
            return "-1"
        speciality = self.gh.form_speciality()
        if speciality is None:
            return "-1"
        department = self.gh.form_department()
        if department is None:
            return "-1"
        data = {"group_name": group_name, "speciality": speciality, "department": department}
        group = GroupsTable()
        group.set_attributes(data)
        group.add()
        return "-1"

    def find_group_by_id(self):
        num = -1
        while True:
            num = input("Укажите номер id, в которой записан интересующий Вас номер группы (0 - отмена): ")
            if len(num.strip()) == 0:
                print("Пустая строка. Повторите ввод! ")
            if num == "0":
                return "1"
            if not num.strip().isnumeric():
                print("Неверные данные. Повторите ввод! ")

            group = GroupsTable().find_by_id(int(num))
            if not group:
                print("Введено число, неудовлетворяющее существующим id!")
            else:
                self.group_obj = group
                break

    def edit_group(self, step):
        if self.find_group_by_id() is None:
            data = {}
            if step == "4":
                data['group_name'] = self.gh.form_group_name()
                if data['group_name'] is None:
                    return "-1"
            elif step == "5":
                data['speciality'] = self.gh.form_speciality()
                if data['speciality'] is None:
                    return "-1"
            else:
                data['department'] = self.gh.form_department()
                if data['department'] is None:
                    return "-1"
            if len(data) > 0:
                GroupsTable().update_value(data, self.group_obj.id)
        return "-1"

    def delete_group(self):
        if self.find_group_by_id() is None:
            PeopleGroupsTable().delete_depended_group(self.group_obj.id)
            self.group_obj.delete()
        return "-1"

    def show_people_in_group(self):
        if self.find_group_by_id() is None:
            lst = PeopleGroupsTable().get_people_by_group(self.group_obj.id)
            if len(lst) > 0:
                self.gh.show_people(lst)
            else:
                print("В группе нет обучающихся!")
        return "-1"

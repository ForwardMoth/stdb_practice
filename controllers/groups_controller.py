from tables.groups_table import *
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
                self.show_groups()
                self.gh.show_group_menu()
                current_step = ReadWriter().read_next_step()
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


    def show_groups(self):
        menu = """Просмотр списка групп!\n"""
        columns = ["№", "Группа", "Специальность", "Кафедра"]
        ReadWriter().formatted_print(columns)
        lst = GroupsTable().all()
        for i in range(len(lst)):
            a = list(lst[i])
            a.insert(0, i + 1)
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
        data = [group_name, speciality, department]
        for i in data:
            if i is None:
                return "-1"
        GroupsTable().insert_one(data)
        return "-1"

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
                group_name = self.gh.form_group_name()
                if group_name is None:
                    return "-1"
                values_for_edit = [group_name, self.group_obj[0], "group_name"]
            elif step == "5":
                speciality = self.gh.form_speciality()
                if speciality is None:
                    return "-1"
                values_for_edit = [speciality, self.group_obj[0], "speciality"]
            else:
                department = self.gh.form_department()
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

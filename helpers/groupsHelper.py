from helpers.readWriterHelper import *


class GroupsHelper:
    def show_group_menu(self):
        menu = """Дальнейшие операции:
        0 - Возврат в главное меню;
        2 - Просмотр списка группы;
        3 - Добавление новой группы;
        4 - Изменение номера группы
        5 - Изменение специальности группы;
        6 - Изменение кафедры; 
        7 - Удаление группы;
        9 - Выход."""
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

    def show_people(self, lst):
        menu = """Просмотр списка людей!"""
        print(menu)
        columns = ["id", "Фамилия", "Имя", "Отчество"]
        ReadWriter().formatted_print(columns)
        i = 0
        for people_group, people, groups in lst:
            a = [people.id, people.last_name, people.first_name, people.second_name]
            ReadWriter().formatted_print(a)
            i += 1

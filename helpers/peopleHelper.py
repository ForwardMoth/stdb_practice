from tables.people_table import *


class PeopleHelper:
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

    def show_edit_person_menu(self):
        menu = """Дальнейшие операции:
           0 - Отмена;
           1 - Изменение фамилии;
           2 - Изменение имени;
           3 - Изменение отчества;
           """
        print(menu)

    def show_people_menu(self):
        menu = """Дальнейшие операции:
    0 - возврат в главное меню;
    3 - добавление нового человека;
    4 - удаление человека;
    5 - просмотр телефонов человека;
    6 - Редактирование информации о человеке;
    7 - Добавление человека в группу;
    9 - выход."""
        print(menu)

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
from tables.people_groups_table import *


class PeopleGroupController:
    def __init__(self):
        self.people_group_obj = None

    def find_person_group(self, person_id):
        num = -1
        while True:
            num = input("Укажите номер id, в которой записан интересующий Вас номер группы (0 - отмена): ")
            if len(num.strip()) == 0:
                print("Пустая строка. Повторите ввод! ")
            if num == "0":
                return "1"
            if not num.strip().isnumeric():
                print("Неверные данные. Повторите ввод! ")
            person_group = PeopleGroupsTable().find_by_person_and_group(person_id, int(num))
            if not person_group:
                print("Введено число, неудовлетворяющее существующим идентификаторам группы!")
            else:
                self.people_group_obj = person_group[0]
                break

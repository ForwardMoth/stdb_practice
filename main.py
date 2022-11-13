import sys

sys.path.append('tables')

from project_config import *
from controllers.people_controller import *
from helpers.peopleHelper import *


class Main:
    config = ProjectConfig()
    connection = DbConnection(config)

    def __init__(self):
        self.group_obj = None
        self.person_id = None
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
        pt.insert_one(["Test", "Test", "Test", "NULL"])
        pt.insert_one(["Test2", "Test2", "Test2", "NULL"])
        pt.insert_one(["Test3", "Test3", "Test3", "NULL"])
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

    def db_drop_init(self):
        self.db_drop()
        self.db_init()
        self.db_insert_somethings()
        print("Таблицы созданы заново!")
        return "0"

    def main_cycle(self):
        current_menu = "0"
        while current_menu != "9":
            if current_menu == "0":
                self.show_main_menu()
                current_menu = ReadWriter().read_next_step()
            elif current_menu == "1":
                current_menu = PeopleController().people_actions()
            elif current_menu == "2":
                current_menu = GroupsController().group_actions()
            elif current_menu == "3":
                current_menu = PeopleHelper().find_people_by_lastname()
            elif current_menu == "8":
                current_menu = self.db_drop_init()
            else:
                print("Выбрано неверное значение! Повторите ввод!")
                current_menu = ReadWriter().read_next_step()
        print("До свидания!")
        return


m = Main()
m.main_cycle()

import sys

sys.path.append('tables')

from project_config import *
from controllers.people_controller import *
from tables.people_table import *


class Main:
    config = ProjectConfig()
    connection = DbConnection(config)

    def __init__(self):
        DbTable.dbconn = self.connection

    def db_init(self):
        self.connection.set_metadata()
        PeopleTable().create()
        GroupsTable().create()
        PhonesTable().create()
        PeopleGroupsTable().create()
        self.connection.metadata.create_all(self.connection.engine)

    def db_drop(self):
        PhonesTable().drop()
        PeopleGroupsTable().drop()
        PeopleTable().drop()
        GroupsTable().drop()
        self.connection.metadata.drop_all(self.connection.engine)

    def db_insert_somethings(self):
        people = PeopleTable()
        groups = GroupsTable()
        phones = PhonesTable()
        people_groups = PeopleGroupsTable()

        people.insert_one(["Test", "Test", "Test"])
        people.insert_one(["Test2", "Test2", "Test2"])
        people.insert_one(["Test3", "Test3", "Test3"])
        phones.insert_one([1, "123"])
        phones.insert_one([2, "123"])
        phones.insert_one([3, "123"])
        groups.insert_one(["C19-702", "ИАСБ", "75"])
        groups.insert_one(["C19-712", "ИАСБ", "75"])
        groups.insert_one(["C19-711", "ЭКБЕЗ", "75"])
        people_groups.insert_one([1, 1])
        people_groups.insert_one([1, 2])
        people_groups.insert_one([2, 2])

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
                current_menu = PeopleController().find_people_by_lastname()
            elif current_menu == "8":
                current_menu = self.db_drop_init()
            else:
                print("Выбрано неверное значение! Повторите ввод!")
                current_menu = ReadWriter().read_next_step()
        print("До свидания!")
        return


m = Main()
m.main_cycle()




from controllers.people_controller import *


class Main:
    def __init__(self):
        self.db = DataBase()

    def db_init(self):
        people = PeopleTable()
        groups = GroupsTable()
        phones = PhonesTable()
        people_groups = PeopleGroupsTable()
        self.db.Base.metadata.create_all(self.db.engine)

    def db_drop(self):
        self.db.Base.metadata.drop_all(self.db.engine)

    def db_insert_somethings(self):
        data_people = {
            "1": {"last_name": "Иванов", "first_name": "Иван", "second_name": "Иванович"},
            "2": {"last_name": "Петров", "first_name": "Александр", "second_name": "Петрович"},
            "3": {"last_name": "Сидоров", "first_name": "Василий", "second_name": "Игоревич"}
        }

        for key in data_people:
            person = PeopleTable()
            person.set_attributes(data_people[key])
            person.add()

        data_groups = {
            "1": {"group_name": "C19-702", "speciality": "ИАСБ", "department": "75"},
            "2": {"group_name": "C19-712", "speciality": "ИАСБ", "department": "75"},
            "3": {"group_name": "C19-711", "speciality": "ЭКБЕЗ", "department": "75"}
        }

        for key in data_groups:
            group = GroupsTable()
            group.set_attributes(data_groups[key])
            group.add()

        data_phones = {
            "1": {"person_id": 1, "phone": "123"},
            "2": {"person_id": 2, "phone": "12421"},
            "3": {"person_id": 3, "phone": "5474"}
        }

        for key in data_phones:
            phone = PhonesTable()
            phone.set_attributes(data_phones[key])
            phone.add()

        data_people_groups = {
            "1": {"person_id": 1, "group_id": 1},
            "2": {"person_id": 1, "group_id": 2},
            "3": {"person_id": 2, "group_id": 2}
        }

        for key in data_people_groups:
            person_group = PeopleGroupsTable()
            person_group.set_attributes(data_people_groups[key])
            person_group.add()

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
                current_menu = PeopleController().people_actions() # не готово
            elif current_menu == "2":
                current_menu = GroupsController().group_actions() # не готово
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



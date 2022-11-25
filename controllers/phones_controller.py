from tables.phones_table import *
from helpers.readWriterHelper import *
from helpers.phonesHelper import *


class PhonesController:
    def __init__(self, person_obj):
        self.ph = PhonesHelper()
        self.person_id = person_obj[2]
        self.person_obj = person_obj

    def show_phones_by_people(self):
        if self.person_id != -1:
            print("Выбран человек: " + self.person_obj[3] + " " + self.person_obj[0] + " " + self.person_obj[4])
            lst = PhonesTable().all_by_person_id(self.person_id)
            # Проверяем есть ли в таблице номера телефонов для человека
            if len(lst) == 0:
                print("Нет телефонов")
            else:
                phone_show_text = """Просмотр списка телефонов!"""
                print(phone_show_text)
                columns = ["№", "Телефон"]
                ReadWriter().formatted_print(columns)
                for i in range(len(lst)):
                    a = [i + 1, lst[i][1]]
                    ReadWriter().formatted_print(a)
        return

    # Новая функция для добавление телефонов
    def add_phone(self):
        phone = self.ph.phone_form()
        if phone is None:
            return "-1"
        data = [self.person_id, phone]
        PhonesTable().insert_one(data)
        return "-1"

    # Вспомогательная функция, которая находит нужный номер телефона человека
    def find_phone_by_id(self):
        num = -1
        while True:
            num = input("Укажите номер строки, в которой записан интересующий Вас номер телефона (0 - отмена): ")
            if len(num.strip()) == 0:
                print("Пустая строка. Повторите ввод! ")
            if num == "0":
                return "-1"
            if not num.strip().isnumeric():
                print("Неверные данные. Повторите ввод! ")

            phone = PhonesTable().find_by_id(int(num), self.person_id)
            if not phone:
                print("Введено число, неудовлетворяющее количеству телефонов!")
            else:
                self.phone_id = int(phone[0])
                self.phone_obj = phone
                break

    # Новая функция для редактирования номера телефона
    def edit_phone(self):
        phone = self.ph.phone_form()
        if phone is not None:
            PhonesTable().update(phone, self.phone_obj[1])
        return "-1"

    # Новая функция для удаления номера телефона
    def delete_phone(self):
        PhonesTable().delete(self.phone_obj[1])
        return "-1"

    def phone_actions(self, code):
        if code == "0":
            current_step = "-1"
            while True:
                if current_step == "-1":
                    self.show_phones_by_people()
                    self.ph.show_phones_menu()
                    current_step = ReadWriter().read_next_step()
                elif current_step == "2":
                    current_step = self.add_phone()
                elif current_step in ["3", "4"]:
                    step = self.find_phone_by_id()
                    if step is None:
                        if current_step == "3":
                            current_step = self.edit_phone()
                        else:
                            current_step = self.delete_phone()
                    else:
                        current_step = step
                elif current_step == "1":
                    return "-1"
                elif current_step == "0":
                    return "0"
                elif current_step == "9":
                    return "9"
                else:
                    print("Выбрано неверное значение! Повторите ввод!")
                    current_step = ReadWriter().read_next_step()
        return "-1"

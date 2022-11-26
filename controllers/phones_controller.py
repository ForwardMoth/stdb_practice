from tables.phones_table import *
from helpers.readWriterHelper import *
from helpers.phonesHelper import *


class PhonesController:
    def __init__(self, person_obj):
        self.ph = PhonesHelper()
        self.person_id = person_obj.id
        self.person_obj = person_obj
        self.phone_id = None
        self.phone_obj = None

    def show_phones_by_people(self):
        if self.person_id != -1:
            print("Выбран человек: " + self.person_obj.last_name + " " + self.person_obj.first_name + " " +
                  self.person_obj.second_name)
            lst = PhonesTable().phones_by_person(self.person_id)
            if len(lst) == 0:
                print("Нет телефонов")
            else:
                phone_show_text = """Просмотр списка телефонов!"""
                print(phone_show_text)
                columns = ["id", "Телефон"]
                ReadWriter().formatted_print(columns)
                for phone in lst:
                    a = [phone.id, phone.phone]
                    ReadWriter().formatted_print(a)
        return

    def add_phone(self):
        phone = self.ph.phone_form()
        if phone is None:
            return "-1"
        data = {"person_id": self.person_id, "phone": phone}
        phone = PhonesTable()
        phone.set_attributes(data)
        phone.add()
        return "-1"

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

            phone = PhonesTable().find_by_phone_person(self.person_id, int(num))
            if not phone:
                print("Введено число, неудовлетворяющее id телефонов!")
            else:
                self.phone_obj = phone[0]
                self.phone_id = self.phone_obj.id
                break

    def edit_phone(self):
        phone = self.ph.phone_form()
        if phone is not None:
            PhonesTable().update_value({"phone": phone}, self.phone_id)
        return "-1"

    def delete_phone(self):
        self.phone_obj.delete()
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

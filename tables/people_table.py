from db import *


class PeopleTable(DataBase.Base, DataBase):
    __tablename__ = "people"
    id = Column(Integer, primary_key=True, autoincrement=True)
    last_name = Column(String(32), nullable=False)
    first_name = Column(String(32), nullable=False)
    second_name = Column(String(32))

    def __init__(self):
        self.last_name = None
        self.first_name = None
        self.second_name = None


    def set_attributes(self, data):
        self.last_name = data["last_name"]
        self.first_name = data["first_name"]
        self.second_name = data["second_name"]

    def find_by_last_name(self, last_name):
        return self.session.query(PeopleTable).filter(PeopleTable.last_name == last_name).all()


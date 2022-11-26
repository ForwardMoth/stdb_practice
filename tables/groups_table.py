from db import *


class GroupsTable(DataBase.Base, DataBase):
    __tablename__ = "groups"
    id = Column(Integer, primary_key=True, autoincrement=True)
    group_name = Column(String(7), nullable=False)
    speciality = Column(String(128), nullable=False)
    department = Column(String(3), nullable=False)

    def __init__(self):
        self.group_name = None
        self.speciality = None
        self.department = None

    def set_attributes(self, data):
        self.group_name = data["group_name"]
        self.speciality = data["speciality"]
        self.department = data["department"]

    def all(self):
        return self.session.query(GroupsTable).all()


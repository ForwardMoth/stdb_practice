from db import *


class PeopleGroupsTable(DataBase.Base):
    __tablename__ = "people_groups"
    id = Column(Integer, primary_key=True, autoincrement=True)
    person_id = Column(Integer, ForeignKey("people.id"))
    group_id = Column(Integer, ForeignKey("groups.id"))

    def __init__(self):
        self.person_id = None
        self.group_id = None

    def set_attributes(self, data):
        self.person_id = data["person_id"]
        self.group_id = data["group_id"]

from tables.people_table import *
from tables.groups_table import *


class PeopleGroupsTable(DataBase.Base, DataBase):
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

    def get_people_groups(self):
        query = self.session.query(PeopleGroupsTable, PeopleTable, GroupsTable)
        query = query.outerjoin(PeopleGroupsTable, PeopleGroupsTable.person_id == PeopleTable.id)
        query = query.outerjoin(GroupsTable, GroupsTable.id == PeopleGroupsTable.group_id)
        return query.order_by(PeopleTable.id).all()

    def delete_depended(self, person_id):
        self.session.query(PeopleGroupsTable).filter(PeopleGroupsTable.person_id == person_id).\
            delete(synchronize_session='fetch')
        self.session.commit()

    def get_groups_by_person(self, per_id):
        query = self.session.query(PeopleGroupsTable, GroupsTable)
        query = query.outerjoin(GroupsTable, GroupsTable.id == PeopleGroupsTable.group_id)
        query = self.session.query(PeopleGroupsTable).filter(PeopleGroupsTable.person_id == per_id)
        return query.order_by().all()

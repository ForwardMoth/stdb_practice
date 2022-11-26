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

    def delete_depended_person(self, person_id):
        self.session.query(PeopleGroupsTable).filter(PeopleGroupsTable.person_id == person_id). \
            delete(synchronize_session='fetch')
        self.session.commit()

    def get_groups_by_person(self, per_id):
        query = self.session.query(PeopleGroupsTable, PeopleTable, GroupsTable)
        query = query.outerjoin(PeopleGroupsTable, PeopleGroupsTable.person_id == PeopleTable.id)
        query = query.outerjoin(GroupsTable, GroupsTable.id == PeopleGroupsTable.group_id)
        return query.filter(PeopleTable.id == per_id).all()

    def find_by_person_and_group(self, p_id, g_id):
        query = self.session.query(PeopleGroupsTable).filter(PeopleGroupsTable.person_id == p_id,
                                                             PeopleGroupsTable.group_id == g_id)
        return query.all()

    def delete_group_by_person(self, p_id, g_id):
        self.session.query(PeopleGroupsTable).filter(PeopleGroupsTable.person_id == p_id,
                                                     PeopleGroupsTable.group_id == g_id).delete()
        self.session.commit()

    def delete_depended_group(self, group_id):
        self.session.query(PeopleGroupsTable).filter(PeopleGroupsTable.group_id == group_id). \
            delete(synchronize_session='fetch')
        self.session.commit()

    def get_people_by_group(self, g_id):
        query = self.session.query(PeopleGroupsTable, PeopleTable, GroupsTable)
        query = query.outerjoin(PeopleGroupsTable, PeopleGroupsTable.person_id == PeopleTable.id)
        query = query.outerjoin(GroupsTable, GroupsTable.id == PeopleGroupsTable.group_id)
        return query.filter(GroupsTable.id == g_id).all()
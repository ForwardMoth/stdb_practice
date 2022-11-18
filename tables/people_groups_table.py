from dbtable import *


class PeopleGroupsTable(DbTable):
    def create(self):
        people_groups = Table(self.table_name(), self.dbconn.metadata, self.column_person_id(),
                              self.column_group_id())

    def table_name(self):
        return self.dbconn.prefix + "people_groups"

    def column_person_id(self):
        return Column('person_id', ForeignKey(self.dbconn.prefix + "people.id"))

    def column_group_id(self):
        return Column('group_id', ForeignKey(self.dbconn.prefix + "groups.id"))

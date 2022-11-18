from dbtable import *


class GroupsTable(DbTable):
    def create(self):
        groups = Table(self.table_name(), self.dbconn.metadata, self.column_id(), self.column_group_name(),
                       self.column_speciality(), self.column_department())

    def table_name(self):
        return self.dbconn.prefix + "groups"

    def column_group_name(self):
        return Column('group_name', String(7), nullable=False)

    def column_speciality(self):
        return Column('speciality', String(128), nullable=False)

    def column_department(self):
        return Column('department', String(3), nullable=False)



    # def primary_key(self):
    #     return ['group_name']
    #
    # def table_constraints(self):
    #     return ["PRIMARY KEY(group_name)"]
    #
    # def find_by_position(self, num):
    #     sql = "SELECT group_name, speciality, department FROM " + self.table_name()
    #     sql += " ORDER BY "
    #     sql += ", ".join(self.primary_key())
    #     sql += " LIMIT 1 OFFSET :offset"
    #     cur = self.dbconn.conn.cursor()
    #     cur.execute(sql, {"offset": num - 1})
    #     return cur.fetchone()
    #
    # def update(self, a):
    #     sql = "UPDATE " + self.table_name()
    #     sql += f" SET {a[2]} = :new_value"
    #     sql += f" WHERE group_name = :group_name"
    #     cur = self.dbconn.conn.cursor()
    #     cur.execute(sql, {"new_value": a[0], "group_name": a[1]})
    #     self.dbconn.conn.commit()
    #     return
    #
    # def delete(self, group_name):
    #     sql = "DELETE FROM " + self.table_name()
    #     sql += " WHERE group_name = :group_name"
    #     cur = self.dbconn.conn.cursor()
    #     cur.execute(sql, {"group_name": group_name})
    #     self.dbconn.conn.commit()
    #     return
    #
    # def all(self):
    #     sql = "SELECT group_name, speciality, department FROM " + self.table_name()
    #     sql += " ORDER BY "
    #     sql += ", ".join(self.primary_key())
    #     cur = self.dbconn.conn.cursor()
    #     cur.execute(sql)
    #     return cur.fetchall()

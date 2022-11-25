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

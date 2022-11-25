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




    # def find_by_position(self, num):
    #     sql = "SELECT * FROM " + self.table_name()
    #     sql += " ORDER BY "
    #     sql += ", ".join(self.primary_key())
    #     sql += " LIMIT 1 OFFSET :offset"
    #     cur = self.dbconn.conn.cursor()
    #     cur.execute(sql, {"offset": num - 1})
    #     return cur.fetchone()
    #
    # def find_by_last_name(self, l_name):
    #     sql = "SELECT * FROM " + self.table_name()
    #     sql += " WHERE last_name = :lastname "
    #     cur = self.dbconn.conn.cursor()
    #     cur.execute(sql, {"lastname": l_name})
    #     return cur.fetchone()
    #
    # def all(self):
    #     sql = "SELECT id, last_name, first_name, second_name, group_name FROM " + self.table_name()
    #     sql += " ORDER BY "
    #     sql += ", ".join(self.primary_key())
    #     cur = self.dbconn.conn.cursor()
    #     cur.execute(sql)
    #     return cur.fetchall()
    #
    # def update(self, a):
    #     sql = "UPDATE " + self.table_name()
    #     sql += f" SET {a[2]} = :new_value"
    #     sql += f" WHERE id = :person_id"
    #     cur = self.dbconn.conn.cursor()
    #     cur.execute(sql, {"new_value": a[0], "person_id": a[1]})
    #     self.dbconn.conn.commit()
    #     return
    #
    # def delete(self, person_id):
    #     sql = "DELETE FROM " + self.table_name()
    #     sql += " WHERE id = :person_id"
    #     cur = self.dbconn.conn.cursor()
    #     cur.execute(sql, {"person_id": person_id})
    #     self.dbconn.conn.commit()
    #     return

from dbtable import *


class PeopleTable(DbTable):
    def create(self):
        people = Table(self.table_name(), self.dbconn.metadata, self.column_id(), self.column_last_name(),
                       self.column_first_name(), self.column_second_name())

    def table_name(self):
        return self.dbconn.prefix + "people"

    def column_last_name(self):
        return Column('last_name', String(32), nullable=False)

    def column_first_name(self):
        return Column('first_name', String(32), nullable=False)

    def column_second_name(self):
        return Column('second_name', String(32))



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

from dbtable import *

class GroupsTable(DbTable):
    def table_name(self):
        return self.dbconn.prefix + "groups"

    def columns(self):
        return {"group_name": ["varchar(7)", "NOT NULL"],
                "speciality": ["varchar(128)", "NOT NULL"],
                "department": ["varchar(3)", "NOT NULL"]}

    def primary_key(self):
        return ['group_name']

    def table_constraints(self):
        return ["PRIMARY KEY(group_name)"]

    def find_by_position(self, num):
        sql = "SELECT group_name, speciality, department FROM " + self.table_name()
        sql += " ORDER BY "
        sql += ", ".join(self.primary_key())
        sql += " LIMIT 1 OFFSET :offset"
        cur = self.dbconn.conn.cursor()
        cur.execute(sql, {"offset": num - 1})
        return cur.fetchone()

    def update(self, a):
        sql = "UPDATE " + self.table_name()
        sql += f" SET {a[2]} = :new_value"
        sql += f" WHERE group_name = :group_name"
        cur = self.dbconn.conn.cursor()
        cur.execute(sql, {"new_value": a[0], "group_name": a[1]})
        self.dbconn.conn.commit()
        return

    def delete(self, group_name):
        sql = "DELETE FROM " + self.table_name()
        sql += " WHERE group_name = :group_name"
        cur = self.dbconn.conn.cursor()
        cur.execute(sql, {"group_name": group_name})
        self.dbconn.conn.commit()
        return

    def all(self):
        sql = "SELECT group_name, speciality, department FROM " + self.table_name()
        sql += " ORDER BY "
        sql += ", ".join(self.primary_key())
        cur = self.dbconn.conn.cursor()
        cur.execute(sql)
        return cur.fetchall()
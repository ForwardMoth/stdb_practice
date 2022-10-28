from dbtable import *

class GroupsTable(DbTable):
    def table_name(self):
        return self.dbconn.prefix + "groups"

    def columns(self):
        return {"group_name": ["varchar(7)", "NOT NULL"],
                "speciality": ["varchar(128)", "NOT NULL"],
                "department": ["varchar(64)"]}

    def primary_key(self):
        return ['group_name']

    def table_constraints(self):
        return ["PRIMARY KEY(group_name)"]

    def find_by_position(self, num):
        sql = "SELECT * FROM " + self.table_name()
        sql += " ORDER BY "
        sql += ", ".join(self.primary_key())
        sql += " LIMIT 1 OFFSET :offset"
        cur = self.dbconn.conn.cursor()
        cur.execute(sql, {"offset": num - 1})
        return cur.fetchone()




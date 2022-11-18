from dbtable import *


class PhonesTable(DbTable):
    def create(self):
        phones = Table(self.table_name(), self.dbconn.metadata, self.column_id(), self.column_person_id(),
                       self.column_phone())

    def table_name(self):
        return self.dbconn.prefix + "phones"

    def column_person_id(self):
        return Column('person_id', ForeignKey(self.dbconn.prefix + "people.id"))

    def column_phone(self):
        return Column('phone', String(12), nullable=False)


    # def primary_key(self):
    #     return ['person_id', 'phone']
    #
    # def table_constraints(self):
    #     return ["PRIMARY KEY(person_id, phone)"]
    #
    # def all_by_person_id(self, pid):
    #     sql = "SELECT * FROM " + self.table_name()
    #     sql += " WHERE person_id = :id"
    #     sql += " ORDER BY "
    #     sql += ", ".join(self.primary_key())
    #     cur = self.dbconn.conn.cursor()
    #     cur.execute(sql, str(pid))
    #     return cur.fetchall()
    #
    # def find_by_position(self, num, person_id):
    #     sql = "SELECT * FROM " + self.table_name()
    #     sql += " WHERE person_id = :id"
    #     sql += " ORDER BY "
    #     sql += ", ".join(self.primary_key())
    #     sql += " LIMIT 1 OFFSET :offset"
    #     cur = self.dbconn.conn.cursor()
    #     cur.execute(sql, {"offset": num - 1, "id": person_id})
    #     return cur.fetchone()
    #
    # def update(self, new_value, old_value):
    #     sql = "UPDATE " + self.table_name()
    #     sql += " SET phone = :new_value"
    #     sql += " WHERE phone = :old_value"
    #     cur = self.dbconn.conn.cursor()
    #     cur.execute(sql, {"new_value": new_value, "old_value": old_value})
    #     self.dbconn.conn.commit()
    #     return
    #
    # def delete(self, phone):
    #     sql = "DELETE FROM " + self.table_name()
    #     sql += " WHERE phone = :phone"
    #     cur = self.dbconn.conn.cursor()
    #     cur.execute(sql, {"phone": phone})
    #     self.dbconn.conn.commit()
    #     return

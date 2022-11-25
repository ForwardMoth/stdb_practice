from db import *


class PhonesTable(DataBase.Base, DataBase):
    __tablename__ = "phones"
    id = Column(Integer, primary_key=True, autoincrement=True)
    person_id = Column(Integer, ForeignKey("people.id"))
    phone = Column(String(12), nullable=False)

    def __init__(self):
        self.person_id = None
        self.phone = None

    def set_attributes(self, data):
        self.person_id = data["person_id"]
        self.phone = data["phone"]

    def delete_depended(self, person_id):
        self.session.query(PhonesTable).filter(PhonesTable.id == person_id).delete(synchronize_session='fetch')
        self.session.commit()


    # def create(self):
    #     person_id = Column('person_id', ForeignKey(self.dbconn.prefix + "people.id"))
    #     phone = Column('phone', String(12), nullable=False)
    #     phones = Table(self.table_name(), self.dbconn.metadata, self.column_id(), person_id, phone)
    #
    # def table_name(self):
    #     return self.dbconn.prefix + "phones"

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

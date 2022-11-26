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

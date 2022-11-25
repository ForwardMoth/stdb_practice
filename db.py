from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.exc import *
from configs.project_config import *
from sqlalchemy import Column, String, Integer, ForeignKey


class DataBase:
    config = Config()
    Base = declarative_base()
    engine = create_engine(f'postgresql://{config.user}:{config.password}@localhost:'
                           f'{config.port}/{config.db_name}')
    Session = sessionmaker(bind=engine)
    session = Session()

    def add(self):
        self.session.add(self)
        try:
            self.session.commit()
        except IntegrityError as err:
            self.session.rollback()
            print(err)

    def find_by_id(self, id):
        return self.session.query(self.__class__).get(id)

    def delete(self):
        self.session.delete(self)
        self.session.commit()

    def update_value(self, data, id):
        self.session.query(self.__class__).filter(self.__class__.id == id).update(data)
        self.session.commit()


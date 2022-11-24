from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.exc import *
from configs.project_config import *
from sqlalchemy import Column, String, Integer, ForeignKey


class DataBase:
    config = Config()
    Base = declarative_base()

    def __init__(self):
        self.engine = create_engine(f'postgresql://{self.config.user}:{self.config.password}@localhost:'
                                    f'{self.config.port}/{self.config.db_name}')
        self.Session = sessionmaker(bind=self.engine)
        self.session = self.Session()

    def add(self, obj):
        self.session.add(obj)
        try:
            self.session.commit()
        except IntegrityError as err:
            self.session.rollback()
            print(err)

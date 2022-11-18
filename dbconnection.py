from sqlalchemy import create_engine, MetaData
from project_config import *

class DbConnection:

    def __init__(self, config):
        self.path = config.dbfilepath
        self.prefix = config.dbtableprefix
        self.engine = create_engine(
            f"postgresql+psycopg2://{config.user}:{config.password}@localhost/{config.db_name}",
            echo=True, pool_size=6, max_overflow=10, encoding='utf8'
        )
        self.connect = self.engine.connect()
        self.metadata = MetaData()

    def set_metadata(self):
        self.metadata = MetaData()


    # def __del__(self):
    #     if self.connection:
    #         self.connection.close()


    # def test(self):
    #     cur = self.connection.cursor()
    #     cur.execute("CREATE TABLE test(test integer)")
    #     cur.execute("INSERT INTO test(test) VALUES(1)")
    #     self.connection.commit()
    #     cur.execute("SELECT * FROM test")
    #     result = cur.fetchall()
    #     cur.execute("DROP TABLE test")
    #     self.connection.commit()
    #     return (result[0][0] == 1)



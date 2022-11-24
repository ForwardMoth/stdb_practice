# from sqlalchemy import Column, ForeignKey, String, Integer
# from db import *
#
#
# class DbTable:
#     database = DataBase()
#     session = database.session
#
#     def add(self):
#
#

# class DbTable:
#     db = DataBase()
#     Base = db.Base
#     session = db.session
#
#     def create_all(self):
#         self.db.Base.metadata.create_all(self.db.engine)
#
#     def add(self):
#         self.db.session.add(self)
#         self.db.session.commit()

# def __init__(self):
#     self.table = self.set_table()
#
# def set_table(self):
#     self.dbconn.metadata.reflect(bind=self.dbconn.engine)
#     return self.dbconn.metadata.tables[self.table_name()]

# def column_id(self):
#     return Column('id', Integer(), primary_key=True, autoincrement=True)
#
# def columns(self):
#     if self.dbconn is not None:
#         s = self.table.select()
#         r = self.dbconn.connect.execute(s)
#         return r.keys()
#
# def column_names_without_id(self):
#     res = list(self.columns())
#     if 'id' in res:
#         res.remove('id')
#     return res
#
# def insert_one(self, data):
#     if self.dbconn is not None:
#         values = dict(zip(self.column_names_without_id(), data))
#         ins = self.table.insert().values(values)
#         r = self.dbconn.connect.execute(ins)
#
# def drop(self):
#     self.table.drop(self.dbconn.engine, checkfirst=False)
#
# def all(self):
#     if self.dbconn is not None:
#         s = self.table.select()
#         r = self.dbconn.connect.execute(s)
#         return r.fetchall()

# def columns(self):
#     if self.dbconn is not None:
#         s = select([people])
#         r = self.dbconn.connection.execute()
#         # self.dbconn.connection.execute()
#

# def column_names(self):
#     return sorted(self.columns().keys(), key = lambda x: x)
#
# def primary_key(self):
#     return ['id']
#
# def column_names_without_id(self):
#     res = list(self.columns().keys())
#     if 'id' in res:
#         res.remove('id')
#     return res
#
# def table_constraints(self):
#     return []
#
# def drop(self):
#     sql = "DROP TABLE IF EXISTS " + self.table_name()
#     cur = self.dbconn.conn.cursor()
#     cur.execute(sql)
#     self.dbconn.conn.commit()
#     return
# # поправить
# def insert_one(self, vals):
#     sql = "INSERT INTO " + self.table_name() + "("
#     sql += ", ".join(self.column_names_without_id()) + ") VALUES("
#     keys = self.column_names_without_id()
#     # name = "VALUES(:last_name, :first_name, :second_name, :group_name)"
#     dict = {}
#     for_sql = ""
#     for i in range(len(keys)):
#         dict[keys[i]] = vals[i]
#         for_sql += ":" + keys[i]
#         if i < len(keys) - 1:
#             for_sql += ", "
#     sql += for_sql + ")"
#     cur = self.dbconn.conn.cursor()
#     cur.execute(sql, dict)
#     self.dbconn.conn.commit()
#     return
#
# def first(self):
#     sql = "SELECT * FROM " + self.table_name()
#     sql += " ORDER BY "
#     sql += ", ".join(self.primary_key())
#     cur = self.dbconn.conn.cursor()
#     cur.execute(sql)
#     return cur.fetchone()
#
# def last(self):
#     sql = "SELECT * FROM " + self.table_name()
#     sql += " ORDER BY "
#     sql += ", ".join([x + " DESC" for x in self.primary_key()])
#     cur = self.dbconn.conn.cursor()
#     cur.execute(sql)
#     return cur.fetchone()
#
# def all(self):
#     sql = "SELECT * FROM " + self.table_name()
#     sql += " ORDER BY "
#     sql += ", ".join(self.primary_key())
#     cur = self.dbconn.conn.cursor()
#     cur.execute(sql)
#     return cur.fetchall()

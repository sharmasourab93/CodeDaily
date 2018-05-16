import sqlite3
import os
import sys
class databaseat:
    "This class looks after including tables, adding records and no of fields in the rocord"
    conn=sqlite3.connect('Dynamic Database')
    cursor=conn.cursor()
    def initfunc(self):
        #creating fields in the database
        cursor.execute("""create table sourab(name text,designation text, salary number)""")
        self.insertvals()
    def insertvals(self):
        #creating records
        cursor.execute("""insert into sourab(name,designation, salary)values('Sourab','CEO','100000')""")
        cursor.execute("""insert into sourab(name,designation, salary)values('Priyush','CXO','10000')""")
        cursor.execute("""create index userid on user(userid)""")
        conn.commit()
        cursor.close()
        conn.close()
    def main(self):
        self.initfunc()
k=databaseat()
k.main()
        

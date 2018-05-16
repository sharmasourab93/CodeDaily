import os
import sqlite3
name='sample_database'
conn=sqlite3.connect(name)
cursor=conn.cursor()
#create tables
if(not os.path.exists(name)):
    cursor.execute("""
    create table employee
    (empid integer, firstname varchar,
    lastname varchar, dept integer,phone varchar)""")
    cursor.execute("""create table department(departmentid integer,name varchar, manager integer)""")
    cursor.execute("""create table user (userid integer,
    username varchar, employeeid integer)""")
    #createing indices
    cursor.execute("""create index userid on user(userid)""")
    cursor.execute("""create index empid on employee(empid)""")
    cursor.execute("""create index deptid on department(departmentid)""")
    cursor.execute("""create index deptfk on employee(dept)""")
    cursor.execute("""create index deptmgr on department(manager)""")
    conn.commit()
    cursor.close()
    conn.close()

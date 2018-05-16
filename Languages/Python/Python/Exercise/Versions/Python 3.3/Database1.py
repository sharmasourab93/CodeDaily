import db #MySQLdb as db
con = db.connect(username="foo", passwd="secret")
cur = con.cursor()
cur.execute('CREATE DATABASE chom;')

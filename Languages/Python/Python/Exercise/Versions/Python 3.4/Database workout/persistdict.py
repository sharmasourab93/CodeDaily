import dbm
db=dbm.open('websites','c')
#Adding an Item
db['www.python.org']='Python Home Page'
print(db['www.python.org'])
#close and save to disk.
db.close()

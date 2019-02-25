import mysql.connector
from mysql.connector import Error


def connect():
				try:
								connection = mysql.connector.connect(host='10.0.0.7',
																																													database='mysql',
																																													user='pacuser',
																																													password='pacuser')
								if connection.is_connected():
												print('Connected to MySQL Database')
				
				except Error as e:
								print(e)
								

connect()
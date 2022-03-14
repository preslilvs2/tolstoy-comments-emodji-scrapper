from bs4 import BeautifulSoup
import sqlite3

with sqlite3.connect("data.db") as connect:
	cursor = connect.cursor()
	cursor.execute("""CREATE TABLE IF NOT EXIST stat(
			id INT PRIMARY KEY AUTOINCREMENT,
			date_scrap TIMESTAMP(8),
			name TEXT,
			url TEXT,
			amount INT
		)""")
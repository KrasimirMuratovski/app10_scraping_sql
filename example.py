import sqlite3

# Establish a connection and cursor
connection = sqlite3.connect("data.db")
cursor = connection.cursor()

## QUERY DATA
cursor.execute("SELECT * FROM events WHERE date Like '%2088%'")
rows = cursor.fetchall()
print(rows)
#
# new_rows = [('Cat', 'Cat city', '2088.10.17'),
#  ('Dog', 'Dog city', '2088.10.17')
#  ]


## INSERT INTO TABLE
# cursor.executemany("INSERT INTO events VALUES(?,?,?)", new_rows)
# connection.commit()



## CREATING TABLE
# create_table = """CREATE TABLE kmtest (
# 	column_1 INT PRIMARY KEY,
#    	column_2 CHAR(25) NOT NULL,
# 	column_3 CHAR(25) DEFAULT 0
# ); """
# # cursor.execute(create_table)


data = [(1, "1One", "1One_"),(2, "2One", "2One_"), ]
cursor.executemany("INSERT INTO kmtest VALUES(?,?,?)", data)
cursor.execute("SELECT * FROM kmtest ")
res = cursor.fetchall()
print(res)
connection.commit()





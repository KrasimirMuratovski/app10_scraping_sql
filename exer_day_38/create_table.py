import sqlite3

connection = sqlite3.connect("exer_38.db")
cursor = connection.cursor()

## CREATE TABLE
create_table = """ CREATE TABLE exer(
column_1 CHAR(25),
column_2 CHAR(25)
);
"""
cursor.execute(create_table)

##
cursor.execute("SELECT * FROM exer")
res = cursor.fetchall()
print(res)


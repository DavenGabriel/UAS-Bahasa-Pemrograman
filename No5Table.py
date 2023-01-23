import mysql.connector

db = mysql.connector.connect(
  host = "localhost",
  user = "root",
  passwd = " ",
  database = "tokoku"
)

cursor = db.cursor()
sql = """CREATE TABLE customers (
  Id_cust INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(255),
  alamat Varchar(255)
)
"""
cursor.execute(sql)

print("Tabel customers berhasil dibuat!")
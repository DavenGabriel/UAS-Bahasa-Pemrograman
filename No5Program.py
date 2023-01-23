import mysql.connector
import os

db = mysql.connector.connect(
  host = "localhost",
  user = "root",
  passwd = "",
  database = "tokoku"
)

def insert_data(db):
  name = input("Masukan nama: ")
  alamat = input("Masukan alamat: ")
  val = (name, alamat)
  cursor = db.cursor()
  sql = "INSERT INTO customers (name, alamat) VALUES (%s, %s)"
  cursor.execute(sql, val)
  db.commit()
  print("{} Data Berhasil Disimpan".format(cursor.rowcount))


def show_data(db):
  cursor = db.cursor()
  sql = "SELECT * FROM customers"
  cursor.execute(sql)
  results = cursor.fetchall()
  
  if cursor.rowcount < 0:
    print("Tidak ada data")
  else:
    for data in results:
      print(data)


def update_data(db):
  cursor = db.cursor()
  show_data(db)
  customer_id = input("Pilih Id Customer =>  ")
  name = input("Nama baru: ")
  address = input("Alamat baru: ")

  sql = "UPDATE customers SET name=%s, alamat=%s WHERE id_cust=%s"
  val = (name, address, customer_id)
  cursor.execute(sql, val)
  db.commit()
  print("{} Data Berhasil Diubah".format(cursor.rowcount))


def delete_data(db):
  cursor = db.cursor()
  show_data(db)
  customer_id = input("Pilih Id Customer => ")
  sql = "DELETE FROM customers WHERE id_cust=%s"
  val = (customer_id,)
  cursor.execute(sql, val)
  db.commit()
  print("{} Data Berhasil Dihapus".format(cursor.rowcount))


def search_data(db):
  cursor = db.cursor()
  keyword = input("Kata kunci: ")
  sql = "SELECT * FROM customers WHERE name LIKE %s OR alamat LIKE %s"
  val = ("%{}%".format(keyword), "%{}%".format(keyword))
  cursor.execute(sql, val)
  results = cursor.fetchall()
  
  if cursor.rowcount < 0:
    print("Tidak ada data")
  else:
    for data in results:
      print(data)


def show_menu(db):
  print("\nAPLIKASI DATABASE PYTHON")
  print("1. Masukkan Data")
  print("2. Tampilkan Data")
  print("3. Update Data")
  print("4. Hapus Data")
  print("5. Cari Data")
  print("0. Keluar")
  menu = input("Pilih => ")

  #clear screen
  os.system("clear")

  if menu == "1":
    insert_data(db)
  elif menu == "2":
    show_data(db)
  elif menu == "3":
    update_data(db)
  elif menu == "4":
    delete_data(db)
  elif menu == "5":
    search_data(db)
  elif menu == "0":
    exit()
  else:
    print("Salah Pilih Woi!")


if __name__ == "__main__":
  while(True):
    show_menu(db)
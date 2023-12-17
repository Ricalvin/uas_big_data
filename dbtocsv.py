import mysql.connector

import pandas as pd

 

# Buat koneksi ke server MySQL

db_connection = mysql.connector.connect(

    host="localhost",

    user="root",

    password="",

    database="uas_big_data_022"

)

 

# Buat objek cursor

db_cursor = db_connection.cursor()

 

# Contoh pernyataan SQL SELECT

select_query = "SELECT * FROM dbd"

 

# Eksekusi pernyataan SELECT

db_cursor.execute(select_query)

 

# Ambil hasil SELECT

results = db_cursor.fetchall()

 

# Tutup cursor dan koneksi

db_cursor.close()

db_connection.close()

 

# Konversi hasil SELECT menjadi dataframe pandas

df = pd.DataFrame(results, columns=["ID", "Kode Provinsi", "Nama Provinsi", "Kode Kabupaten Kota", "Nama Kabupaten Kota", "Jumlah Kasus", "Satuan", "Tahun"])

 

# Simpan dataframe sebagai file csv

df.to_csv("data_dbd.csv", index=False)

 

print("Data telah disimpan dalam file Excel 'data_dbd.csv'") #csv / xlsx

 
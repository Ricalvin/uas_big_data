import requests
import mysql.connector
 
# Konfigurasi database
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '',
    'database': 'uas_big_data_022'
}
 
# Alamat URL API
api_url = "https://data.jabarprov.go.id/api-backend/bigdata/dinkes/od_18509_jml_kasus_penyakit_demam_berdarah_dengue_dbd__kabupate?limit=200"
 
try:
    # Mengirim permintaan GET ke API
    response = requests.get(api_url)
 
    # Memeriksa status kode respons
    if response.status_code == 200:
        # Parse data JSON yang diterima
        dbd_data = response.json().get("data")
 
        # Membuka koneksi ke database
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
 
        # Menambahkan data pengguna ke dalam tabel
        for dbd in dbd_data:
            cursor.execute('''
                INSERT INTO dbd (id, kode_provinsi, nama_provinsi, kode_kabupaten_kota, nama_kabupaten_kota, jumlah_kasus, satuan, tahun)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            ''', (dbd['id'], dbd['kode_provinsi'], dbd['nama_provinsi'], dbd['kode_kabupaten_kota'], dbd['nama_kabupaten_kota'], dbd['jumlah_kasus'], dbd['satuan'], dbd['tahun']))
 
        # Menyimpan perubahan dan menutup koneksi
        conn.commit()
        conn.close()
 
        print("Data pengguna telah disimpan ke database MySQL.")
    else:
        print(f"Gagal mengambil data. Kode status: {response.status_code}")
 
except requests.exceptions.RequestException as e:
    print(f"Terjadi kesalahan saat menghubungi API: {str(e)}")
 
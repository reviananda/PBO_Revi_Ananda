import psycopg2
import os
import random

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    
def kembali():
    print("\n")
    input("Tekan tombol enter untuk kembali...")
    clear_screen()


DB_HOST = "localhost"
DB_NAME = "week12pbo"
DB_USER = "postgres"
DB_PASSWORD = "123"

connect = psycopg2.connect(
    dbname = DB_NAME,
    user = DB_USER,
    password = DB_PASSWORD,
    host = DB_HOST
)
cur = connect.cursor()

# CREATE TABLE
# cur.execute("CREATE TABLE public.supplier (kode_sup text DEFAULT 3, nama_sup text DEFAULT 30)")
# cur.execute("CREATE TABLE public.barang (kode_brg text DEFAULT 3, nama_brg text DEFAULT 30)")
# cur.execute("CREATE TABLE public.nota (no_nota text DEFAULT 3, tanggal text DEFAULT 30, tempo text DEFAULT 30, total integer DEFAULT 11, kode_sup text DEFAULT 3)")
# cur.execute("CREATE TABLE public.transaksi_brg (no_nota text DEFAULT 3, kode_brg text DEFAULT 3, qty integer DEFAULT 3, harga integer DEFAULT 30)")
# connect.commit()

# SELECT ALL
def select() :
    try :
        sql = ("SELECT nama_sup ,nama_brg, tanggal ,tempo, qty, harga, total FROM supplier, barang, transaksi_brg, nota WHERE supplier.kode_sup=nota.kode_sup AND barang.kode_brg=transaksi_brg.kode_brg AND nota.no_nota=transaksi_brg.no_nota")
        cur.execute(sql)
        print(f"\nData Barang")
        print("==============================================")
        for x in cur.fetchall() :
            print(f"Nama Supplier : {x[0]}")
            print(f"Nama Barang   : {x[1]}")
            print(f"Tanggal Masuk : {x[2]}")
            print(f"Kadaluarsa    : {x[3]}")
            print(f"Stok Barang   : {x[4]}")
            print(f"Harga         : {x[5]}")
            print(f"Total         : {x[6]}\n")
        print("==============================================\n\n")
        kembali()
    except :
        print("\nEror")
        kembali()
    

# SELECT ONE
def search(kd_brg) :
    try :
        cur.execute("SELECT nama_sup ,nama_brg, tanggal ,tempo, qty, harga, total FROM supplier, barang, transaksi_brg, nota WHERE supplier.kode_sup=nota.kode_sup AND barang.kode_brg=transaksi_brg.kode_brg AND nota.no_nota=transaksi_brg.no_nota AND barang.kode_brg=%s", [kd_brg])
        print(f"\nHasil Pencarian Dari {kd_brg}")
        print("==============================================")
        for x in cur.fetchall() :
            print(f"Nama Supplier : {x[0]}")
            print(f"Nama Barang   : {x[1]}")
            print(f"Tanggal Masuk : {x[2]}")
            print(f"Kadaluarsa    : {x[3]}")
            print(f"Stok Barang   : {x[4]}")
            print(f"Harga         : {x[5]}")
            print(f"Total         : {x[6]}\n")
        print("==============================================\n\n")
        kembali()
    except :
        print("\nEror / Data Tidak Di Temukan")
        kembali()

# INSERT
def insert() :
    try :
        print("\n=========================================================")
        no_nota = str(random.randint(1,999))
        kode_sup = input("Masukan Kode Supplier\t: ")
        nama_sup = input("Masukan Nama Supplier\t: ")
        kode_brg = input("Masukan Kode Barang\t: ")
        nama_brg = input("Masukan Nama Barang\t: ")
        tanggal = input("Masukan Tanggal Masuk\t: ")
        tempo = input("Masukan Kadaluarsa\t: ")
        qty = int(input("Masukan Stok Barang\t: "))
        harga = int(input("Masukan Harga Barang\t: "))
        total = qty * harga
        cur.execute("INSERT INTO supplier (kode_sup, nama_sup) VALUES (%s,%s)", [kode_sup, nama_sup])
        connect.commit()
        cur.execute("INSERT INTO barang (kode_brg, nama_brg) VALUES (%s,%s)", [kode_brg, nama_brg])
        connect.commit()
        cur.execute("INSERT INTO nota (no_nota, tanggal, tempo, total, kode_sup) VALUES (%s,%s,%s,%s,%s)", [no_nota, tanggal, tempo, total, kode_sup])
        connect.commit()
        cur.execute("INSERT INTO transaksi_brg (no_nota, kode_brg, qty, harga) VALUES (%s,%s,%s,%s)", [no_nota, kode_brg, qty, harga])
        connect.commit()
        print ("\nData Berhasil Di Tambahkan")
        kembali()
    except :
        print ("\nEror / Data Tidak Berhasil Di Tambahkan")
        kembali()

# UPDATE
def update(kd_brg):
        cur.execute("SELECT barang.kode_brg, nota.kode_sup ,nama_sup ,nama_brg, tanggal ,tempo, qty, harga, total FROM supplier, barang, transaksi_brg, nota WHERE supplier.kode_sup=nota.kode_sup AND barang.kode_brg=transaksi_brg.kode_brg AND nota.no_nota=transaksi_brg.no_nota AND barang.kode_brg=%s", [kd_brg])
        try :
            for x in cur.fetchall() :
                kode_brg = x[0]
                kode_sup = x[1]
                if kd_brg in x[0] :
                    print("\n==============================================")
                    qty = int(input("Masukan Stok Barang Baru\t: "))
                    harga = int(input("Masukan Harga Barang Baru\t: "))
                    total = qty * harga
                    cur.execute("UPDATE transaksi_brg SET qty = %s, harga = %s WHERE kode_brg LIKE %s", [qty, harga, kode_brg])
                    connect.commit()
                    cur.execute("UPDATE nota SET total = %s WHERE kode_sup LIKE %s", [total, kode_sup])
                    connect.commit()
                    print(f"\nKode {kd_brg} Berhasil Di Edit")
                    print("==============================================")
                    print(f"Nama Supplier : {x[2]}")
                    print(f"Nama Barang   : {x[3]}")
                    print(f"Tanggal Masuk : {x[4]}")
                    print(f"Kadaluarsa    : {x[5]}")
                    print(f"Stok Barang   : {qty}")
                    print(f"Harga         : {harga}")
                    print(f"Total         : {total}\n")
                    print("==============================================\n\n")
                    kembali()
        except :
            print("\nData Tidak Berhasil Di Edit")
            kembali()

# DELETE
def delete(kd_brg):
    cur.execute("SELECT barang.kode_brg, nota.kode_sup ,nama_sup ,nama_brg, tanggal ,tempo, qty, harga, total FROM supplier, barang, transaksi_brg, nota WHERE supplier.kode_sup=nota.kode_sup AND barang.kode_brg=transaksi_brg.kode_brg AND nota.no_nota=transaksi_brg.no_nota AND barang.kode_brg=%s", [kd_brg])
    try :
        for x in cur.fetchall() :
            kode_brg = x[0]
            kode_sup = x[1]
            if kd_brg in x[0] :
                cur.execute("DELETE FROM barang WHERE kode_brg = %s", [kode_brg])
                connect.commit()
                cur.execute("DELETE FROM supplier WHERE kode_sup = %s", [kode_sup])
                connect.commit()
                cur.execute("DELETE FROM nota WHERE kode_sup = %s", [kode_sup])
                connect.commit()
                cur.execute("DELETE FROM transaksi_brg WHERE kode_brg = %s", [kode_brg])
                connect.commit()
                print(f"\nKode {kd_brg} Berhasil Di Hapus")
                kembali()
    except :
        print("Data Tidak Berhasil Di Hapus")
        kembali()

while True :
    clear_screen()
    print("==============================\n    Menu Pilihan PostgreSQL \n==============================")
    print("1. Tampil Barang")
    print("2. Tambah Barang")
    print("3. Cari Barang")
    print("4. Edit Barang")
    print("5. Hapus Barang")
    print("0. Selesai")
    pilihan = input("Masukan Pilihan : ")

    if pilihan == '1' :
        select()
    elif pilihan == '2' :
        insert()
    elif pilihan == '3' :
        search(
            kd_brg = input("Masukan Kode Barang : ")
        )
    elif pilihan == '4' :
        update(
            kd_brg  = input("Masukan Kode Barang yg Ingin Di Ubah : ")
        )
    elif pilihan == '5' :
        delete(
            kd_brg  = input("Masukan Kode Barang yg Ingin Di Hapus : ")
        )
    elif pilihan == '0' :
        clear_screen()
        break
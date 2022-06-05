import random
import mysql.connector
import os
import datetime

connect = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "" ,
    database = "week12pbo"
)

def rupiah(uang) :
    x = str(uang)
    if len(x) <= 3 :
        return "Rp." + x + '.000'
    else :  #Kelompok 4
        a = x[:-3]
        b = x[-3:]
        return "Rp." + a + '.' + b 

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    
def kembali():
    print("\n")
    input("Tekan tombol enter untuk kembali...")
    clear_screen()

cur = connect.cursor()

# SELECT ALL
def select() :
    try :
        cur.execute("SELECT no_rekening,  nasabah.id_nasabah ,nama_nasabah, saldo, nama_cabang FROM nasabah, rekening, cabang_bank WHERE nasabah.id_nasabah=rekening.id_nasabah AND cabang_bank.kode_cabang=rekening.kode_cabang ")
        
        print(f"\nData Nasabah")
        print("==============================================")
        for x in cur.fetchall() :
            print(f"No Rekening    : {x[0]}")
            print(f"Id Nasabah     : {x[1]}")
            print(f"Nama Nasabah   : {x[2]}")
            print(f"Saldo Rekening : {rupiah(x[3])}")
            print(f"Cabang Bank    : {x[4]}\n")
        print("==============================================\n\n")
        kembali()
    except :
        print("\nEror")
        kembali()

# SELECT NASABAH
def select_nasabah(no_rekening) :
    try :
        cur.execute("SELECT no_rekening,  nasabah.id_nasabah ,nama_nasabah, saldo, nama_cabang FROM nasabah, rekening, cabang_bank WHERE nasabah.id_nasabah=rekening.id_nasabah AND cabang_bank.kode_cabang=rekening.kode_cabang AND rekening.no_rekening LIKE %s", [no_rekening])
        print(f"\nData Pencarian Nasabah")
        print("==============================================")
        for x in cur.fetchall() :
            print(f"No Rekening    : {x[0]}")
            print(f"Id Nasabah     : {x[1]}")
            print(f"Nama Nasabah   : {x[2]}")
            print(f"Saldo Rekening : {rupiah(x[3])}")
            print(f"Cabang Bank    : {x[4]}\n")
        print("==============================================\n\n")
        kembali()
    except :
        print("\nEror")
        kembali()

# INSERT
def insert_nasabah() :
    try :
        print("\n=========================================================")
        #Tabel Cabang Bank
        print("Data Bank")
        kode_cabang = input("Masukan Kode Cabang\t: ")
        nama_cabang = input("Masukan Nama Cabang\t: ")
        alamat_cabang = input("Masukan Alamat Cabang\t: ")
        cur.execute("INSERT INTO cabang_bank (kode_cabang, nama_cabang, alamat_cabang) VALUES (%s,%s,%s)", [kode_cabang, nama_cabang, alamat_cabang])
        connect.commit()

        #Tabel Nasabah
        print("\nData Nasabah")
        id_nasabah = input("Masukan Id Nasabah\t: ")
        nama_nasabah = input("Masukan Nama Nasabah\t: ")
        alamat_nasabah = input("Masukan Alamat Nasabah\t: ")
        cur.execute("INSERT INTO nasabah (id_nasabah, nama_nasabah, alamat_nasabah) VALUES (%s,%s,%s)", [id_nasabah, nama_nasabah, alamat_nasabah])
        connect.commit()

        #Tabel rekening
        print("\nData Rekening")
        no_rekening = input("Masukan No Rekening\t: ")
        pin = int(input("Masukan No Pin\t\t: "))
        saldo = int(input("Masukan Saldo Rekening\t: "))
        cur.execute("INSERT INTO rekening (no_rekening, pin, saldo, id_nasabah, kode_cabang) VALUES (%s,%s,%s,%s,%s)", [no_rekening, pin, saldo, id_nasabah, kode_cabang])
        connect.commit()
        

        print ("\nData Berhasil Di Tambahkan")
        kembali()
    except :
        print ("\nEror / Data Tidak Berhasil Di Tambahkan")
        kembali()

# UPDATE NASABAH
def update(id_nasabah) :
    cur.execute("SELECT * FROM nasabah WHERE id_nasabah LIKE %s", [id_nasabah])
    try :
       for x in cur.fetchall() :
        if id_nasabah == x[0] :
            pin = input("Masukan Pin Baru : ")
            cur.execute("UPDATE rekening SET pin = %s WHERE id_nasabah LIKE %s", [pin, id_nasabah])
            connect.commit()
            print("\nUpdate Berhasil")
        kembali()
    except :
        print("\nUpdate Gagal")

# TRANSAKSI
def transaksi(no_rekening):
        cur.execute("SELECT no_rekening ,nasabah.id_nasabah, nama_nasabah ,saldo FROM nasabah, rekening WHERE nasabah.id_nasabah=rekening.id_nasabah AND rekening.no_rekening LIKE %s", [no_rekening])
        try :
            for x in cur.fetchall() :
                id_nasabah = x[1]
                no_transaksi = str(random.randint(1,999))
                saldo = int(x[3])
                tanggal = datetime.datetime.now()
                if no_rekening in x[0] :
                    print("\n==============================================")
                    print("1. Setor Tunai")
                    print("2. Ambil Tunai")
                    menu = input("Masukan Pilihan : ")
                    if menu == '1' :
                        jenis_nasabah = "Setor Tunai"
                        transaksi = int(input("Masukan Jumlah : "))
                        hasil = saldo + transaksi
                        cur.execute("UPDATE rekening SET saldo = %s WHERE no_rekening LIKE %s", [hasil, no_rekening])
                        connect.commit()
                        cur.execute("INSERT INTO transaksi (no_transaksi, jenis_nasabah, tanggal, jumlah, id_nasabah) VALUES (%s,%s,%s,%s,%s)", [no_transaksi, jenis_nasabah, tanggal, transaksi, id_nasabah])
                        connect.commit()

                    elif menu == '2' :
                        jenis_nasabah = "Ambil Tunai"
                        transaksi = int(input("Masukan Jumlah : "))
                        hasil = saldo - transaksi
                        cur.execute("UPDATE rekening SET saldo = %s WHERE no_rekening LIKE %s", [hasil, no_rekening])
                        connect.commit()
                        cur.execute("INSERT INTO transaksi (no_transaksi, jenis_nasabah, tanggal, jumlah, id_nasabah) VALUES (%s,%s,%s,%s,%s)", [no_transaksi, jenis_nasabah, tanggal, transaksi, id_nasabah])
                        connect.commit()
                    
                print("\nTransaksi Berhasil")
                print(f"Saldo = {rupiah(hasil)}")
                kembali()
        except :
            print("\nTransaksi Gagal")
            kembali()

#SELECT TRANSAKSI
def select_transaksi(id_nasabah) :
    cur.execute("SELECT * FROM transaksi WHERE id_nasabah LIKE %s", [id_nasabah])
    print(f"\nData Transaksi Nasabah")
    print("==============================================")
    for x in cur.fetchall() :
            print(f"No Transaksi     : {x[0]}")
            print(f"Tanggal          : {x[2]}")
            print(f"Jenis Nasabah    : {x[1]}")
            print(f"Jumlah Transaksi : {rupiah(x[3])}\n")
    print("==============================================\n\n")
    kembali()

# DELETE
def delete(id_nasabah):
    cur.execute("SELECT nasabah.id_nasabah, no_rekening, kode_cabang, nama_nasabah FROM rekening, nasabah WHERE rekening.id_nasabah=nasabah.id_nasabah AND rekening.id_nasabah LIKE %s", [id_nasabah])
    try :
        for x in cur.fetchall() :
            no_rekening = x[1]
            kode_cabang = x[2]
            if id_nasabah in x[0] :
                cur.execute("DELETE FROM nasabah WHERE id_nasabah = %s", [id_nasabah])
                connect.commit()
                cur.execute("DELETE FROM rekening WHERE no_rekening = %s", [no_rekening])
                connect.commit()
                cur.execute("DELETE FROM transaksi WHERE id_nasabah = %s", [id_nasabah])
                connect.commit()
                cur.execute("DELETE FROM cabang_bank WHERE kode_cabang = %s", [kode_cabang])
                connect.commit()
                print(f"\nData Berhasil Di Hapus")
                kembali()
    except :
        print("Data Tidak Berhasil Di Hapus")
        kembali()

while True :
    clear_screen()
    print("==============================\n    Menu Pilihan MySQL \n==============================")
    print("1. Tampil Data Nasabah")
    print("2. Cari Data Nasabah")
    print("3. Tambah Nasabah")
    print("4. Transaksi")
    print("5. Tampil Transaksi")
    print("6. Edit Data Nasabah")
    print("7. Hapus Data Nasabah")
    print("0. Selesai")
    pilihan = input("Masukan Pilihan : ")

    if pilihan == '1' :
        select()
    elif pilihan == '2' :
        cur.execute("SELECT nasabah.id_nasabah, no_rekening, kode_cabang, nama_nasabah FROM rekening, nasabah WHERE rekening.id_nasabah=nasabah.id_nasabah")
        print("\n==============================================")
        for x in cur.fetchall() :
            print(f"No Rekening  : {x[1]} ")
            print(f"Nama Nasabah : {x[3]}\n")
        print("==============================================")
        select_nasabah(
            no_rekening = input("Masukan No Rekening : ")
        )
    elif pilihan == '3' :
        insert_nasabah()
    elif pilihan == '4' :
        cur.execute("SELECT nasabah.id_nasabah, no_rekening, kode_cabang, nama_nasabah FROM rekening, nasabah WHERE rekening.id_nasabah=nasabah.id_nasabah")
        print("\n==============================================")
        for x in cur.fetchall() :
            print(f"No Rekening  : {x[1]} ")
            print(f"Nama Nasabah : {x[3]}\n")
        print("==============================================")
        transaksi(
            no_rekening =  input("Masukan No Rekening : ")
        )
    elif pilihan == '5' :
        cur.execute("SELECT nasabah.id_nasabah, no_rekening, kode_cabang, nama_nasabah FROM rekening, nasabah WHERE rekening.id_nasabah=nasabah.id_nasabah")
        print("\n==============================================")
        for x in cur.fetchall() :
            print(f"Id Nasabah   : {x[0]} ")
            print(f"Nama Nasabah : {x[3]}\n")
        print("==============================================")
        select_transaksi(
            id_nasabah = input("Masukan Id Nasabah : ")
        )
    elif pilihan == '6' :
        cur.execute("SELECT nasabah.id_nasabah, no_rekening, kode_cabang, nama_nasabah FROM rekening, nasabah WHERE rekening.id_nasabah=nasabah.id_nasabah")
        print("\n==============================================")
        for x in cur.fetchall() :
            print(f"Id Nasabah   : {x[0]} ")
            print(f"Nama Nasabah : {x[3]}\n")
        print("==============================================")
        update(
            id_nasabah  = input("Masukan Id Nasabah yg Ingin Di Update : ")
        )
    elif pilihan == '7' :
        cur.execute("SELECT nasabah.id_nasabah, no_rekening, kode_cabang, nama_nasabah FROM rekening, nasabah WHERE rekening.id_nasabah=nasabah.id_nasabah")
        print("\n==============================================")
        for x in cur.fetchall() :
            print(f"Id Nasabah   : {x[0]} ")
            print(f"Nama Nasabah : {x[3]}\n")
        print("==============================================")
        delete(
            id_nasabah  = input("Masukan Id Nasabah yg Ingin Di Hapus : ")
        )
    elif pilihan == '0' :
        clear_screen()
        break


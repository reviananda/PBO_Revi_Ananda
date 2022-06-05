import mysql.connector
import os

connect = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "" ,
    database = "week12pbo"
)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    
def kembali():
    print("\n")
    input("Tekan tombol enter untuk kembali...")
    clear_screen()


cur = connect.cursor()

#CREATE TABLE

#sql = (f"CREATE TABLE golongan (kode_golongan VARCHAR(3), nama_golongan VARCHAR(10), tunjangan_suami INT(10), tunjangan_anak INT(10), uang_makan INT(10), uang_lembur INT(10), askes INT(10))")
#cur.execute(sql)
#cur.close()
#connect.close()

# SELECT ALL
def select() :
    try :
        sql = f"SELECT * FROM golongan"
        cur.execute(sql)
        print(f"\nData Golongan")
        print("==============================================")
        for x in cur.fetchall() :
            print(f"Kode golongan\t: {x[0]}")
            print(f"Nama Golongan\t: {x[1]}")
            print(f"Tunjangan suami\t: {x[2]}")
            print(f"Tunjangan Anak\t: {x[3]}")
            print(f"Uang Makan\t: {x[4]}")
            print(f"Uang Lembur\t: {x[5]}")
            print(f"Askes\t\t: {x[6]}")
        print("==============================================\n\n")
        kembali()
    except :
        print("\nEror")
        kembali()

# SELECT ONE
def search(nm_golongan) :
    try :
        sql = cur.execute(f"SELECT * FROM golongan  WHERE nama_golongan LIKE '%{nm_golongan}%'")
        cur.execute(sql)
        print(f"\nHasil Pencarian Dari {nm_golongan}")
        print("==============================================")
        for x in cur.fetchall() :
            print(f"Kode golongan\t: {x[0]}")
            print(f"Nama Golongan\t: {x[1]}")
            print(f"Tunjangan suami\t: {x[2]}")
            print(f"Tunjangan Anak\t: {x[3]}")
            print(f"Uang Makan\t: {x[4]}")
            print(f"Uang Lembur\t: {x[5]}")
            print(f"Askes\t\t: {x[6]}")
        print("==============================================\n\n")
        kembali()
    except :
        print("\nEror")
        kembali()

# INSERT
def insert() :
    try :
        kd_golongan = input("Masukan Kode Golongan\t: ")
        nm_golongan = input("Masukan Nama Golongan\t: ")
        tnj_suami = int(input("Masukan Tunjangan Suami\t: "))
        tnj_anak = int(input("Masukan Tunjangan Anak\t: "))
        uang_mkn = int(input("Masukan Uang Makan\t: "))
        uang_lbr = int(input("Masukan Uang Lembur\t: "))
        askes = int(input("Masukan Askes\t\t: "))
        sql = ("INSERT INTO golongan (kode_golongan, nama_golongan, tunjangan_suami, tunjangan_anak, uang_makan, uang_lembur, askes) VALUES (%s,%s,%s,%s,%s,%s,%s)")
        data = (kd_golongan, nm_golongan, tnj_suami, tnj_anak, uang_mkn, uang_lbr, askes)
        cur.execute(sql,data)
        connect.commit()
        print ("\nData Berhasil Di Tambahkan")
        kembali()
    except :
        print ("\nEror / Data Tidak Berhasil Di Tambahkan")
        kembali()

# UPDATE
def update(nm_golongan):
    cur.execute(f"SELECT * FROM golongan WHERE nama_golongan LIKE '%{nm_golongan}%'")
    try :
        for x in cur.fetchall() :
            if nm_golongan in x[1] :
                print("\n==============================================")
                tnj_suami = int(input("Masukan Tunjangan Suami Baru\t: "))
                tnj_anak = int(input("Masukan Tunjangan Anak Baru\t: "))
                uang_mkn = int(input("Masukan Uang Makan Baru\t\t: "))
                uang_lbr = int(input("Masukan Uang Lembur Baru\t: "))
                sql = ("UPDATE golongan SET tunjangan_suami = %s, tunjangan_anak = %s, uang_makan = %s, uang_lembur = %s WHERE nama_golongan LIKE %s")
                data = (tnj_suami, tnj_anak, uang_mkn, uang_lbr, nm_golongan)
                cur.execute(sql, data)
                connect.commit()
                print(f"\nGolongan {nm_golongan} Berhasil Di Edit")
                print("==============================================")
                print(f"Nama Golongan\t: {x[1]}")
                print(f"Tunjangan Suami\t: {tnj_suami}")
                print(f"Tunjangan Anak\t: {tnj_anak}")
                print(f"Uang Makan\t: {uang_mkn}")
                print(f"Uang Lembur\t: {uang_lbr}") 
                print("==============================================\n\n")
                kembali()
    except :
        print("\nData Tidak Berhasil Di Edit")
        kembali()

# DELETE
def delete(nm_golongan):
    cur.execute(f"SELECT * FROM golongan  WHERE nama_golongan LIKE '%{nm_golongan}%'")
    try :
        for x in cur.fetchall() :
            if nm_golongan in x[1] :
                cur.execute(f"DELETE FROM golongan WHERE nama_golongan LIKE '%{nm_golongan}%'")
                connect.commit()
                print(f"\nGolongan {nm_golongan} Berhasil Di Hapus")
                kembali()
    except :
        print("Data Tidak Berhasil Di Hapus")
        kembali()

while True :
    clear_screen()
    print("=======================\n    Menu MySQL \n=======================")
    print("1. Tampil Golongan")
    print("2. Tambah Golongan")
    print("3. Cari Golongan")
    print("4. Edit Golongan")
    print("5. Hapus Golongan")
    print("0. Selesai")
    pilihan = input("Masukan Pilihan : ")

    if pilihan == '1' :
        select()
    elif pilihan == '2' :
        insert()
    elif pilihan == '3' :
        search(
            nm_golongan = input("Masukan Nama Golongan : ")
        )
    elif pilihan == '4' :
        update(
            nm_golongan = input("Masukan Nama Golongan yg Ingin Di Ubah : ")
        )
    elif pilihan == '5' :
        delete(
            nm_golongan = input("Masukan Nama Golongan yg Ingin Di Hapus : ")
        )
    elif pilihan == '0' :
        clear_screen()
        break


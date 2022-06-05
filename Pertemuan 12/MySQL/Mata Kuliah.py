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

# SELECT ALL
def select() :
    try :
        sql = ("SELECT nama_mk, sks, semester, waktu, tempat, `nama_dos` FROM `kuliah`,  `mata kuliah`, `dosen` WHERE `kuliah`.`kode_mk`=`mata kuliah`.`kode_mk` AND `kuliah`.`kode_dos`=`dosen`.`kode_dos`")
        cur.execute(sql)
        print(f"\nData Jabatan")
        print("==============================================")
        for x in cur.fetchall() :
            print(f"Nama Mata Kuliah : {x[0]}")
            print(f"Dosen Pengampu   : {x[5]}")
            print(f"Sks              : {x[1]}")
            print(f"Semester         : {x[2]}")
            print(f"Waktu            : {x[3]}")
            print(f"Tempat           : {x[4]}\n")
        print("==============================================\n\n")
        kembali()
    except :
        print("\nEror")
        kembali()
    

# SELECT ONE
def search(kd_mk) :
    try :
        cur.execute("SELECT nama_mk, sks, semester, waktu, tempat, `nama_dos` FROM `kuliah`,  `mata kuliah`, `dosen` WHERE `kuliah`.`kode_mk`=`mata kuliah`.`kode_mk` AND `kuliah`.`kode_dos`=`dosen`.`kode_dos` AND `mata kuliah`.`kode_mk`= %s", [kd_mk])
        print(f"\nHasil Pencarian Dari {kd_mk}")
        print("==============================================")
        for x in cur.fetchall() :
            print(f"Nama Mata Kuliah : {x[0]}")
            print(f"Dosen Pengampu   : {x[5]}")
            print(f"Sks              : {x[1]}")
            print(f"Semester         : {x[2]}")
            print(f"Waktu            : {x[3]}")
            print(f"Tempat           : {x[4]}\n")
        print("==============================================\n\n")
        kembali()
    except :
        print("\nEror / Data Tidak Di Temukan")
        kembali()

# INSERT
def insert() :
    try :
        print("\n=========================================================")
        kode_mk = input("Masukan Kode Mata Kuliah\t: ")
        nama_mk = input("Masukan Nama Mata Kuliah\t: ")
        sks = input("Masukan SKS Mata Kuliah\t\t: ")
        semester = input("Masukan Semester Mata Kuliah\t: ")
        waktu = input("Masukan Waktu Mata Kuliah\t: ")
        tempat = input("Masukan Tempat Mata Kuliah\t: ")
        kode_dos = input("Masukan Kode Dosen\t\t: ")
        nama_dos = input("Masukan Nama Dosen\t\t: ")
        alamat_dos = input ("Masukan Alamat Dosen\t\t: ")
        no_tlp = input("Masukan No Telp Dosen\t\t: ")
        cur.execute("INSERT INTO dosen (kode_dos, nama_dos, alamat_dos, no_tlp) VALUES (%s,%s,%s,%s)", [kode_dos, nama_dos, alamat_dos, no_tlp])
        connect.commit()
        cur.execute("INSERT INTO `mata kuliah` (kode_mk, nama_mk, sks, semester) VALUES (%s,%s,%s,%s)", [kode_mk, nama_mk, sks, semester])
        connect.commit()
        cur.execute("INSERT INTO `kuliah` (kode_mk, kode_dos, waktu, tempat) VALUES (%s,%s,%s,%s)", [kode_mk, kode_dos, waktu, tempat])
        connect.commit()
        print ("\nData Berhasil Di Tambahkan")
        kembali()
    except :
        print ("\nEror / Data Tidak Berhasil Di Tambahkan")
        kembali()

# UPDATE
def update(kd_mk):
        cur.execute("SELECT kuliah.kode_mk, nama_mk, sks, semester, `nama_dos` FROM `kuliah`,  `mata kuliah`, `dosen` WHERE `kuliah`.`kode_mk`=`mata kuliah`.`kode_mk` AND `kuliah`.`kode_dos`=`dosen`.`kode_dos` AND `mata kuliah`.`kode_mk`= %s", [kd_mk])
        try :
            for x in cur.fetchall() :
                if kd_mk in x[0] :
                    print("\n==============================================")
                    waktu = input("Masukan Waktu Mata Kuliah Baru\t: ")
                    tempat = input("Masukan Tempat Mata Kuliah Baru\t: ")
                    cur.execute("UPDATE kuliah SET waktu = %s, tempat = %s WHERE kode_mk LIKE %s", [waktu, tempat, kd_mk])
                    connect.commit()
                    print(f"\nKode {kd_mk} Berhasil Di Edit")
                    print("==============================================")
                    print(f"Nama Mata Kuliah : {x[1]}")
                    print(f"Dosen Pengampu   : {x[4]}")
                    print(f"Sks              : {x[2]}")
                    print(f"Semester         : {x[3]}")
                    print(f"Waktu            : {waktu}")
                    print(f"Tempat           : {tempat}\n")
                    print("==============================================\n\n")
                    kembali()
        except :
            print("\nData Tidak Berhasil Di Edit")
            kembali()

# DELETE
def delete(kd_mk):
    cur.execute("SELECT kuliah.kode_mk, dosen.kode_dos FROM `kuliah`, `dosen` WHERE `kuliah`.`kode_dos`=`dosen`.`kode_dos` AND `kuliah`.`kode_mk`= %s", [kd_mk])
    try :
        for x in cur.fetchall() :
            kode_mk = x[0]
            kode_dos = x[1]
            if kd_mk in x[0] :
                cur.execute("DELETE FROM `kuliah` WHERE `kode_mk`= %s", [kode_mk])
                connect.commit()
                cur.execute("DELETE FROM `mata kuliah` WHERE `kode_mk`= %s", [kode_mk])
                connect.commit()
                cur.execute("DELETE FROM `dosen` WHERE `kode_dos`= %s", [kode_dos])
                connect.commit()
                print(f"\nKode {kd_mk} Berhasil Di Hapus")
                kembali()
    except :
        print("Data Tidak Berhasil Di Hapus")
        kembali()

while True :
    clear_screen()
    print("=======================\n    Menu Pilihan MySQL \n=======================")
    print("1. Tampil Mata Kuliah")
    print("2. Tambah Mata Kuliah")
    print("3. Cari Mata Kuliah")
    print("4. Edit Mata Kuliah")
    print("5. Hapus Mata Kuliah")
    print("0. Selesai")
    pilihan = input("Masukan Pilihan : ")

    if pilihan == '1' :
        select()
    elif pilihan == '2' :
        insert()
    elif pilihan == '3' :
        search(
            kd_mk = input("Masukan Kode Mata Kuliah : ")
        )
    elif pilihan == '4' :
        update(
            kd_mk  = input("Masukan Kode Mata Kuliah yg Ingin Di Ubah : ")
        )
    elif pilihan == '5' :
        delete(
            kd_mk  = input("Masukan Kode Mata Kuliah yg Ingin Di Hapus : ")
        )
    elif pilihan == '0' :
        clear_screen()
        break


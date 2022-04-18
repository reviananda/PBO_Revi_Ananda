import csv
import os
import sys


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    
def kembali():
    print("\n") 
    input("Tekan tombol apa saja untuk kembali..")
    clear_screen()
    
def menu_awal():
    while(True):    
        print("         Selamat Data di Perpustakan UTY         ")
        print("-------------------------------------------------")
        print(" 1 Untuk Tampilkan Buku")
        print(" 2 Untuk Pinjamkan Buku")
        print(" 3 Untuk Kembalikan Buku")
        print(" 4 Untuk Tambahkan Buku")
        print(" 5 Untuk Keluar")
        try:
            a=int(input("pilih menu 1-5: "))
            print() 
            if(a==1):
                display_buku()
                kembali()
            elif(a==2):
                listSplit()
                pinjamkan_buku()
                kembali()
            elif(a==3):
                listSplit()
                kembalikan_buku()
                kembali()
            elif(a==4):
                listSplit()
                tambah_buku()
                kembali()
            elif(a==5):
                print("Terimakasih telah menggunakan sistem perpustakan UTY")
                break
            else:
                print("Masukkan angka 1-5")
                kembali()
                continue
        except ValueError:
            print("masukkan sesuai petunjuk!")
            kembali()
            continue
        
def listSplit():
    global judul_buku
    global pengarang
    global jumlah_stok
    #global harga
    judul_buku=[]
    pengarang=[]
    jumlah_stok=[]
    #harga=[]
    with open("stock.txt","r+") as f:
        
        lines=f.readlines()
        lines=[x.strip('\n') for x in lines]
        for i in range(len(lines)):
            ind=0
            for a in lines[i].split(','):
                if(ind==0):
                    judul_buku.append(a)
                elif(ind==1):
                    pengarang.append(a)
                elif(ind==2):
                    jumlah_stok.append(a)
                # elif(ind==3):
                #   harga.append(a.strip("Rp"))
                ind+=1
                
def getDate():
    import datetime
    now=datetime.datetime.now
    return str(now().date())

def getTime():
    import datetime
    now=datetime.datetime.now
    return str(now().time())

def display_buku():
    with open("stock.txt", "r+") as f:
        lines=f.read()
        print(lines)
        print()
        
def tambah_buku():
    with open("stock.txt", "a+") as f:
        judul = input("judul = ")
        pengarang = input("pengarang = ")
        stok = input("stok = ")
        #harga = input("harga = Rp ")
        pembatas = ','
        #f.write('\n' + judul + pembatas + pengarang + pembatas + stok + pembatas + 'Rp' + harga)
        f.write('\n' + judul + pembatas + pengarang + pembatas + stok)
        
def pinjamkan_buku():
    success=False
    while(True):
        firstName=input("Masukkan nama depan peminjam: ")
        if firstName.isalpha():
            break
        print("Masukkan huruf A-Z")
    while(True):
        lastName=input("Masukan nama belakang peminjam: ")
        if lastName.isalpha():
            break
        print("Masukkan huruf A-Z")
        print("")
    display_buku()
    
    t="Pinjaman-"+firstName+".txt"
    with open(t,"w+") as f:
        f.write("           Perpustakaan UTY    \n")
        f.write("               Dipinjam oleh: "+ firstName+" "+lastName+" \n ")
        f.write("   Tanggal: "+getDate()+" Waktu:"+ getTime()+" \n\n")
        f.write("S.N. \t\t Judul buku \t       Pengarang \n")
        
    while success==False:
        print("Pilih menu di Bawah ini :")
        for i in range(len(judul_buku)):
            print("Masukkan", i, "untuk meminjam buku", judul_buku[i])
            
        try:
            a=int(input())
            try:
                if(int(jumlah_stok[a])>0):
                    print("Buku tersedia")
                    with open(t, "a") as f:
                        f.write("1. \t\t "+judul_buku[a]+" \t\t "+pengarang[a]+" \n ")

                        jumlah_stok[a]=int(jumlah_stok[a])-1
                        with open("stock.txt","r+") as f:
                            for i in range(8):
                                f.write(judul_buku[i]+","+pengarang[i]+","+str(jumlah_stok[i])+"\n")
                                continue


                    #jika buku yang dipinjam lebih dari 1
                    loop=True
                    count=1
                    while loop==True:
                        choice=str(input("Apakah ingin pinjam buku lagi? ketik y untuk ya dan n untuk tidak"))
                        if(choice.upper()=="Y"):
                            count=count+1
                            print("Pilih menu di bawah ini : ")
                            for i in range(len(judul_buku)):
                                print("Masukkan", i, "untuk meminjam buku", judul_buku[i])
                            a=int(input())
                            if(int(jumlah_stok[a])>0):
                                print("Buku tersedia")
                                with open(t, "a") as f:
                                    f.write(str(count) +". \t\t "+ judul_buku[a]+" \t\t "+pengarang[a]+"\n")
                                    
                                jumlah_stok[a]=int(jumlah_stok[a])-1
                                with open("stock.txt", "r+") as f:
                                    for i in range(8):
                                        f.wrote(judul_buku[i]+","+pengarang[i]+","+str(jumlah_stok[i])+"\n")
                                        success=False
                                        continue
                                   
                            else:
                                loop=False
                                continue
                        elif (choice.upper()=="N"):
                            print("Terimakasih telah meminjam buku.")
                            print("")
                            loop=False
                            success=True
                        else:
                            print("Masukkan sesuai petunjuk !")

                else:
                    print("Buku tidak tersedia")
                    pinjamkan_buku()
                    success=False
                    continue
            except IndexError:
                print("")
                print("Pilih buku sesuai nomor")
        except ValueError:
            print("")
            print("Pilih sesuai petunjuk !")
            
def kembalikan_buku():
    name=input("Masukkan nama peminjam: ")
    a="Pinjaman-"+name+".txt"
    try:
        with open(a, "r") as f:
            lines=f.readlines()
            lines=[a.strip("Rp") for a in lines]
            
        with open(a, "r") as f:
            data=f.read()
            print(data)
    except:
        print("Nama peminjam salah")
    
    b="Pengembalian-"+name+".txt"
    with open(b, "w+") as f:
        f.write("           Perpustakaan UTY \n")
        f.write("               Dikembalikan oleh: "+ name+"\n")
        f.write("   Tanggal: "+ getDate()+"     Waktu:"+ getTime()+"\n\n")
        f.write("S.N.\t\tJudul Buku\t\tTotal\n")
                
    total=0.0
    for i in range(8):
        if judul_buku[i] in data:
            with open(b, "a") as f:
                f.write(str(i+1)+"\t\t"+judul_buku[i]+"\n")
                jumlah_stok[i] = int(jumlah_stok[i])+1
            #total+=float(harga[i])

            
    print("\t\t\t\t\t\t\t"+"Rp"+str(total))
    print("Apakah buku melewati batas peminjaman?")
    print("Masukkan Y jika ya dan N jika tidak")
    stat=input()        
    if(stat.upper()=="Y"):
        print("Berapa hari keterlambatan?")
        hari=int(input())
        denda=3000*hari
        with open(b,"a+") as f:
            f.write("\t\t\t\tDenda: Rp"+ str(denda)+"\n")
        total=total+denda

        print("Total pembayaran: "+ "Rp"+str(total))
        with open(b,"a") as f:
            f.write("\t\t\t\tTotal: Rp"+str(total))
        
        with open("stock.txt","r+") as f:
            for i in range(8):      
                f.write(judul_buku[i]+","+pengarang[i]+","+str(jumlah_stok[i])+"\n")
              
menu_awal()
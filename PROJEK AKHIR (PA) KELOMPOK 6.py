from prettytable import from_csv
from prettytable import PrettyTable
import os
os.system('cls')
import pwinput
import csv
import json

# Nama file yang untuk disimpan ke dalam database
filename_csv_1 = 'jenispaket.csv'
filename_csv_2 = 'kelas.csv'
filename_csv_3 = 'pilihankelas.csv'
filename_csv_4 = 'pilihanutbk.csv'

# Dictionary untuk login sebagai staff/guru
staf_keltar = {"id":"Staff_172", "password":"Miku_Dayooo"}
guru_keltar = {"id":"Guru", "password":"dewa"}
# Jika login sebagai siswa menggunakan username dan password yang tertera di database 

# Fungsi jika login sebagai staff
class staff:
    def __init__(self,username,password):
        self.username = username
        self.password = password
    def create_paket_kelas(self, kode_paket, jenis_paket, harga, isi):
        self.kode_paket = kode_paket
        self.jenis_paket = jenis_paket
        self.harga = harga
        self.isi = isi
        print(f"Anda Telah Berhasil Menambahkan Paket {jenis_paket} dengan harga {harga}")
    def create_kelas(self, kode_kelas, kelas_baru, jadwal_baru):
        self.kode_kelas = kode_kelas
        self.kelas_baru = kelas_baru
        self.jadwal_baru = jadwal_baru
        print(f"Anda Berhasil Menambahkan Kelas {kelas_baru} dengan Kode {kode_kelas}")
    def update_paket_kelas(self, kode_paket, jenis_paket, harga, isi):
        self.kode_paket = kode_paket
        self.jenis_paket = jenis_paket
        self.harga = harga
        self.isi = isi
        print(f"Anda Berhasil Mengubah Paket dengan Kode {kode_paket} dengan Harga Baru = {harga}")
    def update_kelas(self,kode_kelas, kelas,jadwal):
        self.kode_kelas = kode_kelas
        self.kelas = kelas
        self.jadwal = jadwal
        print(f"Anda Telah Mengubah Jadwal Kelas dengan Kode {kode_kelas} Menjadi {jadwal}")
    def delete_paket_kelas(self, kode_paket):
        self.kode_paket = kode_paket
        print(f"Anda Berhasil Menghapus Paket {kode_paket}")
    def delete_kelas(self, kode_kelas):
        self.kode_kelas = kode_kelas
        print(f"Anda Berhasil Menghapus Kelas dengan Kode {kode_kelas}")
    def new_kelas_update(self,kode_kelas, kelas_baru, jadwal_baru):
        self.kode_kelas = kode_kelas
        self.kelas_baru = kelas_baru
        self.jadwal_baru = jadwal_baru
# Fungsi jika login sebagai guru
class guru:
    def __init__(self,username,password):
        self.username = username
        self.password = password
    def update_kelas(self,kode_kelas, kelas, jadwal):
        self.kode_kelas = kode_kelas
        self.kelas = kelas
        self.jadwal = jadwal
        print(f"Anda Telah Mengubah Jadwal Kelas dengan Kode {kode_kelas} Menjadi {jadwal}")
# Fungsi jika login sebagai siswa
class siswa:
    def __init__(self,username,password):
        self.username = username
        self.password = password

def sama_dengan():
    print("="*30)

# Fungsi untuk daftar kelas
def daftar_kelas():
    with open(filename_csv_3) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        print(csv_reader)
        for code in csv_reader:
            code = from_csv(csv_file)
            print(code)

# Fungsi untuk daftar paket
def daftar_paket():
    with open(filename_csv_1) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        print(csv_reader)
        for code in csv_reader:
            code = from_csv(csv_file)
            print(code)

# Fungsi untuk daftar utbk
def daftar_utbk():
    with open(filename_csv_4) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        print(csv_reader)
        for code in csv_reader:
            code = from_csv(csv_file)
            print(code)

# Fungsi untuk mengetahui nominal saldo
def nominal_saldo():
    with open("dump.json", mode="r") as getdata:
        data = json.load(getdata)
        print(f"Saldo Anda: Rp. ", data[username]["Saldo"])

# Fungsi untuk mengetahui paket belajar apa saja yang tersedia
def paket():
    print("=========================================================")
    print("|                Paket yang tersedia:                   |")
    print("|            1. Paket Regular                           |")
    print("|            2. Paket Premium                           |")
    print("|            3. Paket Intensif UTBK                     |")
    print("=========================================================")

# Fungsi untuk mengetahui apa saja yang dapat dilakukan oleh role siswa, guru, dan staff
def menu(role):
    if role == "Siswa":
        print("=====================================================================================")
        print("|                          Selamat Datang Di KELAS PINTAR                           |")
        print("=====================================================================================")
        print("|            1. Pembelian Paket Belajar                                             |")
        print("|            2. Isi Saldo E-Money                                                   |")
        print("|            3. Masuk Kelas (Bagi yang sudah membeli paket belajar)                 |")
        print("|            4. Keluar                                                              |")
        print("=====================================================================================")
    elif role == "Guru":
        print("=====================================================================================")
        print("|                                  Menu guru                                        |")
        print("=====================================================================================")
        print("|    Hai friendstar! Semangat melakukan pengajaran untuk masa depan generasi muda!  |")
        print("|    Di sini friendstar mau ngapain nih?                                            |")
        print("|    1. Tampilkan jadwal kelas                                                      |")
        print("|    2. Update jadwal kelas                                                         |")
        print("|    3. Keluar                                                                      |")
        print("=====================================================================================")
    elif role == "Staff":
        print("=====================================================================================")
        print("|                                    Menu staff                                     |")
        print("=====================================================================================")
        print("|Hai rekan kerja tercinta! Semangat kerjanya dan ucapkan Bismillah untuk memulai hari")
        print("|Di sini rekan kelas pintar mau ngapain nih?                                        |")
        print("|1. Tampilkan paket dan jadwal kelas                                                |")
        print("|2. Tambah jadwal kelas                                                             |")
        print("|3. Update jadwal kelas                                                             |")
        print("|4. Hapus kelas                                                                     |")
        print("|5. Tambah paket kelas                                                              |")
        print("|6. Update paket kelas                                                              |")
        print("|7. Hapus paket kelas                                                               |")
        print("|8. Keluar                                                                          |")
        print("=====================================================================================")
    else:
        print("Role Tidak Sesuai")
        return None

# Fungsi untuk proses login sebagai siswa, guru, atau staff
def login(role):
    #=================================================================
    #|                             LOGIN                             |
    #=================================================================
    # Fungsi untuk proses login sebagai siswa
    if role == "Siswa":
        tanya = input("Apakah Anda Memiliku Akun? (ya/tidak) = ")
        if tanya == "ya":
            global username
            username = input("Masukkan Username = ")
            password = pwinput.pwinput("Masukkan Password = ")
            with open("dump.json", mode="r") as getdata:
                data = json.load(getdata)
                if username == data[username]["Username"] and password == data[username]["Password"]:
                        print("Halo Pengguna KELAS PINTAR")
                        return siswa(username, password)
                else:
                    print("Username atau Password salah, Silahkan mengulang")
                    login(role)
        #=============================================================
        #|                         REGISTRASI                        |     
        #=============================================================
        # Fungsi untuk proses registrasi sebagai siswa
        elif tanya == "tidak":
            print("Silahkan Membuat Akun Terlebih Dahulu")
            username = input("Masukkan Username Baru: ")
            password = pwinput.pwinput("Masukkan Password baru: ")
            
            dic = {
                "Username": username,
                "Password": password,
                "Saldo": 0
            }
            
            with open("dump.json", mode="r") as getdata:
                data = json.load(getdata) # convert json to python
                
                data[username] = dic
                
                with open("dump.json", mode="w") as save:
                    json.dump(data, save) # convert python to json
                    print("Successfully Added!")
        else:
            print("input salah, silahkan mengulang")
            login(role)
    # Fungsi untuk proses login sebagai guru
    elif role == "Guru":
        username = input("Masukkan ID Guru = ")
        password = pwinput.pwinput("Masukkan Password Guru = ")
        if username == guru_keltar["id"] and password == guru_keltar["password"]:
            print("Selamat Datang Pak/Bu")
            return guru(username,password)
        else:
            print("Username atau Password salah")
            login(role)
    # Fungsi untuk proses login sebagai staff
    elif role == "Staff":
        username = input("Masukkan ID Staff = ")
        password = pwinput.pwinput("Masukkan Password Staff = ")
        if username == staf_keltar["id"] and password == staf_keltar["password"]:
            print("Selamat Datang Admin")
            return staff(username,password)
        else:
            print("Username atau Password salah, Silahkan mengulang")
            login(role)
    else:    
        print("Role Tidak Diketahui, Silahkan mengulang")

# Fungsi untuk menambah saldo
def saldo():
    while True:
        with open("dump.json", mode="r") as getdata:
            data = json.load(getdata)
        print("="*25)
        nominal_saldo()
        tabel_saldo = [
            [1, "100.000"],
            [2, "200.000"],
            [3, "500.000"]
        ]
        table = PrettyTable()
        table.field_names = ["No", "Nominal Saldo"]
        for i in tabel_saldo:
            table.add_row(i)
        print(table)
        #try:
        pengisian = int(input("Pilih nominal saldo yang diinginkan menggunakan angka = "))
        if pengisian == 1 :
            data[username]["Saldo"]
            print("="*25)
            print(f"Saldo anda sekarang Rp.{data[username]['Saldo']}")
            proses = data[username]["Saldo"] + 100000
            data[username]["Saldo"] = proses
            sama_dengan()
            print(f"Saldo setelah pengisian Rp.{data[username]['Saldo']}")
            with open("dump.json", "w") as update:
                json.dump(data, update)
            lanjutkan = str(input("Ingin mengisi lagi? (y/t) = " ))
            if lanjutkan=="y":
                saldo()
            elif lanjutkan == "t":
                siswa_1()
            else:
                print("Mohon mengimput hanya huruf y/t")
        elif pengisian == 2 :
            data[username]["Saldo"]
            print("="*25)
            print(f"Saldo anda sekarang Rp.{data[username]['Saldo']}")
            proses = data[username]["Saldo"] + 200000
            data[username]["Saldo"] = proses
            sama_dengan()
            print(f"Saldo setelah pengisian Rp.{data[username]['Saldo']}")
            with open("dump.json", "w") as update:
                json.dump(data, update)
            lanjutkan = str(input("Ingin mengisi lagi? (y/t) = " ))
            if lanjutkan=="y":
                saldo()
            elif lanjutkan == "t":
                siswa_1()
            else:
                print("Mohon mengimput hanya huruf y/t")
        elif pengisian == 3 :
            data[username]["Saldo"]
            print("="*25)
            print(f"Saldo anda sekarang Rp.{data[username]['Saldo']}")
            proses = data[username]["Saldo"] + 500000
            data[username]["Saldo"] = proses
            sama_dengan()
            print(f"Saldo setelah pengisian Rp.{data[username]['Saldo']}")
            with open("dump.json", "w") as update:
                json.dump(data, update)
            lanjutkan = str(input("Ingin mengisi lagi? (y/t) = " ))
            if lanjutkan=="y":
                saldo()
            elif lanjutkan == "t":
                siswa_1()
            else:
                print("Mohon mengimput hanya huruf y/t")
        else:
            print("Input salah")
            saldo()

# Fungsi untuk konfirmasi pembayaran paket regular
def konfirmasi_pembayaran_reguler():
    with open("dump.json", "r") as getfile:
        data = json.load(getfile)
    try:
        confirm = str(input("Apakah yakin ingin membeli? (y/t) = "))
        if confirm == "y":
            data[username]["Saldo"]
            if data[username]["Saldo"] >= 300000:
                proses = data[username]["Saldo"] - 300000
                data[username]["Saldo"] = proses
                dic = "Reguler"
                data[username]["Langganan"] = dic
                sama_dengan()
                with open("dump.json", "w") as update:
                    json.dump(data, update)
                print("Terima Kasih Telah Membeli")
                print(f"Saldo anda sekarang Rp.{data[username]['Saldo']}")
                product1_name, product1_price = 'Reguler', 300000
                company_name = 'KELAS PINTAR'
                company_address = 'Rimbawan 2 No.44, Karang Anyar'
                company_city = 'Samarinda'
                message = 'Thanks for shopping with us today!'
                print('*' * 50)
                print('\t\t{}'.format(company_name.title()))
                print('\t\t{}'.format(company_address.title()))
                print('\t\t{}'.format(company_city.title()))
                print('=' * 50)
                print('\tProduct Name\tProduct Price')
                print('\t{}\t\tRp.{}'.format(product1_name.title(), product1_price))
                print('=' * 50)
                print('\t\t\tTotal')
                total = product1_price
                print('\t\t\tRp.{}'.format(total))
                print('=' * 50)
                print('\n\t{}\n'.format(message))
            else:
                print("Saldo anda tidak cukup, silahkan melakukan pengisian")
                saldo()
        elif confirm == "t":
            print("Karena Anda Menolak, Anda Perlu Login Ulang")
            main()
        else:
            print("Input Salah, Silahkan Login Ulang")
            main()
    except:
        print("Terjadi Kesalahan, Silahkan Ulangi")

# Fungsi untuk konfirmasi pembayaran paket premium
def konfirmasi_pembayaran_premium():
    with open("dump.json", "r") as getfile:
        data = json.load(getfile)
    try:
        confirm = str(input("Apakah yakin ingin membeli? (y/t) = "))
        if confirm=="y":
            data[username]["Saldo"]
            if data[username]["Saldo"] >= 400000:
                proses = data[username]["Saldo"] - 400000
                data[username]["Saldo"] = proses
                dic = "Premium"
                data[username]["Langganan"] = dic
                sama_dengan()
                with open("dump.json", "w") as update:
                    json.dump(data, update)
                print("Terima Kasih Telah Membeli")
                print(f"Saldo anda sekarang Rp.{data[username]['Saldo']}")
                product2_name, product2_price = 'Premium', 400000
                company_name = 'KELAS PINTAR'
                company_address = 'Rimbawan 2 No.44, Karang Anyar'
                company_city = 'Samarinda'
                message = 'Thanks for shopping with us today!'
                print('*' * 50)
                print('\t\t{}'.format(company_name.title()))
                print('\t\t{}'.format(company_address.title()))
                print('\t\t{}'.format(company_city.title()))
                print('=' * 50)
                print('\tProduct Name\tProduct Price')
                print('\t{}\t\tRp.{}'.format(product2_name.title(), product2_price))
                print('=' * 50)
                print('\t\t\tTotal')
                total = product2_price
                print('\t\t\tRp.{}'.format(total))
                print('=' * 50)
                print('\n\t{}\n'.format(message))
            else:
                print("Saldo anda tidak cukup, silahkan melakukan pengisian")
                saldo()
        elif confirm=="t":
            print("Karena Anda Menolak, Anda Perlu Login Ulang")
            main()
        else:
            print("Input Salah, Silahkan Logim Ulang")
            main()
    except:
        print("Terjadi Kesalahan, Silahkan Ulangi")

# Fungsi untuk konfirmasi pembayaran paket intensif
def konfirmasi_pembayaran_intensif():
    with open("dump.json", "r") as getfile:
        data = json.load(getfile)
    try:
        confirm = str(input("Apakah yakin ingin membeli? (y/t) = "))
        if confirm=="y":
            data[username]["Saldo"]
            if data[username]["Saldo"] >= 400000:
                proses = data[username]["Saldo"] - 400000
                data[username]["Saldo"] = proses
                dic = "Intensif"
                data[username]["Langganan"] = dic
                sama_dengan()
                with open("dump.json", "w") as update:
                    json.dump(data, update)
                print("Terima Kasih Telah Membeli")
                print(f"Saldo anda sekarang Rp.{data[username]['Saldo']}")
                product1_name, product1_price = 'Intensif', 500000
                company_name = 'KELAS PINTAR'
                company_address = 'Rimbawan 2 No.44, Karang Anyar'
                company_city = 'Samarinda'
                message = 'Thanks for shopping with us today!'
                print('*' * 50)
                print('\t\t{}'.format(company_name.title()))
                print('\t\t{}'.format(company_address.title()))
                print('\t\t{}'.format(company_city.title()))
                print('=' * 50)
                print('\tProduct Name\tProduct Price')
                print('\t{}\t\tRp.{}'.format(product1_name.title(), product1_price))
                print('=' * 50)
                print('\t\t\tTotal')
                total = product1_price
                print('\t\t\tRp.{}'.format(total))
                print('=' * 50)
                print('\n\t{}\n'.format(message))
            else:
                print("Saldo anda tidak cukup, silahkan melakukan pengisian")
                saldo()
        elif confirm=="t":
            print("Karena Anda Menolak, Anda Perlu Login Ulang")
            main()
        else:
            print("Input Salah, Silahkan Login Ulang")
            main()
    except:
        print("Terjadi Kesalahan, Silahkan Ulangi")

# Fungsi untuk login sebagai siswa_1 dapat melakukan pembelian paket
def siswa_1():
    with open(filename_csv_1) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        print(csv_reader)
        for code in csv_reader:
            code = from_csv(csv_file)
            print(code)
    print("=========================================================")
    print("|    Halo! silahkan memilih paket yang ingin dibeli.    |")
    paket()
    print("|             Jika ingin keluar ketik '4'               |")
    print("=========================================================")
    try:
        opsi_beli = int(input("Masukkan nomor yang tertera untuk memilih = "))
        # Fungsi untuk membeli paket Regular
        if opsi_beli==1:
            daftar_kelas()
            print("Silahkan memilih satu kelas yang ingin dipelajari")
            try:
                pemilihan_kelas = int(input("Pilih kelas dengan memasukkan nomor kelas = "))
                if pemilihan_kelas==1:
                    sama_dengan()
                    print("Anda memilih kelas Bahasa Inggris")
                    print("Silahkan melakukan pembayaran")
                    konfirmasi_pembayaran_reguler()
                elif pemilihan_kelas==2:
                    sama_dengan()
                    print("Anda memilih kelas Bahasa Indonesia")
                    print("Silahkan melakukan pembayaran")
                    konfirmasi_pembayaran_reguler()
                elif pemilihan_kelas==3:
                    sama_dengan()
                    print("Anda memilih kelas Matematika Wajib")
                    print("Silahkan melakukan pembayaran")
                    konfirmasi_pembayaran_reguler()
                elif pemilihan_kelas==4:
                    sama_dengan()
                    print("Anda memilih kelas Matematika Peminatan")
                    print("Silahkan melakukan pembayaran")
                    konfirmasi_pembayaran_reguler()
                elif pemilihan_kelas==5:
                    sama_dengan()
                    print("Anda memilih kelas Kimia")
                    print("Silahkan melakukan pembayaran")
                    konfirmasi_pembayaran_reguler()
                elif pemilihan_kelas==6:
                    sama_dengan()
                    print("Anda memilih kelas Fisika")
                    print("Silahkan melakukan pembayaran")
                    konfirmasi_pembayaran_reguler()
                elif pemilihan_kelas==7:
                    sama_dengan()
                    print("Anda memilih kelas Biologi")
                    print("Silahkan melakukan pembayaran")
                    konfirmasi_pembayaran_reguler()
                elif pemilihan_kelas==8:
                    sama_dengan()
                    print("Anda memilih kelas Ekonomi")
                    print("Silahkan melakukan pembayaran")
                    konfirmasi_pembayaran_reguler()
                elif pemilihan_kelas==9:
                    sama_dengan()
                    print("Anda memilih kelas Geografi")
                    print("Silahkan melakukan pembayaran")
                    konfirmasi_pembayaran_reguler()
                elif pemilihan_kelas==10:
                    sama_dengan()
                    print("Anda memilih kelas Sejarah")
                    print("Silahkan melakukan pembayaran")
                    konfirmasi_pembayaran_reguler()
            except ValueError:
                print("Tolong memasukkan angka, selain itu ditolak")
            except KeyboardInterrupt:
                print("Terjadi Kesalahan, Silahkan ulangi")
        # Fungsi untuk membeli paket Premium
        elif opsi_beli==2:
            daftar_kelas()
            print("Setelah pembayaran, anda dapat mengakses semua kelas")
            print("Silahkan melakukan pembayaran")
            konfirmasi_pembayaran_premium()
        # Fungsi untuk membeli paket Intensif UTBK
        elif opsi_beli==3:
            daftar_utbk()
            print("Silahkan melakukan pembayaran")
            konfirmasi_pembayaran_intensif()
        # Fungsi untuk keluar dari menu pembelian paket
        elif opsi_beli==4:
            main()
        else:
            print("Input salah")
    except ValueError:
        print("="*25)
        print("Tolong Memasukkan Angka")
    except KeyboardInterrupt:
        print("Terjadi Kesalahan, Silahkan ulangi")

# Fungsi untuk login sebagai siswa_3 dapat mengakses pembelajaran di KELASPINTAR
def siswa_3():
    with open("dump.json", "r") as getfile:
        data = json.load(getfile)
    ulang_pass = pwinput.pwinput("Masukkan Ulang Password = ")
    if ulang_pass == data[username]["Password"] and data[username]["Langganan"] == "Reguler":
        print(f"Selamat Datang {data[username]['Username']}, Pengguna Reguler KELAS PINTAR")
        tanya = str(input("Apakah Ingin Mengakhiri Sesi? (y/t) = "))
        if tanya == "y":
            print("Anda Telah Keluar")
            main()
        elif tanya == "t":
            print("Untuk Keamanan, Silahkan Masukkan Ulang Password")
            siswa_3()
        else:
            print("Input Salah")
            siswa_3()
    elif ulang_pass == data[username]["Password"] and data[username]["Langganan"] == "Premium":
        print(f"Selamat Datang {data[username]['Username']}, Pengguna Platinum KELAS PINTAR")
        tanya = str(input("Apakah Ingin Mengakhiri Sesi? (y/t) = "))
        if tanya == "y":
            print("Anda Telah Keluar")
            main()
        elif tanya == "t":
            print("Untuk Keamanan, Silahkan Masukkan Ulang Password")
            siswa_3()
        else:
            print("Input Salah")
            siswa_3()
    elif ulang_pass == data[username]["Password"] and data[username]["Langganan"] == "Intensif":
        print(f"Selamat Datang {data[username]['Username']}, Pengguna Intensif KELAS PINTAR")
        tanya = str(input("Apakah Ingin Mengakhiri Sesi? (y/t) = "))
        if tanya == "y":
            print("Anda Telah Keluar")
            main()
        elif tanya == "t":
            print("Untuk Keamanan, Silahkan Masukkan Ulang Password")
            siswa_3()
        else:
            print("Input Salah")
            siswa_3()
    elif ulang_pass == data[username]["Password"] and data[username]["Langganan"] == "Gratis":
        print(f"Anda Belum Memiliki Akses Menuju Menu Ini, Harap Membeli Paket Terlebih Dahulu")
        siswa_1()

# Fungsi menu utama (main) untuk login sebagai role staff, guru, atau siswa
def main():
    print(60*"=")
    print("|             Selamat Datang Di KELAS PINTAR               |")
    print("|    Aplikasi Belajar Online yang Menyenangkan dan Seru!   |")
    print("|                         ₊‧°𐐪♡𐑂°‧₊                        |")
    print(60*"=")
    while True:
        try:
            role = input('''
            =================================
            |           Welcome To          |
            |           KELASPINTAR         |
            =================================
            |>>>>>>Silakan pilih role<<<<<<<|
            |                               |
            |   1. Staff                    |
            |   2. Guru                     |
            |   3. Siswa                    |
            |   4. Exit                     |
            |                               |
            =================================
            Anda Masuk Sebagai? (Siswa/Guru/Staff/Exit) = ''')
            if role == "Staff":
                user = login(role)
                menu(role)
            elif role == "Guru":
                user = login(role)
                menu(role)
            elif role == "Siswa":
                user = login(role)
                menu(role)
            elif role == "Exit":
                print("Terima Kasih, Semoga Sehat Selalu")
                break
            else:
                print("Role Tidak Diketahui")
                main()
            while True:
                try:
                    pilihan = int(input("Pilih Menu = "))
                    # Jika login sebagai staff dapat melakukan CRUD
                    if role == "Staff":
                        # Tampilkan paket dan jadwal kelas
                        if pilihan == 1:
                            with open(filename_csv_1) as csv_file:
                                csv_reader = csv.reader(csv_file, delimiter=",")
                                print(csv_reader)
                                for code in csv_reader:
                                    code = from_csv(csv_file)
                                    print(code)
                            print("-------------------------------------------------------")
                            with open(filename_csv_2) as csv_file:
                                csv_reader = csv.reader(csv_file, delimiter=",")
                                print(csv_reader)
                                for code in csv_reader:
                                    code = from_csv(csv_file)
                                    print(code)
                        # Tambah jadwal kelas
                        elif pilihan == 2:
                            with open(filename_csv_2, mode='a', newline='') as csv_file:
                                fieldnames = ['Kode Kelas', 'Kelas', 'Jadwal Belajar']
                                writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                                kode_kelas = input("Masukkan Kode Kelas Baru = ")
                                kelas_baru = input("Masukkan Nama Kelas Baru = ")
                                jadwal_baru = input("Masukkan Jadwal Kelas Baru = ")
                                writer.writerow({'Kode Kelas': kode_kelas, 'Kelas': kelas_baru, 'Jadwal Belajar': jadwal_baru})
                                user.create_kelas(kode_kelas, kelas_baru, jadwal_baru)
                        # Update jadwal kelas
                        elif pilihan == 3:
                            update = []
                            with open(filename_csv_2, mode="r") as csv_file:
                                csv_reader = csv.DictReader(csv_file)
                                for row in csv_reader:
                                    update.append(row)
                                for data in update:
                                    print(f"{data['Kode Kelas']} \t {data['Kelas']} \t {data['Jadwal Belajar']}")
                                print("-------------------------")
                                kode_kelas = input("Masukkan Kode yang Ingin Diubah > ")
                                kelas = input("Masukkan Ulang Kelas yang Ingin Diubah = ")
                                jadwal = input("Masukkan Jadwal Baru (__:__) = ")
                                indeks = 0
                                for data in update:
                                    if (data['Kode Kelas'] == kode_kelas):
                                        update[indeks]['Kelas'] = kelas
                                        update[indeks]['Jadwal Belajar'] = jadwal
                                    indeks = indeks + 1
                                with open(filename_csv_2, mode="w", newline='') as csv_file:
                                    fieldnames = ['Kode Kelas','Kelas','Jadwal Belajar']
                                    writer = csv.DictWriter(csv_file,fieldnames=fieldnames)
                                    writer.writeheader()
                                    for new_data in update:
                                        writer.writerow({'Kode Kelas': new_data['Kode Kelas'],'Kelas': new_data['Kelas'], 'Jadwal Belajar': new_data['Jadwal Belajar']})
                                user.update_kelas(kode_kelas, kelas, jadwal)
                        # Hapus kelas
                        elif pilihan == 4:
                            delete = []
                            with open(filename_csv_2, mode="r") as csv_file:
                                csv_reader = csv.DictReader(csv_file)
                                for row in csv_reader:
                                    delete.append(row)
                                for data in delete:
                                    print(f"{data['Kode Kelas']} \t {data['Kelas']} \t {data['Jadwal Belajar']}")
                                print("-------------------------")
                                kode_kelas = input("Masukkan Kode Kelas yang Ingin Dihapus > ")
                                indeks = 0
                                for data in delete:
                                    if (data['Kode Kelas'] == kode_kelas):
                                        delete.remove(delete[indeks])
                                    indeks = indeks + 1
                                with open(filename_csv_2, mode="w", newline='') as csv_file:
                                    fieldnames = ['Kode Kelas', 'Kelas', 'Jadwal Belajar']
                                    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                                    for new_data in delete:
                                        writer.writerow({'Kode Kelas': new_data['Kode Kelas'], 'Kelas': new_data['Kelas'], 'Jadwal Belajar': new_data['Jadwal Belajar']})
                                user.delete_kelas(kode_kelas)
                        # Tambah paket kelas
                        elif pilihan == 5:
                            with open(filename_csv_1, mode='a', newline='') as csv_file:
                                fieldnames = ['Kode Paket', 'Jenis Paket', 'Harga', 'Isi Paket']
                                writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                                kode_paket = input("Masukkan Kode Paket Baru = ")
                                jenis_paket = input("Masukkan Jenis Paket Baru = ")
                                harga = input("Masukkan Harga Baru = ")
                                isi = input("Masukkan Isi Paket Baru = ")
                                writer.writerow({'Kode Paket': kode_paket, 'Jenis Paket': jenis_paket, 'Harga': harga, 'Isi Paket': isi})
                                user.create_paket_kelas(kode_paket, jenis_paket, harga, isi)
                        # Update paket kelas
                        elif pilihan == 6:
                            update2 = []
                            with open(filename_csv_1, mode="r") as csv_file:
                                csv_reader = csv.DictReader(csv_file)
                                for row in csv_reader:
                                    update2.append(row)
                                for data in update2:
                                    print(f"{data['Kode Paket']} \t {data['Jenis Paket']} \t {data['Harga']} \t {data['Isi Paket']}")
                                print("-----------------------")
                                kode_paket = input("Masukkan Kode Kelas yang Ingin Diubah > ")
                                jenis_paket = input("Masukkan Jenis Paket yang Ingin Diubah > ")
                                harga = input("Masukkan Harga Baru = ")
                                isi = input("Masukkan Isi Paket Baru = ")
                                indeks = 0
                                for data in update2:
                                    if (data['Kode Paket'] == kode_paket):
                                        update2[indeks]['Jenis Paket'] = jenis_paket
                                        update2[indeks]['Harga'] = harga
                                        update2[indeks]['Isi Paket'] = isi
                                    indeks = indeks + 1
                                with open(filename_csv_1, mode="w", newline='') as csv_file:
                                    fieldnames = ['Kode Paket', 'Jenis Paket', 'Harga','Isi Paket']
                                    writer = csv.DictWriter(csv_file,fieldnames=fieldnames)
                                    writer.writeheader()
                                    for new_data in update2:
                                        writer.writerow({'Kode Paket': new_data['Kode Paket'], 'Jenis Paket': new_data['Jenis Paket'], 'Harga': new_data['Harga'], 'Isi Paket':new_data['Isi Paket']})
                                user.update_paket_kelas(kode_paket, jenis_paket, harga, isi)
                        # Hapus paket kelas
                        elif pilihan == 7:
                            delete2 = []
                            with open(filename_csv_1, mode="r") as csv_file:
                                csv_reader = csv.DictReader(csv_file)
                                for row in csv_reader:
                                    delete2.append(row)
                                for data in delete2:
                                    print(f"{data['Kode Paket']} \t {data['Jenis Paket']} \t {data['Harga']} \t {data['Isi Paket']}")
                                print("-------------------------")
                                kode_paket = input("Masukkan Kode Paket yang Ingin Dihapus > ")
                                indeks = 0
                                for data in delete2:
                                    if (data['Kode Paket'] == kode_paket):
                                        delete2.remove(delete2[indeks])
                                    indeks = indeks + 1
                                with open(filename_csv_1, mode="w", newline='') as csv_file:
                                    fieldnames = ['Kode Paket', 'Jenis Paket', 'Harga', 'Isi Paket']
                                    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                                    writer.writeheader()
                                    for new_data in delete2:
                                        writer.writerow({'Kode Paket': new_data['Kode Paket'], 'Jenis Paket': new_data['Jenis Paket'], 'Harga': new_data['Harga'], 'Isi Paket': new_data['Isi Paket']})
                                user.delete_paket_kelas(kode_paket)
                        elif pilihan == 8:
                            print("Anda Telah Keluar")
                            break
                        else:
                            print("Input Salah")
                            return None
                    # Jika login sebagai guru dapat menampilkan jadwal kelas dan update jadwal kelas
                    elif role == "Guru":
                        # Tampilkan jadwal kelas
                        if pilihan == 1:
                            with open(filename_csv_2) as csv_file:
                                csv_reader = csv.reader(csv_file, delimiter=",")
                                print(csv_reader)
                                for code in csv_reader:
                                    code = from_csv(csv_file)
                                    print(code)
                        # Update jadwal kelas
                        elif pilihan == 2:
                            update3 = []
                            with open(filename_csv_2, mode="r") as csv_file:
                                csv_reader = csv.DictReader(csv_file)
                                for row in csv_reader:
                                    update3.append(row)
                                for data in update3:
                                    print(f"{data['Kode Kelas']} \t {data['Kelas']} \t {data['Jadwal Belajar']}")
                                print("-------------------------")
                                kode_kelas = input("Masukkan Kode yang Ingin Diubah > ")
                                kelas = input("Masukkan Ulang Kelas yang Ingin Diubah = ")
                                jadwal = input("Masukkan Jadwal Baru (__:__) = ")
                                indeks = 0
                                for data in update3:
                                    if (data['Kode Kelas'] == kode_kelas):
                                        update3[indeks]['Kelas'] = kelas
                                        update3[indeks]['Jadwal Belajar'] = jadwal
                                    indeks = indeks + 1
                                with open(filename_csv_2, mode="w", newline='') as csv_file:
                                    fieldnames = ['Kode Kelas','Kelas','Jadwal Belajar']
                                    writer = csv.DictWriter(csv_file,fieldnames=fieldnames)
                                    writer.writeheader()
                                    for new_data in update3:
                                        writer.writerow({'Kode Kelas': new_data['Kode Kelas'],'Kelas': new_data['Kelas'], 'Jadwal Belajar': new_data['Jadwal Belajar']})
                                user.update_kelas(kode_kelas, kelas, jadwal)
                        elif pilihan == 3:
                            print("Anda Telah Keluar")
                            break
                        else:
                            print("Input Salah")
                            return None
                        # Jika login sebagai siswa
                    elif role == "Siswa":
                        if pilihan == 1:
                            siswa_1()
                        elif pilihan == 2:
                            saldo()
                        elif pilihan == 3:
                            siswa_3()
                        elif pilihan == 4:
                            print("Anda Telah Keluar")
                            main()
                except ValueError:
                    print("Harap Masukkan angka")
        except KeyboardInterrupt:
            print("")
            print("Mohon untuk tidak mencoba kombinasi keyboard")
main()

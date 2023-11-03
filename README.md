# Projek-Akhir-Kelompok-6

DESKRIPSI PROGRAM
	Pada saat memulai program, akan ditampilkan sebuah pilihan menu untuk melakukan login kedalam program. Kita dapat masuk sebagai staff, guru, siswa. Di program juga terdapat menu exit untuk keluar dari program.
 
JIKA MASUK SEBAGAI STAFF
	Jika kita ingin masuk sebagai staff, maka kita perlu login menggunakan akun yang sudah ditentukan sebagai staff di database program python. Setelah masuk kedalam program sebagai staff, akan ditampilkan 1-8 menu yang dapat dipilih oleh staff. Untuk memilih menu, kita harus menginput angka yang terdapat di menu (Contoh : input angka “1” untuk menampilkan). Yang pertama ialah menu untuk menampilkan (read) paket dan jadwal kelas. Angka kedua untuk menambah jadwal kelas, angka ketiga untuk mengupdate jadwal kelas yang ada, dan angka ke empat untuk menghapus jadwal kelas yang ada.
	Selain itu, di angka kelima staff  dapat menambah paket kelas, angka keenam untuk mengupdate kelas yang ada, angka ketujuh untuk menghapus kelas yang ada, dan yang terakhir di angka 8 ialah angka untuk kembali ke menu login.
 
JIKA MASUK SEBAGAI GURU
	Jika kita ingin masuk sebagai guru, harus menggunakan akun yang sudah ditentukan sebagai guru di database program python. Setelah masuk ke program sebagai guru, akan menu khusus untuk guru. Untuk memilih menu yang ada, harus memasukkan angka yang sudah tertera. Yang pertama ialah menampilkan jadwal kelas, kedua untuk mengupdate jadwal kelas yang telah ditentukan, dan yang ketiga untuk keluar ke menu login.
 
JIKA MASUK SEBAGAI SISWA
	Yang terakhir jika kita masuk sebagai siswa, kita akan diberi pilihan. Apabila sudah memiliki akun atau belum. Jika sudah mempunyai akun kita akan, pengguna dapat langsung login dengan memasukkan username dan password yang telah dibuat dan akan langsung menuju menu siswa. Jika belum mempunyai akun, pengguna harus melakukan registrasi terlebih dahulu. Setelah registrasi berhasil kita akan langsung masuk ke menu siswa.
	Siswa akan diberikan tampilan menu khusus siswa, yang pertama ada pilihan untuk pembelian paket belajar, jika kita memasukkan angka satu maka akan diberikan tampilan paket belajar, Jika memasukkan angka empat akan keluar, namun jika angka 1-3 maka akan diberikan tampilan kelas yang disediakan, lalu pengguna dapat memasukkan angka sesuai kelas yang dipilih dan melakukan pembayaran. Setelah pembayaran akan ada invoice yang dihasilkan.
	Apabila siswa memilih pilihan kedua, siswa dapat melakukan pengisian saldo e-money. Saldo e-money digunakan untuk pembelian nantinya. Terdapat tiga pilihan nominal saldo yang dapat dipilih, yaitu Rp. 100.000, Rp. 200.000, dan Rp. 500.000. Setelah memilih salah satu dari ketiganya, akan ada konfirmasi pengisian saldo. Pengisian saldo ditujukan untuk melakukan transaki pembelian paket belajar.
	Selanjutnya apabila siswa memilih pilihan ketiga, maka siswa telah masuk kedalam kelas.
 
Adapun fitur-fitur yang diimplementasikan ke dalam program aplikasi belajar online adalah sebagai berikut:
1.While
Perulangan while pada python adalah proses pengulangan suatu blok kode program selama sebuah kondisi terpenuhi. Perulangan while sangat berkaitan dengan variabel boolean, atau logical statement. Karena penentuan kapan suatu blok kode akan diulang-ulang ditinjau dari True or False atau suatu pernyataan logika. 
2.PrettyTable
PrettyTable adalah library Python untuk membuat tabel relasional sederhana dengan Python. Kita dapat mengontrol banyak aspek tabel, seperti lebar padding kolom, perataan teks, atau batas tabel. Kita juga bisa mengurutkan data. 
3.Create
Create (menambah data) adalah cara bagaimana kita menambah data baru ke suatu database. 
4.Read
Read (menampilkan data) adalah bagaimana cara kita menampilkan data yang tadi telah kita tambahkan pada proses sebelumnya yaitu Create (menambah data). 
5.Update
Update (mengubah data) adalah proses untuk mengubah data yang sudah ada dalam database. 
6.Delete
Delete (menghapus data) adalah proses untuk menghapus data yang telah diinput sebelumnya. 
7.List
List adalah tipe data yang paling serbaguna yang tersedia dalam bahasa Python, yang dapat ditulis sebagai daftar nilai yang dipisahkan koma (item) antara tanda kurung siku. Hal penting tentang daftar adalah item dalam list tidak boleh sama jenisnya. 
8.If Elif Else
Pada python ada beberapa statement/kondisi diantaranya adalah if, else dan elif. Kondisi if digunakan untuk mengeksekusi kode jika kondisi bernilai benar True. Jika kondisi bernilai salah False maka statement/kondisi if tidak akan di-eksekusi.
Kondisi If Else adalah kondisi dimana jika pernyataan benar True maka kode dalam if akan dieksekusi, tetapi jika bernilai salah False maka akan mengeksekusi kode di dalam else. 
If Elif merupakan lanjutan/percabangan logika dari “kondisi if”. Dengan elif kita bisa membuat kode program yang akan menyeleksi beberapa kemungkinan yang bisa terjadi. Hampir sama dengan kondisi “else”, bedanya kondisi “elif” bisa banyak dan tidak hanya satu. 
9.For
Pengulangan for pada Python memiliki kemampuan untuk mengulangi item dari urutan apapun, seperti list atau string. 
10.PwInput
PWInput berfungsi agar saat user atau admin input password, maka tampilan passwordnya berupa **** dengan tujuan untuk menyembunyikan password tersebut.
11.Dictionary
Dictionary adalah tipe data pada python yang berfungsi untuk menyimpan kumpulan data/nilai dengan pendekatan “key-value”. Dictionary Python berbeda dengan List ataupun Tuple. Karena setiap urutanya berisi key dan value. Setiap key dipisahkan dari value-nya oleh titik dua (:), item dipisahkan oleh koma, dan semuanya tertutup dalam kurung kurawal. Dictionary kosong tanpa barang ditulis hanya dengan dua kurung kurawal, seperti ini: {}.
12. Function
Function adalah kode program yang dirancang untuk menyelesaikan sebuah tugas tertentu, dan merupakan bagian dari program utama. Function dibuat agar kita tidak menulis baris program yang sama berulang kali. Ketika kita ingin menggunakan baris program yang sama, maka kita hanya perlu memanggil function.

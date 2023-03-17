# Dokumentasi
## Pendahuluan

Linked List adalah salah satu struktur data yang sangat berguna dalam pemrograman, termasuk dalam bidang travel dan transportasi. Traveloka, sebagai salah satu perusahaan travel terkemuka di Indonesia, menggunakan linked list untuk menyimpan informasi penerbangan seperti maskapai, asal, tujuan, waktu keberangkatan dan waktu kedatangan, tanggal keberangkatan, harga, dan lain sebagainya.

Pada aplikasi Traveloka, linked list digunakan untuk menyimpan data penerbangan yang tersedia, dimana setiap node dalam linked list merepresentasikan satu penerbangan. Dengan menggunakan linked list, data penerbangan dapat diatur dan diakses dengan mudah, dan juga dapat dengan cepat ditambah atau dihapus jika terdapat perubahan jadwal atau harga tiket.

Pada linked list Traveloka, setiap node berisi informasi tentang satu penerbangan, seperti maskapai, asal, tujuan, waktu keberangkatan dan waktu kedatangan, tanggal keberangkatan, harga, dan juga pointer yang menunjuk ke node selanjutnya. Dengan menggunakan pointer ini, aplikasi Traveloka dapat dengan mudah mengakses setiap node pada linked list untuk menampilkan informasi penerbangan kepada pengguna.

## Penjelasan Source Code
[Source Code](https://github.com/fauzangifari/Algoritma-Struktur-Data/blob/master/Post%20Test%203/traveloka.py)

![image](https://user-images.githubusercontent.com/77602702/225687233-ec0c16d1-208c-47e9-9ecf-e607775081d0.png)
- **import os** digunakan untuk mengimpor modul os, yang menyediakan berbagai fungsi untuk berinteraksi dengan sistem operasi. Modul ini digunakan pada bagian kode selanjutnya untuk membersihkan layar terminal.
- **import time** digunakan untuk mengimpor modul time, yang menyediakan fungsi-fungsi terkait waktu. Modul ini digunakan pada bagian kode selanjutnya untuk memberikan jeda waktu antara aksi-aksi yang dilakukan.
- **from prettytable import PrettyTable** digunakan untuk mengimpor kelas PrettyTable dari modul prettytable. Kelas ini memungkinkan kita untuk membuat tabel dengan mudah dan cantik. Modul ini digunakan pada bagian kode selanjutnya untuk menampilkan hasil pencarian penerbangan dalam bentuk tabel.

============================================================================================
![image](https://user-images.githubusercontent.com/77602702/225689239-1b67cdac-8acc-411d-badd-63f1f0bd7f2c.png)
Dari kode diatas mendefinisikan sebuah class Flight dan terdapat konstruktor dengan atribut seperti airline, orgin, destination, departureTime, arrivalTime, dateTime, price, dan nextFlight.
- airline : merepresentasikan maskapai penerbangan yang akan diambil
- origin : merepresentasikan kota keberangkatan dari pernerbangan
- destination : merepresentasikan kota tujuan dari penerbangan
- departureTime: merepresentasikan waktu keberangkatan dari penerbangan.
- arrivalTime: merepresentasikan waktu tiba dari penerbangan.
- dateTime: merepresentasikan tanggal dan waktu penerbangan.
- price: merepresentasikan harga tiket dari penerbangan.
- nextFlight: merepresentasikan objek Flight selanjutnya pada linked list. Nilai awalnya adalah None jika objek Flight tersebut adalah objek terakhir dalam linked list.

Lalu didalam class Flight ada terdapat sebuah method str. Method tersebut akan mengembalikan string yang merepresentasikan objek Flight dalam bentuk yang mudah dibaca. String yang dihasilkan akan terdiri dari atribut-atribut objek Flight seperti airline, origin, destination, departureTime, arrivalTime, dateTime, dan price. String tersebut akan digabungkan dengan menggunakan format string pada Python (f-string) dengan menggunakan kurung kurawal dan menyisipkan nilai atribut dengan memanggil nama atribut melalui self.

============================================================================================
![image](https://user-images.githubusercontent.com/77602702/225840434-b9b198bd-7ac0-47ec-8ac0-0568a21c461b.png)

Dari kode diatas mendefinisikan sebuah class LinkedList dan didalam class tersebut terdapat konstruktur yand didalamnya terdapat 4 atribut yaitu head, tail, prev, dan history.
- **head** adalah atribut yang menunjukkan simpul pertama atau elemen pertama dari linked list.
- **tail** adalah atribut yang menunjukkan simpul terakhir atau elemen terakhir dari linked list.
- **prev** adalah atribut yang menyimpan nilai simpul sebelumnya. Atribut ini digunakan untuk melakukan operasi penambahan dan penghapusan elemen pada linked list.
- **history** adalah atribut yang menyimpan riwayat penerbangan. Atribut ini digunakan untuk menampilkan riwayat penerbangan yang sudah ditambahkan dan dihapus.

============================================================================================
![image](https://user-images.githubusercontent.com/77602702/225842465-0db60a73-80ae-4381-a40d-4cb3d5443224.png)
Didalam class LinkedList terdapat sebuah method bernama addFlight. Method ini digunakan untuk menambahkan data penerbangan ke dalam linked list.
- Pertama, method ini memeriksa apakah linked list masih kosong (head-nya bernilai None). Jika iya, maka node baru dibuat dan dijadikan sebagai head dan tail dari linked list. Jika tidak, node baru akan ditambahkan pada akhir dari linked list (setelah node terakhir saat ini) dan menjadi tail dari linked list.
- Setelah itu, method ini juga menambahkan riwayat operasi Add ke dalam attribute history dari linked list. Jika node baru ditambahkan ke akhir linked list, informasi node baru juga ditambahkan ke dalam history.

============================================================================================
![image](https://user-images.githubusercontent.com/77602702/225843648-c7e7a772-835e-4499-b75d-c22868808d7d.png)
Lalu terdapat lagi sebuah method bernama printFlight. Method ini digunakan untuk mencetak daftar tiket pesawat yang tersedia pada linked list.
- Pertama, variabel temp diinisialisasi dengan self.head, yaitu elemen pertama dari linked list. Kemudian, dibuat objek PrettyTable yang memiliki 8 kolom, yaitu nomor tiket, maskapai, asal, tujuan, waktu keberangkatan, waktu kedatangan, tanggal keberangkatan, dan harga.
- Selanjutnya, dengan menggunakan perulangan while, setiap elemen dari linked list akan ditambahkan ke PrettyTable dengan nomor tiket, informasi penerbangan, waktu keberangkatan, waktu kedatangan, tanggal keberangkatan, dan harga. Variabel number digunakan untuk menentukan nomor urut tiket. Akhirnya, objek PrettyTable dicetak dengan menggunakan fungsi print.

============================================================================================
![image](https://user-images.githubusercontent.com/77602702/225844266-7bd0031b-0478-4651-a29c-e3b905a022d0.png)
Lalu terdapat lagi sebauh method bernama deleteFlight. Method ini digunakan untuk menghapus elemen dari linked list berdasarkan nomor yang diinputkan.
- Argumen number digunakan untuk menunjukkan nomor urutan elemen yang akan dihapus. Kemudian, metode deleteFlight akan mencari elemen dengan nomor urutan tersebut. Apabila elemen yang dicari tidak ditemukan, maka metode akan langsung berhenti.
- Jika elemen yang ditemukan merupakan elemen pertama, maka pointer head akan diubah menjadi elemen selanjutnya. Sedangkan jika elemen yang ditemukan merupakan elemen lainnya, maka pointer nextFlight dari elemen sebelumnya akan dihubungkan dengan elemen setelahnya.
- Setelah elemen berhasil dihapus, maka informasi mengenai elemen tersebut akan ditambahkan ke dalam atribut history.

============================================================================================
![image](https://user-images.githubusercontent.com/77602702/225904762-d3f82717-b54b-46ad-8d81-ae739bb215d8.png)
Lalu terdapat lagi sebuah method bernama paginate. Method ini akan menampilkan data penerbangan sesuai dengan halaman yang ditentukan dan jumlah data yang ingin ditampilkan pada setiap halaman.
- Parameter page dan size digunakan untuk menentukan halaman dan jumlah data yang ingin ditampilkan pada setiap halaman.
- temp adalah sebuah variabel yang digunakan untuk menunjuk pada node pertama dari linked list yang berisi data penerbangan.
- Variabel t digunakan untuk membuat objek dari kelas PrettyTable dan mendefinisikan header atau kolom-kolom tabel.
- Variabel number digunakan untuk menentukan nomor urut dari setiap data penerbangan yang ditampilkan pada tabel.
- count adalah sebuah variabel penghitung yang digunakan untuk menghitung jumlah data penerbangan yang telah dilooping.

Pada saat dilakukan looping, data penerbangan yang sesuai dengan halaman dan jumlah data yang ditentukan akan ditambahkan pada tabel menggunakan method add_row(). Setiap kali data penerbangan berhasil ditambahkan ke dalam tabel, variabel number akan ditambahkan 1 untuk menentukan nomor urutan dari data penerbangan pada halaman selanjutnya. Setelah semua data penerbangan pada halaman yang ditentukan telah ditampilkan, tabel akan dicetak ke layar menggunakan method print().

============================================================================================
![image](https://user-images.githubusercontent.com/77602702/225908243-c4b2bc61-d70a-4359-95b7-cbc5597ac721.png)
Lalu terdapat lagi sebuah method bernama historyAddDelete. Method ini untuk menampilkan riwayat penambahan atau penghapusan data penerbangan yang dilakukan sebelumnya. Fungsi ini menggunakan modul PrettyTable untuk menampilkan data secara rapi dan terstruktur.
- Fungsi ini membuat objek PrettyTable dengan kolom yang sesuai dengan atribut penerbangan seperti nomor, pesawat, asal, tujuan, waktu keberangkatan, waktu kedatangan, tanggal keberangkatan, dan harga. Selanjutnya, variabel number diinisialisasi dengan nilai 0.
- Fungsi ini melakukan iterasi pada setiap item pada atribut history dengan menggunakan perulangan for. Di dalam perulangan, fungsi menentukan judul tabel menjadi "Riwayat Add/Delete" dan menambahkan baris pada tabel sesuai dengan tindakan yang dilakukan pada setiap item.
- Jika tindakan pada item adalah "Add", maka fungsi menambahkan baris pada tabel dengan menggunakan data pada item sebagai parameter input. Jika tindakan pada item adalah "Delete", fungsi menambahkan baris pada tabel dengan menggunakan data pada item sebagai parameter input.
- Setiap kali sebuah baris ditambahkan pada tabel, nilai number akan ditambahkan dengan 1. Setelah semua item pada atribut history selesai diiterasi, tabel akan dicetak pada layar menggunakan perintah print(t).

============================================================================================
![image](https://user-images.githubusercontent.com/77602702/225934545-e9218b2a-42c3-449f-bf2e-c2ac951d6f2f.png)

**flight = LinkedList()** program menginisialisasi linked list baru dengan memanggil konstruktor LinkedList() dan menyimpannya ke dalam variabel flight.

![image](https://user-images.githubusercontent.com/77602702/225936308-93ecebd1-6ed8-45f3-b9c6-474570ff7839.png)

Program menampilkan menu pilihan untuk pengguna yang terdiri dari opsi untuk menambah tiket pesawat, menghapus tiket pesawat, menampilkan halaman tiket pesawat, melihat riwayat penambahan/hapus tiket, dan keluar dari program. Setelah pengguna memilih salah satu opsi, program akan memproses pilihan tersebut dan menjalankan kode yang sesuai.

![image](https://user-images.githubusercontent.com/77602702/225937720-3dd1f75a-c600-46a5-9c47-bfc55b7f37b9.png)

Jika pengguna memilih opsi 1, program akan meminta pengguna untuk memasukkan detail tiket pesawat (nama maskapai, asal, tujuan, waktu keberangkatan, waktu kedatangan, tanggal keberangkatan, dan harga) dan menambahkan tiket tersebut ke dalam linked list menggunakan metode addFlight().

![image](https://user-images.githubusercontent.com/77602702/225938064-e932c3df-fe54-4051-a005-06a6aab92d80.png)

Jika pengguna memilih opsi 2, program akan menampilkan daftar tiket pesawat menggunakan metode printFlight() dan meminta pengguna untuk memilih nomor tiket yang ingin dihapus. Setelah pengguna memilih nomor tiket, program akan menghapus tiket tersebut dari linked list menggunakan metode deleteFlight().

![image](https://user-images.githubusercontent.com/77602702/225938393-9d3b99a8-b83a-4cd6-ad89-9509e1895d06.png)

Jika pengguna memilih opsi 3, program akan menampilkan halaman pertama dari daftar tiket pesawat menggunakan metode paginate() dan meminta pengguna untuk memilih apakah ingin melanjutkan ke halaman berikutnya atau tidak. Jika pengguna memilih untuk melanjutkan, program akan menampilkan halaman berikutnya dengan menggunakan metode paginate() kembali dan meminta pengguna untuk memilih apakah ingin melanjutkan atau tidak. Proses ini akan terus berlanjut sampai pengguna memilih untuk tidak melanjutkan lagi.

![image](https://user-images.githubusercontent.com/77602702/225938509-d4c0105e-4d87-4c81-9a70-123a21b405da.png)

Jika pengguna memilih opsi 4, program akan menampilkan riwayat penambahan/hapus tiket pesawat menggunakan metode historyAddDelete() dan meminta pengguna untuk menekan tombol ENTER untuk kembali ke menu utama.

![image](https://user-images.githubusercontent.com/77602702/225938622-99c8b046-110e-4b8d-a2e2-01c163476dd5.png)

Jika pengguna memilih opsi 5, program akan keluar dari program.

![image](https://user-images.githubusercontent.com/77602702/225938718-f60b1e5b-e612-4072-9f8d-d78c7c15057a.png)

Jika pengguna memilih opsi selain 1-5, program akan menampilkan pesan "Pilihan tidak tersedia".

## Output Program

![image](https://user-images.githubusercontent.com/77602702/225941195-679dc148-a71a-4ab4-867c-79a728761b91.png)

Pada menu utama terdapat 5 opsi.
- Opsi 1, program akan meminta pengguna untuk memasukkan detail tiket pesawat (nama maskapai, asal, tujuan, waktu keberangkatan, waktu kedatangan, tanggal keberangkatan, dan harga.

![image](https://user-images.githubusercontent.com/77602702/225942187-3afa1e83-28cd-4b4c-b978-cfd7cecba036.png)

Jika berhasil maka tampilan akan seperti diatas.

- Opsi 2, Program akan menampilkan daftar tiket pesawat dan meminta pengguna untuk memilih nomor tiket yang ingin dihapus.

![image](https://user-images.githubusercontent.com/77602702/225943182-c16bdd2e-bcf4-4f12-8ee8-f513dc1e1e38.png)

Jika berhasil maka tampilan akan seperti diatas.

- Opsi 3, Program akan menampilkan halaman pertama dari daftar tiket pesawat dan meminta pengguna untuk memilih apakah ingin melanjutkan ke halaman berikutnya atau tidak. 

![image](https://user-images.githubusercontent.com/77602702/225943644-e7da33c8-6041-4bbb-b1fc-0bdb38bc60df.png)

Jika pengguna memilih untuk melanjutkan, program akan menampilkan halaman berikutnya kembali dan meminta pengguna untuk memilih apakah ingin melanjutkan atau tidak.

![image](https://user-images.githubusercontent.com/77602702/225943796-3a4109e4-45db-476b-b8a2-a70ff23aacc6.png)

Dan seterusnya sampai data tiket penerbangan menampilkan semuanya. Jika sudah menampilkan semuanya maka halaman akan menjadi kosong.

- Opsi 4, Program akan menampilkan riwayat penambahan/hapus tiket pesawat.

![image](https://user-images.githubusercontent.com/77602702/225944729-e9d1627f-a82f-435d-bb5b-ae649aeef673.png)

Berbeda dengan menampilkan opsi 3, di opsi 4 terdapat tambahan attribut bernama action, dimana action berfungsi untuk penanda data ditambah atau dihapus. Jika ingin user ingin kembali, dapat memencet ENTER maka otomatis akan kembali menu.

- Opsi 5, untuk mengakhiri program


## Sekian dokumentasi yang bisa saya bagikan.

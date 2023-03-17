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

![image](https://user-images.githubusercontent.com/77602702/225840434-b9b198bd-7ac0-47ec-8ac0-0568a21c461b.png)

Dari kode diatas mendefinisikan sebuah class LinkedList dan didalam class tersebut terdapat konstruktur yand didalamnya terdapat 4 atribut yaitu head, tail, prev, dan history.
- **head** adalah atribut yang menunjukkan simpul pertama atau elemen pertama dari linked list.
- **tail** adalah atribut yang menunjukkan simpul terakhir atau elemen terakhir dari linked list.
- **prev** adalah atribut yang menyimpan nilai simpul sebelumnya. Atribut ini digunakan untuk melakukan operasi penambahan dan penghapusan elemen pada linked list.
- **history** adalah atribut yang menyimpan riwayat penerbangan. Atribut ini digunakan untuk menampilkan riwayat penerbangan yang sudah ditambahkan dan dihapus.

![image](https://user-images.githubusercontent.com/77602702/225842465-0db60a73-80ae-4381-a40d-4cb3d5443224.png)
Didalam class LinkedList terdapat sebuah method bernama addFlight. Method ini digunakan untuk menambahkan data penerbangan ke dalam linked list.
- Pertama, method ini memeriksa apakah linked list masih kosong (head-nya bernilai None). Jika iya, maka node baru dibuat dan dijadikan sebagai head dan tail dari linked list. Jika tidak, node baru akan ditambahkan pada akhir dari linked list (setelah node terakhir saat ini) dan menjadi tail dari linked list.
- Setelah itu, method ini juga menambahkan riwayat operasi Add ke dalam attribute history dari linked list. Jika node baru ditambahkan ke akhir linked list, informasi node baru juga ditambahkan ke dalam history.

![image](https://user-images.githubusercontent.com/77602702/225843648-c7e7a772-835e-4499-b75d-c22868808d7d.png)
Lalu terdapat lagi sebuah method bernama printFlight. Method ini digunakan untuk mencetak daftar tiket pesawat yang tersedia pada linked list.
- Pertama, variabel temp diinisialisasi dengan self.head, yaitu elemen pertama dari linked list. Kemudian, dibuat objek PrettyTable yang memiliki 8 kolom, yaitu nomor tiket, maskapai, asal, tujuan, waktu keberangkatan, waktu kedatangan, tanggal keberangkatan, dan harga.
- Selanjutnya, dengan menggunakan perulangan while, setiap elemen dari linked list akan ditambahkan ke PrettyTable dengan nomor tiket, informasi penerbangan, waktu keberangkatan, waktu kedatangan, tanggal keberangkatan, dan harga. Variabel number digunakan untuk menentukan nomor urut tiket. Akhirnya, objek PrettyTable dicetak dengan menggunakan fungsi print.

![image](https://user-images.githubusercontent.com/77602702/225844266-7bd0031b-0478-4651-a29c-e3b905a022d0.png)
Lalu terdapat lagi sebauh method bernama deleteFlight. Method ini digunakan untuk menghapus elemen dari linked list berdasarkan nomor yang diinputkan.
- Argumen number digunakan untuk menunjukkan nomor urutan elemen yang akan dihapus. Kemudian, metode deleteFlight akan mencari elemen dengan nomor urutan tersebut. Apabila elemen yang dicari tidak ditemukan, maka metode akan langsung berhenti.
- Jika elemen yang ditemukan merupakan elemen pertama, maka pointer head akan diubah menjadi elemen selanjutnya. Sedangkan jika elemen yang ditemukan merupakan elemen lainnya, maka pointer nextFlight dari elemen sebelumnya akan dihubungkan dengan elemen setelahnya.
- Setelah elemen berhasil dihapus, maka informasi mengenai elemen tersebut akan ditambahkan ke dalam atribut history.

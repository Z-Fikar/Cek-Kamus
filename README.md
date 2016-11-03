# Cek-Kamus
Cek-Kamus adalah sebuah sebuah program sederhana untuk mencari apakah sebuah kata dalam file terjemahan berekstensi PO **tidak** termasuk ke dalam Kamus Besar Bahasa Indonesia.

###Detail
Cek-Kamus akan membaca msgstr pada file po, kemudian mencari asal kata tersebut, setelah ditemukan kata tersebut akan dicek apakah terdapat dalam KBBI. Jika tidak ada dalam KBBI, maka program akan mengeluarkan sebuah *output* berupa msgstr beserta kata tersebut. Mohon diperhatikan program ini memakai skrip sederhana sehingga masih membutuhkan banyak perubahan untuk ke depannya.

###Syarat Kondisi
- Python 3.x
- paket [polib](http://polib.readthedocs.io/)
- paket [Pysastrawi](https://github.com/har07/PySastrawi)

###Penggunaan
`python cekkamus.py alamat/ke/file.po`

###Penghargaan
Penghargaan dan pujian diberikan kedapa orang-orang dibawah ini karena tanpa mereka, program ini tidak akan pernah ~~selesai~~ tercipta.
- [John Vandenberg](https://github.com/jayvdb) dan tim BesutKode lainnya.
- [Mamat Rahmat](https://github.com/mamat-rahmat), Program ini berdasarkan program yang dia buat. cek [disini](https://github.com/mamat-rahmat/checker_id)

Cek juga:
- https://github.com/bgli/kbbi-qt <- `Kamus.txt` berdasarkan basis data mereka
- https://github.com/sastrawi/sastrawi <- Sastrawi versi PHP

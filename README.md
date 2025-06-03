# TASK-REPOSITORY
#Apa itu Zeller's Congruence?
Zeller's Congruence adalah algoritma matematika yang digunakan untuk menentukan hari dalam seminggu dari suatu tanggal tertentu. Algoritma ini bekerja dengan rumus sebagai berikut:

ini
Copy
Edit
h = (q + (13(m + 1) // 5) + K + (K // 4) + (J // 4) + (5J)) % 7
Keterangan:

h = hari dalam minggu (0 = Sabtu, 1 = Minggu, ..., 6 = Jumat)

q = tanggal (day of the month)

m = bulan (March = 3, ..., January = 13, February = 14) → Januari dan Februari dianggap bulan ke-13 dan ke-14 dari tahun sebelumnya

K = tahun (2 digit terakhir)

J = abad (2 digit pertama dari tahun)

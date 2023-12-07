# Counter Picker Helper for DOTA 2

## Overview

Pembantu Pemilih Kontra DOTA 2 adalah program yang dirancang untuk membantu pengguna dalam memilih Hero yang paling cocok untuk dimainkan dalam Game DOTA 2. Program ini menggunakan prinsip teori himpunan untuk menganalisis dan merekomendasikan Hero berdasarkan pemilihan Hero lawan.

## Features

- Antarmuka yang ramah pengguna: Program ini meminta pengguna untuk memasukkan nama-nama Hero lawan.
- Pengambilan data: Program ini mengambil data Hero dari situs web [dota2.fandom.com](https://dota2.fandom.com).
- Operasi himpunan: Program ini melakukan operasi himpunan untuk menentukan Hero terbaik untuk melawan Hero lawan.
- Tampilan rekomendasi: Program ini menampilkan Hero yang direkomendasikan untuk pengguna mainkan.

## Requirements

1. Python 3.6 atau yang lebih tinggi
2. [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) 4.9.3 atau yang lebih tinggi
3. [Requests](https://requests.readthedocs.io/en/master/) 2.25.1 atau yang lebih tinggi
4. [Itertools](https://docs.python.org/3/library/itertools.html) 8.6.0 atau yang lebih tinggi

## Installation

1. Clone repositori: `git clone https://github.com/TazakiN/DOTA2_Counter_Picker_Helper.git`
2. Buka direktori proyek: `cd DOTA2_Counter_Picker_Helper`
3. Pastikan Anda telah menginstal semua dependensi yang terdapat pada [Requirements](#Requirements).

## Usage

1. Jalankan program: `python main.py`
2. Ikuti petunjuk untuk memasukkan nama-nama Hero lawan.
3. Program akan menganalisis data dan menampilkan Hero yang direkomendasikan untuk pengguna mainkan.
4. Program akan meminta pengguna untuk memasukkan nama-nama Hero lawan lagi. Jika pengguna memasukkan "exit", program akan berhenti. Jika pengguna memasukkan "reset", program akan mereset pilihan Hero lawan.

## Room for Improvement

1. Menambahkan fitur input Hero yang dimainkan oleh pengguna menggunakan singkatan nama Hero yang lazim digunakan.
2. Meningkatkan akurasi rekomendasi Hero yang diberikan dengan memanfaatkan data lainnya seperti _win-rate_ dan _pick-rate_.
3. Menambahkan fitur untuk memilih Hero berdasarkan role yang diinginkan pengguna.
4. Meningkatkan kecepatan program dengan teknik-teknik seperti _multithreading_.

## Contributing

Jika Anda memiliki ide, saran, atau laporan bug, silakan [buat issues baru](https://github.com/TazakiN/DOTA2_Counter_Picker_Helper/issues) atau [buat pull request](https://github.com/TazakiN/DOTA2_Counter_Picker_Helper/pulls).

## License

Proyek ini dilisensikan di bawah [Lisensi MIT](LICENSE).

## Acknowledgements

- [dota2.fandom.com](https://dota2.fandom.com) atas penyediaan data Hero DOTA 2 dan Counter-nya.

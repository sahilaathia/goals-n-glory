Cara mengimplementasikan checklist tugas 2:
- Membuat sebuah proyek Django baru.
        Dengan membuat direktori goals-n-glory, membuat dan mengaktifkan virtual environment melalui terminal direktori, menyiapkan dependencies ( dengan membuat dan mengisi file requirements.txt dengan dependencies), install dependencies melalui terminal, membuat project django dengan nama goals_n_glory melalui terminal, menambahkan file .env dan .env.prod dan mengisinya dengan konfigurasi, modifikasi file settings.py (menambahkan kode menggunakan env variables, menambahkan localhost ke allowed_hosts, konfigurasi production dan database), migrate database, run server django, push ke github dan pws.
- Membuat aplikasi dengan nama main pada proyek tersebut.
        Dengan menjalankan perintah di terminal direktori, menambahkan aplikasi "main" ke installed_apps di settings.py
- Melakukan routing pada proyek agar dapat menjalankan aplikasi main.
- Membuat model pada aplikasi main dengan nama Product dan memiliki atribut wajib sebagai berikut.
name sebagai nama item dengan tipe CharField.
price sebagai harga item dengan tipe IntegerField.
description sebagai deskripsi item dengan tipe TextField.
thumbnail sebagai gambar item dengan tipe URLField.
category sebagai kategori item dengan tipe CharField.
is_featured sebagai status unggulan item dengan tipe BooleanField.
- Membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas kamu.
- Membuat sebuah routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py.
- Melakukan deployment ke PWS terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.


- Membuat sebuah README.md yang berisi tautan menuju aplikasi PWS yang sudah di-deploy, serta jawaban dari beberapa pertanyaan berikut.
Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
Jelaskan peran settings.py dalam proyek Django!
Bagaimana cara kerja migrasi database di Django?
Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
Apakah ada feedback untuk asisten dosen tutorial 1 yang telah kamu kerjakan sebelumnya?
## Tugas Individu 2

**PWS**: https://sahila-khairatul-goalsnglory.pbp.cs.ui.ac.id/

### 1. Cara mengimplementasikan checklist tugas 2:
- Membuat direktori utama goals-n-glory
- Membuat dan mengaktifkan virtual environment
- Menyiapkan dependencies di file `requirements.txt` dan install melalui terminal
- Membuat project django dengan nama goals_n_glory melalui terminal
- Membuat file `.env` dan `.env.prod` dan mengisinya dengan konfigurasi
- Modifikasi file `settings.py`: menambahkan `load_dotenv()`, menambahkan localhost ke `ALLOWED_HOSTS`, konfigurasi production dan database
- Migrate dan run server django
- Membuat aplikasi `main` dengan `python manage.py startapp main`
- Menambahkan 'main' ke `INSTALLED_APPS` di `settings.py`
- Membuat model `Product` di `main/models.py`, dengan atribut: name, price, description, thumbnail, category, is_featured, brand, size, color, stock
- Migrate model dengan `python manage.py makemigrations` dan `python manage.py migrate` melalui terminal
- Membuat fungsi `show_main` di `main/views.py` dan mengisinya dengan dictionary berisi nama, npm, kelas, dan nama aplikasi untuk dikirimkan ke `main.html`
- Membuat folder `templates` di `main`
- Menambahkan file `main.html` dan mengisinya dengan yang ingin ditampilkan di web (nama, npm, kelas, dan nama aplikasi yang direturn oleh fungsi `show_main` di `main/views.py`)
- Routing dengan membuat `urls.py` di `main` dan mengisinya dengan `path('', show_main, name="show_main")`
- Menambahkan `path('', include('main.urls'))` di `goals_n_glory/urls.py`
- Push ke github
- Create new project di PWS, isi environs dengan kode dari `.env.prod`, tambahkan url deployment PWS pada `ALLOWED_HOSTS` di `settings.py`
- Push ke PWS

### 2. Bagan alur request-response dan kaitan antara urls.py, views.py, models.py, dan berkas html


### 3. Peran settings.py dalam proyek Django
`settings.py` berperan sebagai pusat kontrol proyek Django yang memuat seluruh konfigurasi proyek, seperti menyimpan daftar aplikasi aktif, pengaturan database, middleware, template, static files, bahasa dan time zone, kunci keamanan, serta daftar allowed hosts.

### 4. Cara kerja migrasi database di Django

### 5. Mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?

### 6. Feedback untuk asisten dosen terkait tutorial 1

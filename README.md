## LINK ADAPTABLE
[link nanti di sini]

<hr>

## DAFTAR ISI
* [Implementasi *Checklist*](#implementasi-checklist)
* [Bagan *Request-Response*](#bagan-request-response-pada-django)
* [Virtual Environment](#deskripsi-virtual-enviroment)
* [MVC, MVT, MVVM dan Perbedaannya](#mvc-mvt-mvvm-dan-perbedaannya)
* [BONUS](#bonus)

<hr>

## Implementasi *Checklist*
#### Membuat Proyek Django Baru
1. Awalnya, saya membuat direktori baru dengan nama `scoobyria`.
<br>

2. Kemudian, saya membuka `cmd` untuk membuat Virtual Environment dengan perintah berikut. 
    ``` bash
    python -m venv env
    ```
    Jika aktif, akan ditandai dengan `(env)`.
<br>

3. Setelah itu, saya mengaktifkan Virtual Environment dengan perintah berikut:
    ``` bash
    env\Scripts\activate.bat
    ```
<br>

4. Pada direktori `scoobyria`, saya membuat file `requirements.txt` seperti berikut.
    ``` text
    django
    gunicorn
    whitenoise
    psycopg2-binary
    requests
    urllib3
    ```
<br>

5. Kemudian, saya mengaktifkan `(env)` di `cmd`. Lalu, saya membuat proyek Django dengan perintah berikut.
    ``` bash
    django-admin startproject scoobyria .
    ```
<br>

6. Lalu, saya menambahkan `*` pada `ALLOWED_HOST` di `settings.py` agar dapat *deploy*.
<br>

#### Membuat Aplikasi dengan Nama `main`
1. Mula-mulanya, saya membuat aplikasi `main` terlebih dahulu.
<br>

2. Pada variabel `INSTALLED_APPS` di `settings.py`, saya tambahkan `main` seperti contoh berikut.
    ``` python
    INSTALLED_APPS = [
        ...,
        'main',
        ...
    ]
    ```
<br>

3. Lalu, saya membuat `main.html` dalam direktori `templates`.
<br>

#### Melakukan *Routing* pada Proyek
1. Awalnya, saya membuat `urls.py` dalam `main`. Saya mengisinya dengan kode berikut.
    ``` python
    from django.urls import path
    from main.views import show_main

    app_name = 'main'

    urlpatterns = [
        path('', show_main, name='show_main'),
    ]
    ```
<br>

2. Kemudian, saya impor fungsi `include` dari `django.urls` dan menambahkan rute URL seperti berikut.
    ``` python
    from django.contrib import admin
    from django.urls import path
    from django.urls import path, include


    urlpatterns = [
        path('admin/', admin.site.urls),
        path('', include('main.urls')),
        path('main/', include('main.urls')),
    ]
    ```
<br>

#### Membuat Model pada Aplikasi `main`
1. Saya memodifikasi `models.py` pada `main` seperti berikut.
    ``` python
    from django.db import models

    class Product(models.Model):
        name = models.CharField(max_length=255)
        amount = models.IntegerField()
        description = models.TextField()
        status = models.CharField(max_length=255)
        price = models.IntegerField()
    ```
    `name`, `amount`, `description`, `status`, dan `price` adalah atribut yang saya pilih atau buat untuk `models.py`
<br>

2. Lalu, saya melakukan migrasi model di `cmd` dengan perintah berikut.
    ``` bash
    python manage.py makemigrations
    ```
    ``` bash
    python manage.py migrate
    ```
<br>

#### Membuat Fungsi pada `views.py`
1. Pertama, saya memodifikasi `views.py` dalam `main` seperti berikut.
    ``` python
    from django.shortcuts import render

    def show_main(request):
        context = {
            'name': 'Vina Myrnauli Abigail Siallagan',
            'class': 'PBP E',
            'harga': 'Rp200.000,00',
        }

        return render(request, "main.html", context)
    ```

2. Saya juga melakukan render untuk me-*render* tampilan `HTML` dengan data yang ada.
<br>

#### membuat *Routing* pada `urls.py`
Awalnya, saya memodifikasi `urls.py` dalam `main` seperti berikut.
``` python
from django.urls import path
from main.views import show_main

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
]
```
Hal ini dilakukan untuk mengimplementasikan tampilan dalam `main` dan mengubungkannya dengan rute URL proyek..
<br>

#### Melakukan *Deployment* ke Adaptable
1. Apabila semuanya sudah selesai, saya melakukan `add`, `commit`, `push` pada repositori `scoobyria` di GitHub. Kemudian, saya melakukan *deployement* di Adaptable.
<br>

2. Pada Adaptable, klik `create a new app`. kemudian `connect an Existing Repository` karena kita sudah melakukan `add`, `commit`, `push`.
<br>

3. Lalu, klik `Python App Template`. Selanjutnya, klik `PostgreSQL` yang adalah tipe basis data.
<br>

4. Masukkan perintah `python manage.py migrate && gunicorn scoobyria.wsgi` pada `start command`.
<br>

5. Terakhir, masukkan nama aplikasi dan centanglah `HTTP Listener on PORT`. Lalu, klik `deploy`.
<br>

#### Membuat `README.md`
Saya hanya menambahkan dekorasi sedikit yang relevan dengan judul direktori saya. Tak hanya itu, saya juga memasukkan beberapa komponen yang sudah pernah diajarkan oleh tim asdos dan dosen sebelumnya.

## Bagan *Request-Response* pada Django
![BAGAN](/fotovina/baganvina.png)
1. `urls.py` yang diterima dari *client* akan dibandingkan oleh Django dengan pola URL yang sudah didefinisikan. Apabila URL cocok, maka akan disematkan pada *template* `HTML`. 
<br>

2. `views.py` berfungsi untuk memproses atau memanipulasi data yang dibutuhkan dari *database*, `urls.py` akan meminta penerimaan ke `views.py`. Setelah data sudah diproses semua, `views.py`akan mempersiapkan konteks yang disematkan pada *template* `HTML`.
<br>

3. `models.py` memiliki model yang telah didefinisikan. Maka dari itu, `views.py` dapat berinteraksi dengan *database* melalui model tersebut.
<br>

4. `HTML` adalah *template* yang dapat mengambil data yang diberikan oleh `views.py` dan menampilkannya sesuai dengan desain tampilan yang ada.
<br>

## Deskripsi Virtual Enviroment
#### Pentingnya Virtual Environment
Virtual Environment digunakan untuk memisahkan *package* dan *dependencies* dari aplikasi sehingga tidak akan bertabrakan dengan versi lainnya yang ada pada komputer. 

*Dependencies* ini adalah komponen atau modul yang diperlukan oleh *software* untuk berfungsi, termasuk *library*, *framework*, atau *package*. Hal ini dapat memungkinkan pengembang untuk memanfaatkan kode yang sudah ada sehingga dapat mempercept proses pengembangan. Akan tetapi, manajemen ketergantungan harus dilakukan dengan cermat agar sesuai dengan versi yang dibutuhkan. 
<br>

#### Membuat Aplikasi Web Django Tanpa Menggunakan Virtual Environment: Apakah Mungkin?
Kita dapat membuat aplikasi web Django tanpa Virtual Environment. Namun, sebaiknya menggunakan Virtual Environment karena memungkinkan isolasi *dependencies*, memungkinkan penggunaan versi Python yang berbeda, dan mempermudah manajemen *package*.

Jika ingin tidak menggunakan Virtual Environment, dianjurkan untuk tidak menginstal *package* secara global yang dapat mengganggu sistem atau proyek lain.
<br>

## MVC, MVT, MVVM, dan Perbedaannya
#### MVC (Model-View-Control)
Pola ini membagi kode menjadi tiga bagian utama. Saat pengembangan aplikasi, pengembangan perlu mengklasifikasikan kelas atau file ke dalam tiga lapisan.
* ***Model:*** Berfungsi sebagai tempat penyimpanan data aplikasi. Namun, tidak terikat langsung dengan antarmuka pengguna dan bertanggung jawab atas logika domain (aturan bisnis dunia nyata).
* ***View:*** Berisikan komponen yang ditampilkan di layar. Tampilan menyajikan visualisasi data dari model dan menfasilitasi interaksi pengguna.
* ***Controller:*** Berfungsi sebagai penghubung antara *view* dan *model*. Berisikan logika aplikasi utama, merespons interaksi pengguna, dan memperbaharui *model* sesuai kebutuhan.

* ***Perbedaan dengan MVT:*** Pada MVT, bagian *controller* digantikan oleh *template*. *Template* adalah file HTML yang digabungkan dengan Django Template Language (DTL).
* ***Perbedaan dengan MVVM:*** Pada MVVM, bagian *controller* digantikan oleh *ViewModel* yang berfungsi sebagai penghubung antara *model* dan *view*. 
<br>

#### MVT (Model-View-Template)
Pola ini membagi komponen aplikasi menjadi bagian-bagian yang berbeda untuk memudahkan pengelolaan dan organisasi kode. Dengan pendekatan ini, pengembangan dapat bekerja dengan kode yang lebih rapi dan terstruktur.
* ***Model:*** Berfungsi sebagai tempat penyimpanan data dan logika aplikasi.
* ***View:*** Bertugas menampilkan data dari *model* dan mengintegrasikannya dengan *template*.
* ***Template:*** Menyusun tampilan antarmuka pengguna. 

* ***Perbedaan dengan MVC:*** Pada MVC, bagian *template* digantikan oleh *controller*. *Controller* berfungsi sebagai penghubung antara *view* dan *model*.
* ***Perbedaan dengan MVVM:*** Pada MVVM, bagian *template* digantikan oleh *ViewModel* yang berfungsi sebagai penghubung antara *model* dan *view*. 
<br>

#### MVVM (Model-View-ViewModel)
Pola arsitektur pembuatan aplikasi berbasis GUI yang berfokus pada pemisahan antara kode untuk logika bisnis dan tampilan aplikasi.
* ***Model:*** Berfungsi untuk mengatur sumber data secara abstrak dan berkolaborasi dengan *ViewModel* dalam proses pengambilan dan penyimpanan data.
* ***View:*** Bertugas untuk memberi tahu *ViewModel* tentang interaksi pengguna. Lapisan ini mengamati *ViewModel* dan tidak mengandung logika aplikasi.
* ***ViewModel:*** Menyajikan aliran data yang relevan dengan *view*. Selain itu, berfungsi sebagai penghubung antara *model* dan *view*. 
* ***Perbedaan dengan MVT:*** Pada MVT, bagian *ViewModel* digantikan oleh *template*. *template* berfungsi untuk menyusun tampilan antarmuka pengguna.
* ***Perbedaan dengan MVC:*** Pada MVC, bagian *ViewModel* digantikan oleh *controller* yang berfungsi sebagai penghubung antara *view* dan *model*

## BONUS
Berikut adalah bukti bahwa tests.py yang sudah saya tambahkan, berjalan dengan lancar.
![TES](/fotovina/mytest.jpg)
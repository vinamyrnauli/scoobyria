## 🔗🥦**LINK ADAPTABLE**🥦🔗 
https://scoobyria.adaptable.app
<hr>

## 📖**ASSIGNMENTS PBP**📖
<details>
<summary>📋Assignment 2</summary>

## **DAFTAR ISI**
* [Implementasi *Checklist*](#a-implementasi-checklist-part-1)
* [Bagan *Request-Response*](#b-bagan-request-response-pada-django)
* [Virtual Environment](#c-deskripsi-virtual-enviroment)
* [MVC, MVT, MVVM dan Perbedaannya](#d-mvc-mvt-mvvm-dan-perbedaannya)
* [BONUS](#e-bonus)
<hr>

## **A. Implementasi *Checklist* Part 1**
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

#### Membuat *Routing* pada `urls.py`
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

## **B. Bagan *Request-Response* pada Django**
![BAGAN](/photos/mybagan.png)
1. `urls.py` yang diterima dari *client* akan dibandingkan oleh Django dengan pola URL yang sudah didefinisikan. Apabila URL cocok, maka akan disematkan pada *template* `HTML`. 
<br>

2. `views.py` berfungsi untuk memproses atau memanipulasi data yang dibutuhkan dari *database*, `urls.py` akan meminta penerimaan ke `views.py`. Setelah data sudah diproses semua, `views.py`akan mempersiapkan konteks yang disematkan pada *template* `HTML`.
<br>

3. `models.py` memiliki model yang telah didefinisikan. Maka dari itu, `views.py` dapat berinteraksi dengan *database* melalui model tersebut.
<br>

4. `HTML` adalah *template* yang dapat mengambil data yang diberikan oleh `views.py` dan menampilkannya sesuai dengan desain tampilan yang ada.
<br>

## **C. Deskripsi Virtual Enviroment**
#### Pentingnya Virtual Environment
Virtual Environment digunakan untuk memisahkan *package* dan *dependencies* dari aplikasi sehingga tidak akan bertabrakan dengan versi lainnya yang ada pada komputer. 

*Dependencies* ini adalah komponen atau modul yang diperlukan oleh *software* untuk berfungsi, termasuk *library*, *framework*, atau *package*. Hal ini dapat memungkinkan pengembang untuk memanfaatkan kode yang sudah ada sehingga dapat mempercept proses pengembangan. Akan tetapi, manajemen ketergantungan harus dilakukan dengan cermat agar sesuai dengan versi yang dibutuhkan. 
<br>

#### Membuat Aplikasi Web Django Tanpa Menggunakan Virtual Environment: Apakah Mungkin?
Kita dapat membuat aplikasi web Django tanpa Virtual Environment. Namun, sebaiknya menggunakan Virtual Environment karena memungkinkan isolasi *dependencies*, memungkinkan penggunaan versi Python yang berbeda, dan mempermudah manajemen *package*.

Jika ingin tidak menggunakan Virtual Environment, dianjurkan untuk tidak menginstal *package* secara global yang dapat mengganggu sistem atau proyek lain.
<br>

## **D. MVC, MVT, MVVM, dan Perbedaannya**
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
#### D. Implementasi *Checklist*

#### MVVM (Model-View-ViewModel)
Pola arsitektur pembuatan aplikasi berbasis GUI yang berfokus pada pemisahan antara kode untuk logika bisnis dan tampilan aplikasi.
* ***Model:*** Berfungsi untuk mengatur sumber data secara abstrak dan berkolaborasi dengan *ViewModel* dalam proses pengambilan dan penyimpanan data.
* ***View:*** Bertugas untuk memberi tahu *ViewModel* tentang interaksi pengguna. Lapisan ini mengamati *ViewModel* dan tidak mengandung logika aplikasi.
* ***ViewModel:*** Menyajikan aliran data yang relevan dengan *view*. Selain itu, berfungsi sebagai penghubung antara *model* dan *view*. 
* ***Perbedaan dengan MVT:*** Pada MVT, bagian *ViewModel* digantikan oleh *template*. *template* berfungsi untuk menyusun tampilan antarmuka pengguna.
* ***Perbedaan dengan MVC:*** Pada MVC, bagian *ViewModel* digantikan oleh *controller* yang berfungsi sebagai penghubung antara *view* dan *model*

## **E. BONUS**
Berikut adalah bukti bahwa `tests.py` yang sudah saya tambahkan, berjalan dengan lancar.
![TES](/photos/mytest.jpg)
</details>

<details>
<summary>📋Assignment 3</summary>

## **DAFTAR ISI**
* [Perbedaan POST dan GET](#a-perbedaan-form-post-dan-get-dalam-django)
* [Perbedaan XML, JSON, dan HTML](#b-perbedaan-xml-extensible-markup-language-json-javascript-object-notation-dan-html-hypertext-markup-language-dalam-pengiriman-data)
* [JSON sebagai Pertukaran Data](#c-json-sebagai-pertukaran-data-antara-aplikasi-web-modern)
* [Implementasi *Checklist*](#d-implementasi-checklist-part-2)
* [BONUS](#e-bonus-tugas-2)
<hr>

## **A. Perbedaan form `POST` dan `GET` dalam Django**
#### **1. Cara Mengirim Data**
* `GET`: mengirim data form dalam URL.
* `POST`: mengirim data form sebagai bagian dari tubuh permintaan HTTP secara tersembunyi dan tidak muncul di URL.
#### **2. Fungsi**
* `GET`: membaca informasi atau permintaan pencarian.
* `POST`: mengubah status sistem atau mengirim data sensitif.
#### **3. Keamanan secara Umum**
* `GET`: tidak cocok untuk data sensitif karena data akan muncul dalam URL.
* `POST`: lebih aman untuk data sensitif karena data tidak muncul dalam URL.
#### **4. Kemampuan *Bookmarking***
* `GET`: dapat di-*bookmark* karena data ada di dalam URL.
* `POST`: tidak dapat di-*bookmark* karena data tidak ada di dalam URL.
#### **5. Keamanan Aplikasi**
* `GET`: apabila menggunakannya untuk data sensitif, akan menjadi risiko keamanan.
* `POST`: perlindungan seperti `CSRF Django`, dapat meningkatkan keamanan aplikasi. 
<br>

## **B. Perbedaan XML *(eXtensible Markup Language)*, JSON *(JavaScript Object Notation)*, dan HTML *(Hypertext Markup Language)* dalam Pengiriman Data**
#### **1. Fungsi**
* **XML:** menyimpan dan mengirim data. Format datanya fleksibel dan *self-descriptive*.
* **JSON:** menyimpan dan mengirim data dalam bentuk data terstruktur. Format datanya ringkas dan mudah dimengerti.
* **HTML:** membuat struktur dan tampilan konten pada halaman web yang merupakan bahasa *markup* untuk mengatur tampilan web. 
#### **2. Struktur Data**
* **XML:** data disusun seperti bentuk pohon atau *tree structure* dengan elemen-elemen yang memiliki *parent-child relationships*.
* **JSON:** data disimpan dalam pasangan *key-value* dan dapat bersifat *nested*.
* **HTML:** menggambarkan struktur halaman web, di antarnya terdapat *headings*, paragraf, tautan, gambar, dan tabel.
#### **3. Sintaks**
* **XML:** menggunakan *tags (markup)* untuk mengelompokkan data dan tiap elemen harus memiliki *tag* pembuka dan penutup. 
* **JSON:** menggunakan format teks yang mirip dengan struktur objek `JavaScript` dengan objek *key-value*.
* **HTML:** menggunakan *tags* untuk menandai tiap konten elemen dan mengatur tampilan halaman web.
#### **4. Keterbacaan**
* **XML:** lebih sulit dibaca kaarena terdapat banyak *markup*.
* **JSON:** mudah dibaca dan sering digunakan dalam pertukaran data antar-aplikasi, konfigurasi, dan penyimpanan data sederhana.
* **HTML:** mudah dibaca karena untuk merancang tampilan halaman web dan konten.
<br>

## **C. JSON sebagai Pertukaran Data antara Aplikasi Web Modern**
#### **1. Sederhana dan Mudah Dibaca**
JSON menggunakan format yang mudah dibaca, yaitu pasangan *key-value* dan *arrays*.
#### **2. Tidak Perlu *Tag* atau Skema Khusus**
Tidak seperti XML, JSON tidak perlu menggunakan *tag*, atribut, atau skema khusus yang membuatnya lebih ringkas dan fleksibel. 
#### **3. Mendukung Berbagai Tipe Data**
JSON mendukung berbagai tipe data, di antaranya *strings, numbers, booleans, nulls, objects,* dan *arrays* yang dapat berbentuk *nested*.
#### **4. Mudah Dikonversi ke `JavaScript` dan Sebaliknya**
Hal ini sangat berguna bagi para pengembang web karena memungkinkan untuk memproses dan memanipulasi data dengan mudah.
#### **5. Efisien dan Ringkas**
JSON memiliki form data yang ringkas. Hal ini dapat menghemat *bandwith* dan mempercepat pertukaran data antara aplikasi web. 
<br>

## **D. Implementasi *Checklist* Part 2**
#### **Membuat Input `form` untuk Menambahkan Objek Model**
1. Awalnya, saya mengaktifkan *virtual environment* pada proyek scoobyria seperti berikut.
    ``` bash
    env\Scripts\activate.bat
    ```
<br>

2. Kemudian, saya membuka `urls.py` pada folder `scoobyria` dan mengganti *path* `main/` menjadi `''` di `urlpatterns` seperti berikut.
    ``` python
    urlpatterns = [
        path('admin/', admin.site.urls),
        path('', include('main.urls')),
    ]
    ```
<br>

3. Lalu, saya mengimplementasi *Skeleton* dengan membuat *folder* `templates` pada *root folder* dan membuat `base.html` yang berisikan kode seperti berikut.
    ``` html
    {% load static %}
    <!DOCTYPE html>
    <html lang="en">
        <head>
            <meta charset="UTF-8" />
            <meta
                name="viewport"
                content="width=device-width, initial-scale=1.0"
            />
            {% block meta %}
            {% endblock meta %}
        </head>

        <body>
            {% block content %}
            {% endblock content %}
        </body>
    </html>
    ```
<br>

4. Selanjutnya, saya mengubah `settings.py` pada subdirektori `scoobyria` yang mengandung `TEMPLATES` seperti berikut.
    ``` python
    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [BASE_DIR / 'templates'],
            'APP_DIRS': True,
            'OPTIONS': {
                'context_processors': [
                    'django.template.context_processors.debug',
                    'django.template.context_processors.request',
                    'django.contrib.auth.context_processors.auth',
                    'django.contrib.messages.context_processors.messages',
                ],
            },
        },
    ]
    ```
<br>

5. Kemudian, saya mengubah `main.html` pada subdirektori `templates` di direktori `main` sesuai dengan tema aplikasi saya.
<br>

6. Saya membuat `forms.py` pada direktori `main` dengan kode seperti berikut.
    ``` python
    from django.forms import ModelForm
    from main.models import Product

    class ProductForm(ModelForm):
        class Meta:
            model = Product
            fields = ["name", "price", "description"]
    ```
<br>

7. lalu, saya membuka `views.py` pada folder `main` dan menambahkan beberapa kode seperti berikut.
    ``` python
    from django.http import HttpResponse
    from django.core import serializers
    from django.shortcuts import render
    from django.http import HttpResponseRedirect
    from main.forms import ProductForm
    from django.urls import reverse
    from main.models import Product

    def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "create_product.html", context)
    ```
<br>

8. Selanjutnya, saya mengubah beberapa kode pada `views.py` di fungsi `show_main` seperti berikut.
    ``` python
    def show_main(request):
        products = Product.objects.all()

        context = {
            'name': 'Vina Myrnauli Abigail Siallagan',
            'class': 'PBP E', 
            'products': products
        }

        return render(request, "main.html", context)
    ```
<br>

9. Saya *import* fungsi `create_product` pada folder `main` di `urls.py` dan menambahkan *path url* dalam `urlpatterns` pada `urls.py` di `main` seperti berikut.
    ``` python
    from main.views import show_main, create_product
    ```
    ``` pyhton
    path('create-product', create_product, name='create_product'),
    ```
<br>

10. Lalu, saya membuat `crate_product.hmtl` pada direktori `main/templates` dan menambahkan kode dalam `{% block content %}` pada `main.html` sesuai dengan tema aplikasi saya.
<br>

#### **Menambahkan 5 Fungsi `views` dalam Format HTML, XML, JSON, XML *by ID*, dan JSON *by ID***.
1. Kemudian, saya menambahkan beberapa fungsi dan *import* pada `views.py` di direktori `main` seperti berikut.
    ``` python
    from django.http import HttpResponse
    from django.core import serializers
    from django.shortcuts import render
    from django.http import HttpResponseRedirect
    from main.forms import ProductForm
    from django.urls import reverse
    from main.models import Product

    def show_main(request):
        products = Product.objects.all()

        context = {
            'name': 'Vina Myrnauli Abigail Siallagan',
            'class': 'PBP E', 
            'products': products
        }

        return render(request, "main.html", context)

    def create_product(request):
        form = ProductForm(request.POST or None)

        if form.is_valid() and request.method == "POST":
            form.save()
            return HttpResponseRedirect(reverse('main:show_main'))

        context = {'form': form}
        return render(request, "create_product.html", context)

    def show_xml(request):
        data = Product.objects.all()
        return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

    def show_json(request):
        data = Product.objects.all()
        return HttpResponse(serializers.serialize("json", data), content_type="application/json")

    def show_xml_by_id(request, id):
        data = Product.objects.filter(pk=id)
        return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

    def show_json_by_id(request, id):
        data = Product.objects.filter(pk=id)
        return HttpResponse(serializers.serialize("json", data), content_type="application/json")

    ```
<br>

#### **Membuat *Routing* URL untuk Masing-Masing** `views`
1. Selanjutnya, saya memodifikasi berkas `urls.py` pada *folder* `main` dengan menambahkan beberapa *path* dan *import* seperti berikut.
    ``` python
    from django.urls import path
    from main.views import show_main, create_product, show_xml, show_json, show_xml_by_id, show_json_by_id

    app_name = 'main'

    urlpatterns = [
        path('', show_main, name='show_main'),
        path('create-product', create_product, name='create_product'),
        path('xml/', show_xml, name='show_xml'), 
        path('json/', show_json, name='show_json'), 
        path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
        path('json/<int:id>/', show_json_by_id, name='show_json_by_id'), 
    ]
    ```
<br>

#### **Menambahkan Pesan Singkat**
1. Terakhir, saya menambahkan beberapa kode pada `main.html` di `main/templates` seperti berikut.
    ``` html
    <h4>Only {{ products.count }} item(s) available</h4>
    ```
<br>

#### **Mengakses URL dengan Postman**
Berikut adalah *screenshots* dari hasil akses URL pada Postman saya.
![POST1](/photos/post1.jpg)
![POST2](/photos/post2.jpg)
![POST3](/photos/post3.jpg)
![POST4](/photos/post4.jpg)
![POST5](/photos/post5.jpg)
<br>

#### **Melakukan Add, Commit, dan Push**
Apabila semuanya sudah selesai, saya melakukan `add`, `commit`, `push` pada repositori `scoobyria` di GitHub.
<br>

## **E. BONUS TUGAS 2**
Berikut adalah bukti bahwa saya menambahkan pesan singkat untuk nilai bonus.
![COBA](/photos/bonustwo.jpg)
</details>
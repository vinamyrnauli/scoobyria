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
![TES](/photos/bonustwo.jpg)
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

*Source:*
* https://docs.djangoproject.com/en/4.2/topics/forms/
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

*Source:*
* https://pbp-fasilkom-ui.github.io/ganjil-2024/docs/tutorial-2#referensi-tambahan
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

*Source:*
* https://www.linkedin.com/advice/3/what-benefits-drawbacks-using-json-data
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
![COBA](/photos/bonusthree.jpg)
</details>

<details>
<summary>📋Assignment 4</summary>

## **DAFTAR ISI**
* [Kelebihan dan Kekurangan `UserCreationForm`](#a-pengertian-djago-usercreationform-beserta-kelebihan-dan-kekurangan)
* [Perbedaan Autentikasi dan Otorisasi dalam Django](#b-perbedaan-autentikasi-dan-otorisasi-dalam-django)
* [Pengertian dan Penggunaan *Cookies* pada Django](#c-pengertian-cookies-dan-penggunaannya-pada-django)
* [Keamanan dan Risiko Potensial *Cookies*](#d-keamaan-cookies-dan-risiko-potensialnya)
* [Implementasi *Checklist*](#e-implementasi-checklist-part-3)
* [BONUS](#f-bonus-tugas-4)
<hr>

## **A. Pengertian Djago `UserCreationForm` beserta Kelebihan dan Kekurangan**
#### **1. Pengertian**
`UserCreationForm` merupakan impor *form* bawaan yang memudahkan pembuatan *form* pendaftaran untuk *user* dalam aplikasi web. Django `UserCreationForm` memiliki *form* yang mempunyai tiga *field*, yaitu **username**, **password1**, dan **password2** yang biasanya digunakan untuk konfirmasi password1.

#### **2. Kelebihan**
* Dengan menggunakan *form* ini, *user* baru dapat dengan mudah mendaftar di situs web tanpa perlu menuliskan kode dari awal. 

* Memfasilitasi validasi *password* dan izin otomatis. 

#### **3. Kekurangan**
* `UserCreationForm` memiliki tiga *field* secara *default*. Apabila ingin menambah *field* lain, maka kita harus membuat *custom form* atau *override* `UserCreationForm`. Hal ini dapat memakan waktu.

* Tidak memiliki *field* untuk email, maka dari itu diperlukan class `CustomUserCreationForm` agar dapat membuat *field* email.
<br>

*Source:*
* https://www.javatpoint.com/django-usercreationform
* https://overiq.com/django-1-10/django-creating-users-using-usercreationform/
<br>

## **B. Perbedaan Autentikasi dan Otorisasi dalam Django**
#### **1. Perbedaan**
| Autentikasi | Otorisasi |
| --- | --- |
| Identitas pengguna diperiksa agar dapat diakses ke sistem | Memutuskan apa yang dapat dilakukan pengguna yang diautentikasi di situs |
| Proses ini dilakukan sebelum proses otorisasi | proses ini dilakukan setelah proses autentikasi |
| Membutuhkan *detail* login pengguna | Membutuhkan hak istimewa pengguna |
| Pada proses ini, pengguna harus diverifikasi | Pada proses ini, pengguna harus divalidasi |

#### **2. Pentingnya Autentikasi dan Otorisasi**
Keduanya digunakan oleh administrator untuk melindungi sistem dan informasi, termasuk dalam *framework* Django. Autentikasi digunakan untuk memverifikasi identitas pengguna atau layanan dan otorisasi digunakan untuk menentukan hak akses pengguna. 
<br>

*Source:*
* https://www.geeksforgeeks.org/difference-between-authentication-and-authorization/
* https://aws.amazon.com/id/what-is/django/
* https://www.onelogin.com/learn/authentication-vs-authorization
<br>

## **C. Pengertian *cookies* dan Penggunaannya pada Django**
#### **1. Pengertian**
*Cookies* adalah fasilitas penyimpanan di web yang memungkinkan web tersebut dapat mengingat informasi sesi login pengguna. Dalam aplikasi web, *cookies* dapat dibuat, dimodifikasi, dan diakses sehingga dapat memfasilitasi interaksi yang mulus antara pengguna dan situs web. 

#### **2. Penggunaan *cookies* pada Django**
Penggunaan *cookies* pada Django ini berisikan *session id* khusus untuk mengidentifikasi tiap *browser* dan sesi yang terkait pada situs. 

Data sesi sebenarnya ini disimpan dalam *database* situs secara *default*. Maka dari itu, pengguna dapat mengkonfigurasi Django untuk menyimpan data sesi di tempat lain, seperti *cache, files, "secure", cookies*, namun lokasi *default* yang relatif lebih aman. 

Berikut adalah langkah-langkah penggunakan *cookies* untuk mengelola data sesi pengguna:
* Saat pengguna mengakses Django, akan dibuat *session id* yang unik untuk sesi pengguna yang baru.
* Setelah sudah dibuat, Django menyimpan *session id* dalam *cookie* di komputer klien pengguna.
* Pada server, Django mengaitkan *session id* dengan data sesi pengguna yang berisi informasi seperti status login dan lainnya.
* Tiap pengguna melakukan permintaan ke server, Django mengambil *session id* dari *cookie* di permintaan HTTP.
* Django dapat mengubah data sesu sesuai aksi pengguna selama interaksi pengguna-aplikasi.
* Setelah sesi pengguna selesai, Django membersihkan data sesi yang terkait dengan *session id*.
<br>

*Source:*
* https://www.geeksforgeeks.org/es6-cookies/
* https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Sessions


## **D. Keamaan *cookies* dan Risiko Potensialnya**
#### **1. Keamanan**
Sebagian besar *cookies* itu aman karena tidak mengandung informasi yang dapat diidentifikasi dan mereka dirancang untuk membuat pengalaman *online* lebih nyaman, seperti mengisi nama pengguna ketika mengunjungi sebuah situs web, memastikan pengalaman penjelajahan yang lancar, dan mengontentikasi identitas. 

Akan tetapi, ada juga *cookies* yang dapat melacak tanpa sepengetahuan kita.

#### **2. Risiko Potensial**
Terdapat beberapa risiko umum dari *cookie*, di antaranya:
* *Cross-site request forgery attack (XSRF):* Serangan terjadi karena situs web tidak dapat membedakan aksi yang diterima berasal dari pengguna atau tidak, yang mengakibatkan penghapusan data.
* *Session fixation:* Serangan terjadi karena penyerang memaksa pengguna untuk menggunakan *session id* sesi penyerang atau orang lain, yang mengakibatkan tampilan pengguna terlihat seperti punya orang lain.
* *Cookie overflow attack:* Serangan terjadi karena melibatkan penggantian *cookie* domain utama dengan subdomain *cookie* menggunakan `JScript` di subdomain, yang mengakibatkan seluruh *cookie* tidak berguna.  
<br>

*Source:*
* https://allaboutcookies.org/information-in-cookies
* https://resources.infosecinstitute.com/topics/general-security/risk-associated-cookies/
<br>

## **E. Implementasi *Checklist* Part 3**
#### **Implementasi Fungsi Registrasi, Login, dan Logout**
1. Pertama, saya menjalankan *virtual environment* dan membuka `views.py` pada subdirektori `main`.
<br>

2. Kedua, saya membuat fungsi bernama `register` dan menambahkan beberapa *import*, di antaranya adalah `redirect`, `UserCreationForm`, dan `messages` seperti berikut.
``` python
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages  
```
<br>

3. Ketiga, saya membuat fungsi bernama `login_user` dan menambahkan beberapa *import*, di antaranya adalah `authenticate` dan `login` seperti berikut.
``` python
from django.contrib.auth import authenticate, login
```
<br>

4. Keempat, saya membuat fungsi bernama `logout_user` dan menambahkan *import* `logout` seperti berikut.
```python
from django.contrib.auth import logout
```
<br>

5. Kelima, saya menambahkan kode fungsi `register` seperti berikut.
``` python
def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)
```
<br>

6. Keenam, saya menambahkan kode fungsi `login_user` seperti berikut.
``` python
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('main:show_main')
        else:
            messages.info(request, 'Sorry, incorrect username or password. Please try again.')
    context = {}
    return render(request, 'login.html', context)
```
<br>

7. Ketujuh, saya menambahkan kode fungsi `logout_user` seperti berikut.
``` python
def logout_user(request):
    logout(request)
    return redirect('main:login')
```
<br>

8. Kedelapan, saya membuat berkas HTML baru dengan nama `register.html` dan `login.html` pada folder `main/templates` dengan kode yang sesuai dengan kreasi saya.
<br>

9. Kesembilan, saya menuju `urls.py`yang ada di subdirektori `main` dan mengimpor beberapa fungsi seperti berikut.
``` python
from main.views import register
from main.views import login_user
from main.views import logout_user
```
<br>

10. Kesepuluh, saya menambahkan kode pada `main.html` setelah *hyperlink tag* untuk *Add New Order* seperti berikut.
``` html
...
<a href="{% url 'main:logout' %}">
    <button style="color: maroon; font-weight: bolder; align-items: center">
        Logout
    </button>
</a>
...
```
<br>

11. Kesebelas, saya menambahkan *path url* dalam `urlpatterns` agar dapat mengakses fungsi yang diimpor seperti berikut.
``` python
...
path('register/', register, name='register'),
path('login/', login_user, name='login'),
path('logout/', logout_user, name='logout'),
...
```
<br>

12. Lalu, saya menambahkan beberapa *import* pada `views.py` di subdirektori `main` seperti berikut.
``` python
from django.contrib.auth.decorators import login_required
```

13. Saya juga menambahkan `@login_required...` pada fungsi `show_main` seperti berikut.
``` python
...
@login_required(login_url='/login')
def show_main(request):
...
```
<br>

#### **Menerapkan *Cookies* pada Halaman Utama**
1. Pertama, saya *logout* terlebih dahulu. Lalu, saya membuka `views.py` di subdirektori `main` dan menambahkan beberapa impor seperti berikut.
``` python
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
```
<br>

2. Kedua, saya mengganti fungsi `login_user` di `views.py` menjadi seperti berikut.
``` python
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main")) 
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.info(request, 'Sorry, incorrect username or password. Please try again.')
    context = {}
    return render(request, 'login.html', context)
```
<br>

3. Ketiga, saya menambahkan kode `'last_login': request.COOKIES['last_login']` di variabel `context` pada fungsi `show_main`yang terletak di `views.py` seperti berikut.
``` python
    context = {
        'name': 'Vina Myrnauli Abigail Siallagan',
        'class': 'PBP E', 
        'customer': request.user.username,
        'products': products,
        'total_product': total_product,
        'last_login': request.COOKIES['last_login'],
    }
```
<br>

4. Keempat, saya mengubah kode pada fungsi `logout_user` seperti berikut.
``` python
def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response
```
<br>

#### **Menampilkan Informasi Penggguna yang *Logged In***
1. Saya menambahkan beberapa kode pada `main.html` di antara tabel dan tombol `logout` seperti berikut.
``` html
<h5>Last login: {{ last_login }}</h5>
```
<br>

#### **menghubungkan model `Product` dengan `User`**
1. Saya menambahkan *import* di subdirektori `main` yang ada di `models.py` seperti berikut.
``` python
from django.contrib.auth.models import User
```
<br>

2. Lalu, pada `models.py` di model `Product` yang sudah dibuat, saya menambahkan kode seperti berikut.
``` python
class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ...
```
<br>

3. Selanjutnya, saya menuju `views.py` yang ada di subdirektori `main`. Kemudian, saya menambahkan kode pada fungsi `create_product` seperti berikut.
``` python
def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        product = form.save(commit=False)
        product.user = request.user
        product.save()
        return HttpResponseRedirect(reverse('main:show_main'))
    ...
```
<br>

4. Terakhir, saya mengubah satu baris pada fungsi `show_main` seperti berikut.
``` python
def show_main(request):
    products = Product.objects.filter(user=request.user)
    total_product = len(products)
   ...
...
```
<br>

#### **Membuat Dua Akun dengan Tiga *Dummy Data***
1. Pertama, saya membuka `command` dan menjalankan *virtual environment* seperti berikut.
``` bash
env\Scripts\activate.bat
```
<br>

2. Kedua, saya menjalankan proyek Django dengan perintah `python manage.py runserver` dan membuka `http://localhost:8000`.
<br>

3. Ketiga, saya melakukan *register* pada dua akun yang bernama `halodok` dan `vinamyrnauli`. 
<br>

4. Keempat, saya melakukan *login* dengan memasukkan `username` dan `password`.
<br>

5. Pada tiap akun tersebut, saya klik `Add New Order`. Lalu, saya tambahkan produk sebanyak tiga kali dan mengisi `Name`, `Price`, `Amount`, dan `Description`.
<br>

6. Setelah itu, saya klik `Add Product` dan produk sudah ada terpampang jelas di `main.html`.
<br>

## **F. BONUS TUGAS 4**
Berikut adalah bukti bahwa saya menambahkan fungsi `add_product`, `decrement_product`, dan `remove_product` di `views.py` sehingga dapat menghasilkan tampilan seperti berikut.
![COBA](/photos/bonusfour.jpg)
<br>
</details>

<details>
<summary>📋Assignment 5</summary>

## **DAFTAR ISI**
* [Manfaat *Element Selector* dan Penggunaan Waktunya](#a-manfaat-tiap-element-selector-dan-penggunaan-waktu-yang-tepatnya)
* [Penjelasan HTML5 Tag](#b-penjelasan-html5-tag)
* [Perbedaan *Margin* dan *Padding*](#c-perbedaan-margin-dan-padding)
* [Perbedaan dan Penggunaan *framework* CSS Tailwind dan Bootstrap](#d-perbedaan-dan-penggunaan-framework-css-tailwind-serta-bootstrap)
* [Implementasi *Checklist*](#e-implementasi-checklist-tugas-5)
* [BONUS TUGAS 5](#f-bonus-tugas-5)
<hr>

## **A. Manfaat Tiap *Element Selector* dan Penggunaan Waktu yang Tepatnya**
#### **1. *Element Selector***
* **Manfaat:**
    * Dapat mengubah properti untuk semua elemen yang memiliki tag HTML yang sama atau dapat memilih elemen HTML berdasarkan nama elemen.
    * Dapat mengaplikasikan *style* yang sama pada tiap elemen dengn jenis yang sama, contohnya seperti tag `<p>` atau `<h1>`.
* **Penggunaan Waktu yang Tepat:**
    * Ketika kita ingin mengubah *style* tiap elemen dengan jenis yang sama dan tidak ada *class* maupun ID khusus. 
<br>

#### **2. *ID Selector***
* **Manfaat:**
    * Dapat memilih elemen berdasarkan ID yang diberikan. IDnya unik dalam satu halaman web dan dapat ditambahkan pada halaman template HTML.
* **Penggunaan Waktu yang Tepat:**
    * Ketika ingin memberikan interaksi atau *style* khusus pada satu elemen tertentu.
<br>

#### **3. *Class Selector***
* **Manfaat:**
    * Dapat mengelompokkan elemen dengan karakteristik yang sama.
    * Dapat memilih elemen berdasarkan nama *class* yang diberi.
* **Penggunaan Waktu yang Tepat:**
    * Ketika ingin memberikan *style* yang identik terhadap beberapa elemen dalam halaman.
<br>

*Source:*
* https://www.w3schools.com/CSS/css_selectors.asp
<br>

## **B. Penjelasan HTML5 Tag**
| Tag | Penjelasan |
| --- | --- |
| `<a>` | Mendefinisikan *hyperlink* |
| `<abbr>` | Mendefinisikan bentuk singkatan dari kata atau frasa yang panjang |
| `<address>` | Menentukan informasi kontak penulis |
| `<area>` | Mendefinisikan area tertentu dalam peta gambar |
| `<!--...-->` | Menentukan komentar |
| `<!DOCTYPE>` | Menentukan jenis dokumen |
| `<div>` | Menentukan bagian dalam dokumen |
| `<detail>` | Menentukan informasi tambahan yang dapat diperoleh pengguna |
| `<header>` | Menentukan informasi tentang dokumen |
| `<q>` | Menentukan variabel |
| `<select>` | Menentukan daftar yang dapat dipilih |
| `<spacer>` | Menentukan *white space* |
| `<style>` | Menentukan definisi gaya |
| `<table>` | Menentukan tabel |

<br>

*Source:*
* https://www.tutorialrepublic.com/html-reference/html5-tags.php
* https://www.tutorialspoint.com/html5/html5_tags.htm
<br>

## **C. Perbedaan *Margin* dan *Padding***
![COBA](/photos/marginpadding.png)
| *Margin* | *Padding* |
| --- | --- |
| Mengosongkan area di sekitar border (transparan) | Mengosongkan area di sekitar konten (transparan) |
| Ruang luar suatu elemen yaitu *margin* yang merupakan ruang di luar batas | Ruang dalam suatu elemen *padding* yaitu ruang dalam batas elemen |
| Dapat berupa angka negatif atau *float* | Tidak boleh ada nilai-nilai negatif |
| Mengatur *margin* menjadi otomatis | Tidak dapat mengatur *padding* menjadi otomatis |
| Penataan *style* elemen seperti warna *backgorund* tidak memengaruhi *margin* | *Padding* dipengaruhi *style* suatu elemen seperti *background* |

<br>

*Source:*
* https://www.geeksforgeeks.org/css-padding-vs-margin/
<br>

## **D. Perbedaan dan Penggunaan *framework* CSS Tailwind serta Bootstrap**
| Tailwind | Bootstrap |
| --- | --- |
| Membangun tampilan dengan menggabungkan *class-class* utilitas yang telah didefinisikan sebelumnya | Menggunakan *style* dan komponen yang sudah didefinisikan, memiliki tampilan yang sudah jadi dan dapat digunakan langsung |
| Memiliki *file* CSS yang lebih kecil dan memuat *class-class* utilitas yang ada | Memiliki *file* CSS yang lebih besar karena termasuk banyak komponen yang telah didefinisikan |
| Memberikan fleksibilitas dan adaptabilitas tinggi terhadap proyek | Menghasilkan tampilan yang lebih konsisten di seluruh proyek karena memakai komponen yang sudah didefinisikan |
| Memiliki pembelajaran lebih curam karena perlu pemahaman terhadap *class-class* utilitas yang tersedia dan cara menggabungkannya untuk mencapai tampilan yang kita inginkan | Memiliki pembelajaran yang lebih cepat untuk pemula karena dapat mulai dengan komponen yang sudah didefinisikan |

<br>

Kapan sebaiknya kita menggunakan Bootstrap daripada Tailwind, dan sebaliknya?

* ***Bootsrap:***
    * Apabila ingin membangun situs web dengan cepat.
    * Apabila ingin menggunakan komponen-komponen bawaan yang sudah dirancang.
    * Apabila ingin menjaga konsistensi dalam desain.

* ***Tailwind:***
    * Apabila ingin memiliki kontrol yang lebih besar dalam merancang tampilan sesuai preferensi.
    * Apabila ingin menggunakan *class-class* CSS yang ada pada Tailwind.
    * Apabila ingin mengurangi ukuran berkas CSS untuk meningkatkan kinerja situs web.
   

*Source:*
* https://www.tutorialspoint.com/tailwind-css-vs-bootstrap
* https://pbp-fasilkom-ui.github.io/ganjil-2024/docs/tutorial-4
<br>

## **E. Implementasi *Checklist* Tugas 5**
#### **1. Design Login Page**
Pertama, saya melakukan kustomisasi desain dengan menggunakan CSS *framework* yaitu Bootstrap, lalu saya melakukan instalasi Bootstrap dan lainnya.

``` html
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN" crossorigin="anonymous">
<script src="https://code.jquery.com/jquery-3.6.0.min.js" integrity="sha384-KyZXEAg3QhqLMpG8r+J4jsl5c9zdLKaUk5Ae5f5b1bw6AUn5f5v8FZJoMxm6f5cH1" crossorigin="anonymous"></script>
<script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.11.8/dist/umd/popper.min.js" integrity="sha384-I7E8VVD/ismYTF4hNIPjVp/Zjvgyol6VFvRkX/vR+Vc4jQkC+hVqc2pM8ODewa9r" crossorigin="anonymous"></script>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.min.js" integrity="sha384-BBtl+eGJRgqQAUMxJ7pMwbEyER4l1g+O15P+16Ep7Q9Q+zqX6gSbd85u4mG4QzX+" crossorigin="anonymous"></script>
```

Selanjutnya, saya melakukan kustomisasi pada *Login Page* seperti berikut.
![LOGINPAGE](/photos/loginpage.jpg)

Berikut adalah kode yang saya modifikasi.
``` html
{% extends 'base.html' %}

{% block meta %}
    <title>Login</title>
{% endblock meta %}

{% block content %}
<style>
    .centered-elements {
      text-align: center;
    }

    .centered-elements .btn,
    .centered-elements p {
      display: inline-block;
      vertical-align: middle;
      margin: 0;
    }
</style>
<section class="vh-100">
    <div class="container py-5 h-100">
      <div class="row d-flex align-items-center justify-content-center h-100">
        <div class="col-md-8 col-lg-7 col-xl-6">
          <img src="https://i.ibb.co/8bzR20H/dog-png.webp"
            class="img-fluid" alt="Phone image">
        </div>
        <div class="col-md-7 col-lg-5 col-xl-5 offset-xl-1">
          <form method="POST" action="">
            {% csrf_token %}
            <!-- Email input -->
            <div class="form-outline mb-4">
              <label class="form-label" for="form1Example13">Username</label>
              <input type="text" name="username" id="username" class="form-control" placeholder="Username">
            </div>
  
            <!-- Password input -->
            <div class="form-outline mb-4">
              <label class="form-label" for="form1Example23">Password</label>
              <input type="password" name="password" id="password" class="form-control" placeholder="Password">
            </div>
  
            <!-- Submit button -->
            <div class="centered-elements">
                <!-- Submit button -->
                <a href="{% url 'main:register' %}" class="btn btn-primary btn-lg" style="background-color:peru; border-color: whitesmoke;">Sign up</a>
                
                <p class="text-center fw-bold mx-3 mb-0 text-muted">OR</p>

              
                <button type="submit" class="btn btn-primary btn-lg" style="background-color:sienna; border-color: whitesmoke;" value="Login">Log in</button>
            </div>
  
        </form>
        {% if messages %}
            <ul class="mt-3">
                {% for message in messages %}
                    <li>{{ message }}</li>
                {% endfor %}
            </ul>
        {% endif %}
        </div>
      </div>
    </div>
  </section>

<body style="background-image: url(https://i.ibb.co/zXgLwgP/4-7315db01-be96-4931-889c-8142cb97b580.webp); background-size: cover; background-position: center;">
{% endblock content %}
```
<br>

#### **2. Design Register Page**
Lalu, saya memberikan beberapa tambahan pada *Register Page* seperti berikut.
![REGISTERPAGE](/photos/registerpage.jpg)

Berikut adalah rincian hode *Register Page* saya.
``` html
{% extends 'base.html' %}

{% block meta %}
    <title>Register</title>
{% endblock meta %}

{% block content %}  
<body class="container-fluid" style="background-color:bisque;"> 
    <div class="container mt-5">
        <div class="row justify-content-center">
            <div class="col-md-6">
                <div class="card">
                    <div class="card-header bg-primary text-white">
                        <h3 class="card-title">Register</h3>
                    </div>
                    <div class="card-body">
                        <form method="POST">
                            {% csrf_token %}

                            <div class="form-group">
                                {{ form.username.label_tag }}
                                {{ form.username }}
                            </div>

                            <div class="form-group">
                                {{ form.email.label_tag }}
                                {{ form.email }}
                            </div>

                            <div class="form-group">
                                {{ form.password1.label_tag }}
                                {{ form.password1 }}
                            </div>

                            <div class="form-group">
                                {{ form.password2.label_tag }}
                                {{ form.password2 }}
                            </div>

                            <button type="submit" class="btn btn-success">Register</button>
                        </form>
                        
                        {% if messages %}
                        <ul>
                            {% for message in messages %}
                            <li>{{ message }}</li>
                            {% endfor %}
                        </ul>
                        {% endif %}
                    </div>
                </div>
            </div>
        </div>
    </div>
</body>
{% endblock content %}
```
<br>

#### **3. Design Edit Product dan Add Product Page**
Kemudian, saya mengubah beberapa kode pada *Edit dan Add Product Page* seperti berikut.
**1. *Edit Product***
![ADDPRODUCT](/photos/editproduct.jpg)
<br>

**2. *Add Product***
![ADDPRODUCT](/photos/addproduct.jpg)
<br>

Berikut adalah rincian hode *Edit dan Add Product* saya.
**A. *Edit Product***
``` html
{% extends 'base.html' %}

{% block content %}
<div class="container mt-5">
    <div class="row justify-content-center">
        <div class="col-md-6">
            <div class="card">
                <div class="card-header bg-primary text-white">
                    <h3 class="card-title">Edit Product</h3>
                </div>
                <div class="card-body">
                    <form method="POST">
                        {% csrf_token %}
                        <table class="table">
                            {{ form.as_table }}
                            <tr>
                                <td></td>
                                <td>
                                    <button type="submit" class="btn btn-success">Edit Product</button>
                                </td>
                            </tr>
                        </table>
                    </form>
                </div>
            </div>
        </div>
    </div>
</div>
{% endblock %}
```
<br>

**B. *Add Product***
``` html
{% extends 'base.html' %} 

{% block content %}
<div class="container mt-5">
    <div class="row justify-content-center">
        <div class="col-md-6">
            <div class="card">
                <div class="card-header bg-success text-white">
                    <h3 class="card-title">Add New Product</h3>
                </div>
                <div class="card-body">
                    <form method="POST">
                        {% csrf_token %}
                        <table class="table">
                            {{ form.as_table }}
                            <tr>
                                <td>
                                    <button type="submit" class="btn btn-primary">Add Product</button>
                                </td>
                            </tr>
                        </table>
                    </form>
                </div>
            </div>
        </div>
    </div>
</div>

<style>
    body {
        background-color: pink;
    }

    tr {
        color: saddlebrown;
        font-weight: bolder;
        font-family: Arial, sans-serif;
    }
</style>
{% endblock %}
```
<br>

#### **4. Design Main Page**
Terakhir, saya memodifikasi *Main Page* seperti berikut ini.
![MAINPAGE](/photos/mainpage.jpg)
Berikut adalah rincian hode *Design Main Page* saya.
``` html
{% extends 'base.html' %}

{% block content %}
<style>
.button-container {
    display: flex;
    align-items: center;
    justify-content: space-evenly;
    padding: 10px;
    margin-right: 5px;
}

h2 {
    color: crimson;
    font-family: Arial, sans-serif;
    font-size: larger;
    text-align: center;
    font-weight: bolder;
}

h3 {
    color: black;
    font-family: Arial, sans-serif;
    font-size: small;
    font-weight: bolder;
    text-align: center;
}

h4 {
    color: crimson;
    font-weight: bolder;
    font-size: large;
    font-family: Arial, sans-serif;
}

th {
    text-align: center;
}

td {
    text-align: center;
}
</style>

<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Icons</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
</head>

<body class="bg-image h-100" style="background-color: #6095F0;">
    <div class="mask d-flex align-items-center h-100">
        <div class="container">
            <div class="row justify-content-center">
                <div class="col-12">
                    <div class="card shadow-2-strong" style="background-color: #f5f7fa;">
                        <div class="card-body">
                            <div class="table-responsive">
                                <table class="table table-borderless mb-0">
                                    <thead>
                                        <h1 style="color: saddlebrown; font-family: Arial, sans-serif; font-weight: bolder; display: flex; flex-direction: row; justify-content: space-evenly; align-items: center;text-shadow: 2px 2px 4px #000;">🥤🐶SCOOBYRIA🐶🍔</h1>
                                        <h2>Hello, {{ customer }} !</h2>
                                        <h3>SCOOBYRIA provides food and drinks for the PBP E adventurers. The food and drinks provided can be either delicious or unpleasant, depending on their description. If you choose to consume toxic food or beverages, the choice is at your own risk.</h3>
                                        <h4>{{ total_product }} ITEMS(S) AVAILABLE</h4>
                                        <tr>
                                            <th scope="col">NAME</th>
                                            <th scope="col">PRICE</th>
                                            <th scope="col">AMOUNT</th>
                                            <th scope="col">DESCRIPTION</th>
                                            <th scope="col">DETAILS</th>
                                            <th scope="col">CUSTOMIZE</th>
                                        </tr>
                                    </thead>
                                    <tbody>
                                        {% for product in products %}
                                        <tr class="add-colortext">
                                            <td>{{product.name}}</td>
                                            <td>{{product.price}}</td>
                                            <td>{{product.amount}}</td>
                                            <td>{{product.description}}</td>
                                            <td>
                                                <div class="button-container">
                                                    <form action="{% url 'main:add_product' product.id %}" method="post">
                                                        {% csrf_token %}
                                                        <button class="btn btn-success btn-sm px-3 shadow" type="submit" name="Tambah"><i class="fa fa-plus" aria-hidden="true" ></i></button>
                                                    </form>
                                                    <form action="{% url 'main:decrement_product' product.id %}" method="POST">
                                                        {% csrf_token %}
                                                        <button class="btn btn-warning btn-sm px-3 shadow" type="submit" name="Kurang"><i class="fa fa-minus" aria-hidden="true"></i></button>
                                                    </form>
                                                    <form action="{% url 'main:remove_product' product.id %}" method="post">
                                                        {% csrf_token %}
                                                        <button class="btn btn-danger btn-sm px-3 shadow" type="submit" name="Hapus"><i class="fa fa-times" aria-hidden="true"></i></button>
                                                    </form>
                                                </div>
                                            </td>
                                            <td>
                                                <div class="button-container">
                                                    <a href="{% url 'main:edit_product' product.pk %}">
                                                        <button class="btn btn-primary btn-sm px-3 shadow" name="Edit">Edit</button>
                                                    </a>
                                                </div>
                                            </td>
                                        </tr>
                                        {% endfor %}
                                    </tbody>
                                </table>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <div class="button-container">
        <a href="{% url 'main:create_product' %}" class="btn btn-success btn-sm px-50 shadow">
            <i class="fa fa-clipboard" aria-hidden="true"></i> Add New Order
        </a>
        
        <a href="{% url 'main:logout' %}" class="btn btn-danger btn-sm px-50 shadow">
            <i class="fa fa-home" aria-hidden="true"></i> Logout
        </a>
    </div>

</body>

<div class="bg-light py-4">
    <div class="container text-center">
        <p class="text-muted mb-0 py-2">Name: {{ name }}</p>
        <p class="text-muted mb-0 py-2">Class: {{ class }}</p>
    </div>
</div>

{% endblock content %}
```
<br>

#### **F. BONUS TUGAS 5**
Berikut adalah bukti bahwa saya menambahkan bonus seperti berikut.
``` html
<style>
.button-container {
    display: flex;
    align-items: center;
    justify-content: space-evenly;
    padding: 10px;
    margin-right: 5px;
}

h2 {
    color: crimson;
    font-family: Arial, sans-serif;
    font-size: larger;
    text-align: center;
    font-weight: bolder;
}

h3 {
    color: black;
    font-family: Arial, sans-serif;
    font-size: small;
    font-weight: bolder;
    text-align: center;
}

h4 {
    color: crimson;
    font-weight: bolder;
    font-size: large;
    font-family: Arial, sans-serif;
}

th {
    text-align: center;
}

td {
    text-align: center;
}
</style>
```
</details>

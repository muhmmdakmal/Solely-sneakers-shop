<h1>Solely Sneakers Shop</h1>
<h2>
   
   Nama  : Muhammad Akmal Abdul Halim
   
   NPM   : 2306245125
  
   Kelas : PBP-D
</h2>

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

<details>
   <summary> Tugas 2: Implementasi Model-View-Template (MVT) pada Django </summary>
   
**1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).** 
   
      1. Membuat repository baru dan meng-clone ke directory yang diinginkan
      2. Membuat Virtual environment dan menjalankannya di command promt
      3. Membuat file requrements.txt dan mendownload didalam VM
      4. Membuat project django sesuai dengan nama project
      5. Menambahkan string alamat ip di dalam list ALLOWED_HOST di settings.py
      6. Tambahkan berkas .gitignore untuk mengabaikan hal-hal yang tidak perlu di push
      7. Membuat project baru di website PWS (Jangan lupa mencatat info penting sepertu username dan password)
      8.  Melakukan add, commit, push untuk meng-save yang sudah dilakukan
      9.  Menjalankan command "python manage.py startapp main" untuk membuat directory baru bernama main
      10. Menambahkan "main" didalam list INSTALLED_APPS didalam file settings.py untuk mendaftarkan aplikasi 'main' ke proyek
      11. Buat directory baru bernama templates dan buat main.html isi seusai design proyek yang diinginkan
      12. Membuka models.py dan mengedit sesuai dengan kebutuhan anda
      13. Melakukan migration
      14. Mengedit views.py dan menambahkan dictionary sesuai kebutuhan anda
      15. Melakukan routing di urls.py didalam directory main dan directory proyek anda
      16. Menjalankan preintah 'python manage.py runserver' lalu pergi ke url 'http://localhost:8000/' untuk mengecek proyek anda
      17. Melakukan add,commit,push ke pws master agar proyek anda bisa dilihat orang-orang

**2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.**
   ![Untitled Diagram drawio](https://github.com/user-attachments/assets/9ef27e87-448f-4ce7-821d-78bb94589679)

   1. Pertama, pengguna akan melakukan permintaan HTTP, yang kemudian akan diproses oleh View. Untuk mengetahui apa yang diminta dan apa yang akan diberikan tanggapan, akan menentukan 
      urls.py. Kemudian, berdasarkan pattern url yang diminta, akan menentukan function View yang akan dijalankan di Views.py.
   2. Kedua, Data yang dibutuhkan untuk ditampilkan diminta oleh tampilan; data tersebut sudah tercantum dalam function view yang dijalankan, dan tampilan akan mendapatkan field data           yang tersedia di models.py.
   3. Untuk menentukan berkas HTML yang akan dipopulasikan dengan data pada Template, View akan meminta berkas HTML yang telah ditentukan dalam function View. Setelah mendapatkan berkas 
      HTML yang diminta, kemudian User akan menerima HTML yang telah dipopulasikan dengan data dalam bentuk HTTP.
      
**3. Jelaskan fungsi git dalam pengembangan perangkat lunak!**
   Berikut adalah fungsi git dalam pengembangan perangkat lunak :
   - Tracking Perubahan Kode (Version Control):
   Git melacak setiap perubahan yang dilakukan pada kode, memungkinkan pengembang untuk melihat riwayat perubahan dan mengetahui siapa yang melakukan perubahan tersebut. Setiap perubahan
   disimpan sebagai sebuah commit, yang berisi deskripsi perubahan dan bisa dikembalikan atau diperiksa kapan saja.
   
   - Kolaborasi Tim:
   Git memungkinkan banyak pengembang untuk bekerja pada proyek yang sama secara bersamaan. Setiap pengembang bisa bekerja pada cabang (branch) terpisah, lalu menggabungkan (merge) 
   pekerjaannya kembali ke cabang utama (main branch) setelah selesai. Ini menghindari konflik kode dan memudahkan kolaborasi tanpa gangguan satu sama lain.

   - Branching dan Merging:
   
      1.Branching memungkinkan pengembang membuat salinan independen dari kode untuk mengembangkan fitur baru atau memperbaiki bug tanpa memengaruhi kode utama. Setelah fitur selesai             cabang tersebut bisa digabungkan (merging) kembali ke cabang utama.
      2.Branching juga mempermudah pengelolaan siklus pengembangan seperti pengembangan fitur, perbaikan bug, dan rilis versi produk.

   - Membantu dalam Pengelolaan Proyek Besar:
   Git sangat berguna dalam proyek besar yang melibatkan banyak pengembang atau banyak fitur yang sedang dikembangkan secara bersamaan. Dengan menggunakan Git, proyek bisa dibagi ke   
   dalam cabang-cabang terpisah, memastikan stabilitas cabang utama, dan menghindari risiko mengacaukan proyek dengan perubahan yang belum diuji.

   - Revert Kode:
   Jika terjadi kesalahan, Git memungkinkan pengembang untuk mengembalikan (revert) kode ke versi sebelumnya. Ini sangat berguna dalam kasus ketika fitur baru menyebabkan bug atau 
   masalah, dan pengembang ingin kembali ke versi stabil dari kode.

   - Distribusi dan Penyimpanan Kode Secara Terpusat:
   Git bekerja secara terdistribusi, artinya setiap pengembang memiliki salinan penuh dari seluruh repositori (riwayat kode). Namun, biasanya repositori utama disimpan di layanan seperti 
   GitHub, GitLab, atau Bitbucket, yang juga menyediakan platform berbasis cloud untuk berbagi kode secara aman antar anggota tim.

   - Integrasi dengan Alat Lain:
   Git terintegrasi dengan banyak alat Continuous Integration (CI) dan Continuous Deployment (CD), sehingga pengujian otomatis, build, dan deployment bisa dijalankan setiap kali ada 
   perubahan pada kode. Ini mempercepat pengembangan dengan memastikan bahwa setiap perubahan telah diuji dan siap untuk diluncurkan.

   - Dokumentasi dan Transparansi:
   Setiap commit di Git disertai dengan pesan commit, yang memungkinkan pengembang untuk menuliskan informasi terkait perubahan tersebut. Ini memudahkan dokumentasi dan memberikan 
   transparansi pada seluruh proses pengembangan.

**4. Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?**

   Menurut saya, karena Django adalah salah satu framework yang mudah dipelajari untuk pemula. Django juga menggunakan bahasa python yang merupakan bahasa pemrograman populer dan ramah      untuk pemula. Django memiliki dokumentasi terbaik dibandingkan framework lainnya, bagi pemula yang baru pertama kali belajar framework web, dokumentasi yang bagus bisa menjadi panduan    utama untuk menyelesaikan masalah tanpa kebingungan. Secara keseluruhan, Django adalah pilihan yang ideal bagi pemula karena kesederhanaan, keteraturan, dan dokumentasi yang kuat,        serta fitur-fitur yang langsung siap digunakan.

**5. Mengapa model pada Django disebut sebagai ORM?**

   Model pada Django disebut sebagai ORM (Object-Relational Mapping) karena model dalam Django berfungsi sebagai jembatan antara objek-objek dalam kode Python dan tabel-tabel dalam basis    data relasional.
   </details>
   
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

<details>
   <summary> Tugas 3: Implementasi Form dan Data Delivery pada Django </summary>
   
**1. Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?**
   
   Data delivery diperlukan dalam pengimplementasian sebuah platform karena itu adalah proses untuk mentransfer informasi dari satu bagian sistem ke bagian lain. Misalnya, dari server ke 
   client atau antar sistem yang berbeda. Ini sangat penting karena:
   - Kecepatan Akses Data: Pengguna membutuhkan data secara real-time atau secepat mungkin. Tanpa mekanisme data delivery yang baik, akses data bisa lambat, yang akan mempengaruhi 
     performa platform secara keseluruhan.
   - Konsistensi Data: Data harus tetap konsisten dan akurat ketika ditransfer antar bagian sistem. Data delivery yang baik memastikan tidak ada kehilangan data atau perubahan yang tidak 
     diinginkan selama pengiriman.
   - Komunikasi Antar Komponen: Platform sering kali terdiri dari berbagai komponen yang bekerja bersama. Data delivery memungkinkan setiap komponen untuk bertukar informasi dan 
     berfungsi sesuai dengan tujuannya.
   - Efisiensi Operasional: Proses pengiriman data yang efektif dan efisien memastikan bahwa platform dapat beroperasi dengan lancar tanpa terjadi bottleneck atau keterlambatan dalam 
     proses.

**2. Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?**

   Menurut saya yang lebih baik antara XML dan JSON adalah JSON. Alasan megapa JSON lebih populer dibandingkan XML yaitu :
   - Kebersihan dan Kesederhanaan Sintaks : JSON memiliki sintaks yang lebih sederhana dan lebih mudah dibaca oleh manusia. Formatnya menggunakan pasangan key-value yang mirip dengan 
     objek pada bahasa pemrograman seperti JavaScript. XML, di sisi lain, menggunakan tag pembuka dan penutup yang membuat dokumen bisa jadi panjang dan kompleks, terutama ketika data 
     yang dikirimkan cukup banyak.
   - Ukuran File Lebih Ringan : JSON cenderung lebih ringan dibandingkan XML karena tidak memerlukan tag yang berpasangan seperti pada XML. Ini membuat JSON lebih efisien dalam hal 
     ukuran dan waktu pengiriman data.
   - Kecepatan Parsing : JSON lebih cepat diproses oleh banyak sistem dibandingkan XML. Hal ini karena JSON bisa langsung diparsing menjadi objek JavaScript, sementara XML biasanya 
     memerlukan langkah parsing yang lebih rumit.

**3. Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?**

   Method is_valid() pada form Django digunakan untuk memeriksa apakah data yang dimasukkan ke dalam form sesuai dengan aturan validasi yang ditetapkan. Jika data valid, method ini 
   mengisi atribut cleaned_data yang berisi data bersih siap pakai. Jika tidak valid, method ini mengembalikan False dan menyimpan pesan error di atribut errors.
   Kita membutuhkan is_valid() untuk:
   - Memastikan hanya data yang valid yang diproses.
   - Meningkatkan keamanan aplikasi dengan mencegah input berbahaya.
   - Memberikan umpan balik yang jelas ke pengguna untuk memperbaiki kesalahan input mereka.

**4.  Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat 
    dimanfaatkan oleh penyerang?**

    - Mengapa csrf_token dibutuhkan?
      csrf_token adalah token keamanan unik yang dibuat oleh server dan disertakan di dalam form. Token ini divalidasi setiap kali form dikirim untuk memastikan bahwa permintaan berasal 
      dari sumber yang sah (yaitu pengguna yang sah dan bukan dari pihak luar).
    - Apa yang dapat terjadi jika tidak menambahkan csrf_token?
      Jika form Django tidak menyertakan csrf_token, aplikasi menjadi rentan terhadap serangan CSRF. Penyerang bisa memanfaatkan celah ini dengan mengirimkan permintaan berbahaya yang 
      tampak seperti berasal dari pengguna sah. Misalnya, penyerang bisa membuat pengguna tanpa sadar mengirimkan formulir yang berisi perintah untuk mengubah data penting atau 
      melakukan transaksi tanpa persetujuan mereka.
    - Bagaimana penyerang bisa memanfaatkannya?
      Penyerang dapat:
      1. Mengirimkan link berbahaya atau menyisipkan form tersembunyi di situs lain.
      2. Saat pengguna mengklik link atau mengunjungi situs tersebut, permintaan palsu dikirimkan ke aplikasi target dengan menggunakan sesi login pengguna.
      3. Aplikasi tanpa csrf_token tidak bisa membedakan apakah permintaan tersebut sah atau tidak, sehingga permintaan berbahaya bisa dieksekusi dengan sukses, misalnya mentransfer 
         uang atau mengubah kata sandi pengguna.

**5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).**

   1. Buat directory dengan nama "templates" diroot lalu buatlah file base.html didalam folder tersebut.
   2. Isi file base.html.
   3. Buka settings.py lalu tambahkan 'templates' di dalam dictionary TEMPLATES di key 'DIRS'.
   4. Tambahkan import uuid di file models.py di dalam directory main. Lalu melakukan migration.
   5. Buat file forms.py yang berguna untuk mengambil data dari models.py.
   6. Tambahkan beberapa import didalam file views.py yang berguna untuk mengambil data dari models.py dan forms.py.
   7. Buat function didalam views.py untuk menghasilkan formnya.
   8. Tambahkan variable didalam function show_main() untuk mengambil semua object didalam models.py. Tambahkan juga didalam dictionary context yang berisi variable itu.
   9. Tambahkan import di file urls.py untuk menghubungkan ke html baru yang nanti akan berguna untuk user mengisi form. Tambahkan juga di list 'urlpatterns'.
   10. Buatlah file html yang sesuai dengan nama yang anda isi didalam file urls.py.
   11. Isi file html form tersebut sesuai dengan keinginan anda. Jangan lupa untuk menambahkan {% csrf_token %} didalam file html anda untuk melindungi data user.
   12. Lalu di file main.html tambahkan code untuk mengarahkan user ke page form yang juga berupa html yang sudah kita buat.
   13. Untuk mengakses data user lebih mudah, kita akan menambahkan beberapa import dan function di dalam views.py.
   14. Tambahkan import from django.http import HttpResponse dan from django.core import serializers didalam file views.py
   15. Buatlah function baru show_xml(), show_json(), show_xml_by_id(), dan show_json_by_id() yang menerima parameter request untuk show xml dan show json dan menerima parameter request 
       dan id untuk show xml by id dan show json by id.
   16. Lalu kita tambahkan import berupa nama-nama function tersebut didalam file urls.py dan tambahkan path didalam list urlpatterns.

**Screenshot bukti postman :**
![XML](https://github.com/user-attachments/assets/bf66f515-2e16-48e5-aa57-f66b81a7feaf)
![json](https://github.com/user-attachments/assets/7b359c10-919d-4e97-a445-90283b4165f4)
![XML_id](https://github.com/user-attachments/assets/776310e8-61cb-45e3-b9fc-b374a8d333ca)
![json_id](https://github.com/user-attachments/assets/50c04815-a5ee-43ea-8729-e0d761901f2c)

</details>

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

<details>
   <summary> Tugas 4: Implementasi Autentikasi, Session, dan Cookies pada Django </summary>

   **1. Apa perbedaan antara HttpResponseRedirect() dan redirect()**

   1. HttpResponseRedirect():
   - HttpResponseRedirect() adalah kelas bawaan Django yang digunakan untuk mengembalikan respons HTTP yang menginstruksikan browser pengguna untuk mengunjungi URL yang berbeda.
   - Digunakan secara langsung dengan mengoperkan URL tujuan sebagai argumen.
   
   2. redirect():
   - redirect() adalah shortcut atau fungsi utilitas di Django yang menyediakan cara lebih mudah dan fleksibel untuk melakukan pengalihan.
   - Selain menerima URL, fungsi ini juga dapat menerima nama dari suatu view (dengan menggunakan nama URL patterns dari urls.py), serta argumen tambahan untuk di-parse dalam URL.

   Perbedaan Utama :
   - Fleksibilitas: redirect() lebih fleksibel karena dapat menggunakan nama URL dari urls.py dan juga bisa menangani objek, sementara HttpResponseRedirect() hanya bekerja dengan URL string secara eksplisit.
   - Kenyamanan: redirect() merupakan shortcut yang sering digunakan karena memungkinkan pengembang untuk tidak menulis URL secara langsung, melainkan menggunakan logika nama view atau object, membuat kode lebih bersih dan mudah di-maintain.

   **2. Jelaskan cara kerja penghubungan model Product dengan User!**

   Menghubungkan model Product dengan model User dalam Django biasanya dilakukan dengan membuat relasi antara keduanya. Salah satu cara umum adalah dengan menggunakan ForeignKey, yang merepresentasikan hubungan many-to-one di mana banyak produk bisa dimiliki oleh satu pengguna (user).
   
   Berikut penjelasan langkah-langkah untuk menghubungkan model Product dengan User:
   1. Membuat Model Product dengan ForeignKey ke User:
      
      Django menyediakan model User bawaan dalam django.contrib.auth.models. Untuk menghubungkannya dengan model Product, kita bisa menggunakan ForeignKey untuk menyatakan bahwa setiap produk terkait dengan satu pengguna.

      Contoh kode:
      
      ```python
      from django.db import models
      from django.contrib.auth.models import User
      
      class Product(models.Model):
          name = models.CharField(max_length=255)
          description = models.TextField()
          price = models.DecimalField(max_digits=10, decimal_places=2)
          created_at = models.DateTimeField(auto_now_add=True)
          updated_at = models.DateTimeField(auto_now=True)
          owner = models.ForeignKey(User, on_delete=models.CASCADE)  # Relasi ke model User
      
          def __str__(self):
              return self.name
      ```

      Penjelasan:
      - name: Nama produk yang disimpan sebagai CharField.
      - description: Deskripsi produk yang disimpan sebagai TextField.
      - price: Harga produk, disimpan sebagai DecimalField untuk menyimpan angka desimal dengan presisi.
      - owner: Field ini menggunakan ForeignKey untuk membuat relasi dengan model User.
      - on_delete=models.CASCADE: Opsi ini menentukan bahwa jika pengguna dihapus, semua produk yang dimiliki oleh pengguna tersebut juga akan dihapus. Jika Kita ingin perilaku berbeda, Kita bisa memilih opsi lain seperti SET_NULL atau PROTECT.
      - str(): Metode ini mengembalikan representasi string dari objek, dalam hal ini nama produk.
     
   2. Relasi di Database:

      Ketika ForeignKey digunakan, Django akan membuat kolom tambahan di tabel Product yang menyimpan ID pengguna (user_id) dari model User. Jadi, untuk setiap produk, ada nilai owner_id yang menunjukkan pengguna yang memiliki produk tersebut.

   3. Penggunaan dalam Views:

      Untuk menghubungkan produk dengan pengguna tertentu dalam view, Kita bisa mengakses atau menetapkan pengguna seperti ini:

      ```python
      from django.shortcuts import render, redirect
      from .models import Product
      from django.contrib.auth.decorators import login_required
      
      @login_required
      def create_product(request):
          if request.method == 'POST':
              product_name = request.POST.get('name')
              description = request.POST.get('description')
              price = request.POST.get('price')
      
              # Membuat produk baru dan menetapkan owner sebagai user yang sedang login
              product = Product.objects.create(
                  name=product_name,
                  description=description,
                  price=price,
                  owner=request.user  # Menetapkan pengguna yang login sebagai owner
              )
      
              return redirect('product_list')
      
          return render(request, 'create_product.html')

      ```

      Penjelasan:
      - request.user: Saat pengguna sudah login, Kita bisa mengakses objek User yang sedang login melalui request.user dan menetapkannya sebagai pemilik produk.
      - @login_required: Decorator ini memastikan bahwa hanya pengguna yang login yang bisa mengakses view ini.
     
   4. Querying Product Berdasarkan User:

      Kita bisa mengambil produk-produk milik pengguna tertentu dengan menggunakan filter pada field owner:

      ```python
      # Mendapatkan semua produk milik pengguna yang sedang login
      products = Product.objects.filter(owner=request.user)
      ```

   5. Membuat Relasi Lebih Kompleks:

      Jika dibutuhkan, Kita bisa membuat relasi lebih kompleks antara Product dan User, misalnya:
      - Many-to-many: Jika satu produk bisa dimiliki oleh beberapa pengguna.
      - One-to-one: Jika Anda ingin memastikan bahwa hanya ada satu produk yang terkait dengan satu pengguna.

      Contoh untuk Many-to-many:

      ```python
      buyers = models.ManyToManyField(User, related_name='bought_products')
      ```

   - Kesimpulan:
      - ForeignKey adalah cara paling umum untuk menghubungkan model Product dengan User dalam relasi many-to-one.
      - Field owner pada model Product menyimpan referensi ke pengguna (user) yang memiliki produk tersebut.
      - Kita dapat menggunakan metode seperti filter() untuk meng-query produk-produk yang dimiliki oleh pengguna tertentu, serta menghubungkan produk baru dengan pengguna melalui request.user

   **3. Apa perbedaan antara authentication dan authorization, apakah yang dilakukan saat pengguna login? Jelaskan bagaimana Django mengimplementasikan kedua konsep tersebut.**

   Authentication adalah proses memverifikasi identitas pengguna (misalnya, saat login dengan username dan password). Authorization adalah proses menentukan apa yang boleh dilakukan oleh pengguna setelah login (misalnya, mengakses halaman tertentu atau mengedit data).

   Perbedaan:
   - Authentication: Memastikan siapa pengguna (verifikasi identitas).
   - Authorization: Menentukan apa yang boleh dilakukan oleh pengguna (izin akses).

   Saat pengguna login:
   - Django **mengauntentikasi** pengguna dengan memeriksa username dan password.
   - Setelah berhasil login, Django **mengotorisasi** pengguna untuk mengakses fitur atau halaman berdasarkan izin (permissions) mereka.

   Implementasi di Django:
   
   Authentication:
   - Login: Django menyediakan fungsi authenticate() untuk memverifikasi identitas pengguna.
   - Contoh penggunaan:
     ```python
     from django.contrib.auth import authenticate, login

     def login_view(request):
       username = request.POST['username']
       password = request.POST['password']
       user = authenticate(request, username=username, password=password)
       if user is not None:
           login(request, user)
           # Redirect to a success page
       else:
           # Return an 'invalid login' error message
     ```

   - Middleware: Django menggunakan middleware AuthenticationMiddleware untuk mengaitkan setiap permintaan dengan pengguna yang terautentikasi (request.user).

   Authorization:
   - Django menggunakan permissions dan groups untuk melakukan kontrol akses.
   - @login_required decorator digunakan untuk membatasi akses hanya kepada pengguna yang sudah login.
   - Permissions: Setiap model di Django memiliki add, change, dan delete permissions secara default. Anda juga bisa membuat permission kustom.
   - Contoh:
     ```python
     from django.contrib.auth.decorators import login_required, permission_required

     @login_required
     @permission_required('app_name.change_product')
     def edit_product(request, product_id):
        # Logika untuk mengedit produk
     ```

   **4. Bagaimana Django mengingat pengguna yang telah login? Jelaskan kegunaan lain dari cookies dan apakah semua cookies aman digunakan?**

   Django mengingat pengguna yang telah login menggunakan cookies dan sessions.

   **Cara Django Mengingat Pengguna yang Telah Login:**
   1. Session: Django menyimpan informasi pengguna yang telah login dalam session. Saat pengguna berhasil login, Django membuat session key yang unik dan menyimpannya di database atau dalam cache.
   2. Cookie: Django kemudian menyimpan session key ini di browser pengguna sebagai cookie (biasanya bernama sessionid). Setiap kali pengguna membuat permintaan baru ke server, cookie ini dikirim bersama dengan permintaan tersebut.
   3. Session Key Validasi: Django menggunakan session key untuk mencocokkan data session yang ada di server dan mengetahui siapa pengguna yang sedang login. Dengan cara ini, pengguna tetap "terlogin" selama session masih aktif.

   **Kegunaan Lain dari Cookies:**
   1. Menyimpan Preferensi: Cookies dapat digunakan untuk menyimpan preferensi pengguna, seperti pengaturan bahasa atau tampilan tema situs.
   2. Pelacakan Aktivitas: Cookies bisa digunakan untuk melacak aktivitas pengguna di berbagai halaman, seperti produk yang dilihat atau keranjang belanja di e-commerce.
   3. Autentikasi Otomatis: Cookies dapat menyimpan informasi yang memungkinkan pengguna untuk tetap login tanpa memasukkan kredensial setiap kali membuka situs (misalnya, fungsi "remember me").

   **Apakah Semua Cookies Aman digunakan?**

   Tidak semua cookies aman. Ada beberapa risiko terkait keamanan cookies:
   1. Cookies yang Tidak Terenkripsi (HTTP): Cookies yang dikirim melalui koneksi HTTP tidak terenkripsi, sehingga dapat diintip oleh pihak ketiga yang berbahaya.
   2. Cookies yang Terpapar pada JavaScript (XSS): Jika cookie tidak dilindungi dengan benar, mereka bisa diakses melalui JavaScript, membuatnya rentan terhadap serangan Cross-Site Scripting (XSS).
   3. Serangan Cross-Site Request Forgery (CSRF): Cookies bisa digunakan untuk menyerang pengguna yang tidak curiga, dengan memanfaatkan request yang dikirim tanpa sepengetahuan pengguna.

   **5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).**
</details>

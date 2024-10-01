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

   1. Menambahkan import UserCreationForm dan messages pada views.py
   2. Menambahkan fungsi register didalam views.py seperti berikut :
      ```python
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

   3. Membuat register.html didalam directory main/templates untuk menampilkan halaman register.
   4. Melakukan routing di urls.py dengan mengimport register dan menambahkan path dilist urlpatterns agar terhubung.
   5. Untuk implementasi login kita akan mengimport authenticate, login, dan AuthenticationForm pada bagian paling atas di file views.py.
   6. Tambahkan fungsi login_user yang menerima parameter request didalam views.py seperti berikut:
      ```python
      def login_user(request):
         if request.method == 'POST':
            form = AuthenticationForm(data=request.POST)
      
            if form.is_valid():
                  user = form.get_user()
                  login(request, user)
                  return redirect('main:show_main')
      
         else:
            form = AuthenticationForm(request)
         context = {'form': form}
         return render(request, 'login.html', context)
      ```

   7. Membuat login.html didalam directory main/templates untuk menampilkan halaman login.
   8. Melakukan routing di urls.py dengan mengimport login_user dan menambahkan path dilist urlpatterns agar terhubung.
   9. Untuk implementasi logout kita akan mengimport logout pada bagian paling atas di file views.py.
   10. Tambahkan fungsi logout yang menerima parameter request didalam views.py seperti berikut:
       ```python
       def logout_user(request):
          logout(request)
          return redirect('main:login')
       ```
    
   11. Menambahkan tombol logout didalam file main.html dengan menambahkan kode berikut :
       ```html
         <a href="{% url 'main:logout' %}">
           <button>Logout</button>
         </a>
       ```

   12. Melakukan routing di urls.py dengan mengimport logout dan menambahkan path dilist urlpatterns agar terhubung.
   13. Tambahkan potongan kode @login_required(login_url='/login') di atas fungsi show_main yang berada di views.py agar halaman main hanya dapat diakses oleh pengguna yang sudah login (terautentikasi).
   14. Untuk menerapkan cookies seperti last_login kita akan menambahkan import HttpResponseRedirect, reverse, dan datetime didalam views.py.
   15. Kita akan menambahkan cookies yang bernama last_login didalam fungsi login user di blok if form.is_valid(): dengan menggantinya menjadi seperti ini :
       ```python
       if form.is_valid():
          user = form.get_user()
          login(request, user)
          response = HttpResponseRedirect(reverse("main:show_main"))
          response.set_cookie('last_login', str(datetime.datetime.now()))
          return response
       ```

   16. Didalam dictionary context pada fungsi show_main, kita menambahkan potongan kode 'last_login': request.COOKIES['last_login'] untuk menambahkan informasi last login pada page main.
   17. Untuk menghapus cookies last_login, kita akan mengubah fungsi logout menjadi sebagai berikut:
       ```python
       def logout_user(request):
          logout(request)
          response = HttpResponseRedirect(reverse('main:login'))
          response.delete_cookie('last_login')
          return response
       ```

   18. Tambahkan potongan kode berikut pada main.html untuk menampilkan informasi last login
       ```html
       <h5>Sesi terakhir login: {{ last_login }}</h5>
       ```

   19. Untuk menghubungkan model Product dengan User, kita akan mengimport User pada models.py
   20. Pada model Product kita akan menambahkan potongan kode berikut:
       ```python
       user = models.ForeignKey(User, on_delete=models.CASCADE)
       ```

   21. Pada views.py kita akan mengubah fungsi yang menghandle untuk pembuatan form.
   22. Lalu kita akan mengubah isi variable yang berguna untuk mengambil semua objek pada models pada fungsi show_main menjadi seperti berikut:
       ```python
       Product.objects.filter(user=request.user)
       ```

   23. Lalu kita juga akan menambahkan potongan kode didalam dictionary context seperti berikut:
       ```python
       'name': request.user.username,
       ```

   24. Lakukan migrasi
</details>

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

<details>
   <summary> Tugas 5: Desain Web menggunakan HTML, CSS dan Framework CSS </summary>

   **1. Jika terdapat beberapa CSS selector untuk suatu elemen HTML, jelaskan urutan prioritas pengambilan CSS selector tersebut!**

   1. Inline Style (Prioritas Tertinggi)
      
      Jika sebuah elemen HTML memiliki gaya CSS yang ditentukan langsung di atribut style, maka ini akan memiliki prioritas tertinggi. CSS dari style inline akan selalu menimpa aturan dari selektor eksternal, internal, atau CSS lainnya.

   2. ID Selector
      
      Selektor yang menggunakan atribut id akan memiliki prioritas yang lebih tinggi daripada kelas, tag, atau elemen lainnya.

   3. Class, Pseudo-Class, Attribute Selector
      
      Selektor kelas (.class), pseudo-class (:hover, :active), atau selektor atribut ([type="text"]) memiliki prioritas yang lebih rendah daripada ID, tetapi lebih tinggi daripada elemen.

   4. Type Selector (Tag HTML), Pseudo-Elements

      Selektor elemen HTML seperti div, p, h1, atau pseudo-element seperti ::before dan ::after memiliki prioritas paling rendah.

   5. Universal Selector, Inherited Styles, dan Default Browser Styles (Prioritas Terendah)

      Selektor universal (*), gaya yang diwariskan dari elemen induk, serta gaya bawaan dari browser memiliki prioritas terendah.

   **2. Mengapa responsive design menjadi konsep yang penting dalam pengembangan aplikasi web? Berikan contoh aplikasi yang sudah dan belum menerapkan responsive design!**

   Berikut adalah beberapa alasan mengapa responsive design penting:
   - Meningkatkan Pengalaman Pengguna (User Experience) :
     
     Responsivitas menjamin tampilan yang sesuai pada semua perangkat, sehingga pengguna tidak perlu memperbesar layar atau menggulir secara horizontal. Navigasi yang mudah dan tata letak yang konsisten meningkatkan kepuasan pengguna.
   - SEO dan Peringkat di Mesin Pencari :

     Google dan mesin pencari lainnya memberikan peringkat lebih tinggi untuk situs web yang mobile-friendly. Karena Google menggunakan algoritma yang memprioritaskan indeksasi mobile, memiliki situs yang responsif membantu meningkatkan peringkat di mesin pencari dan memperluas jangkauan audiens.
   - Efisiensi Biaya dan Waktu :

     Dengan responsive design, Anda tidak perlu membuat versi terpisah untuk desktop dan mobile, sehingga lebih hemat waktu dan biaya dalam pengembangan dan pemeliharaan. Desain responsif menghemat sumber daya karena satu kode dapat diterapkan di berbagai perangkat.
   - Peningkatan Konversi dan Penjualan :

     Ketika pengguna mengalami kemudahan saat berinteraksi dengan situs di berbagai perangkat, mereka lebih cenderung untuk kembali, menjelajahi, dan melakukan transaksi, yang pada akhirnya meningkatkan tingkat konversi dan penjualan.
   - Adaptasi terhadap Perangkat Masa Depan :

     Dengan menggunakan konsep responsivitas berbasis viewport dan ukuran layar, situs web lebih siap menghadapi perangkat baru dengan berbagai ukuran layar yang mungkin muncul di masa depan.

      **Contoh Aplikasi yang Sudah Menerapkan Responsive Design**
     - Instagram: Instagram memiliki desain yang responsif baik di aplikasi maupun di versi web-nya. Ketika diakses melalui desktop atau smartphone, tampilan aplikasi menyesuaikan sesuai ukuran layar. Navigasi dan pengalaman pengguna tetap konsisten dan nyaman di semua perangkat.
    
      **Contoh Aplikasi yang Belum Menerapkan Responsive Design**
     - Beberapa Website Institusi Pemerintah: Beberapa situs pemerintah (terutama versi lama atau yang tidak diperbarui secara berkala) masih belum menerapkan desain responsif. Misalnya, situs web yang menampilkan konten statis dalam tata letak yang kaku dan tidak bisa menyesuaikan layar kecil, mengharuskan pengguna memperbesar layar atau menggulir horizontal.
    
   **3.Jelaskan perbedaan antara margin, border, dan padding, serta cara untuk mengimplementasikan ketiga hal tersebut!**

   1. Margin

      - Pengertian : Margin adalah ruang di luar batas (border) elemen. Ini digunakan untuk membuat jarak antara elemen satu dengan elemen lainnya.
      - Fungsi: Margin mempengaruhi jarak di luar elemen, sehingga dua elemen tidak saling berhimpitan.
      - Cara Implementasi: Properti margin dapat diatur dengan nilai spesifik untuk bagian atas, kanan, bawah, dan kiri, atau dapat diatur secara keseluruhan. Contoh untuk mengimplementasikannya sebagai berikut :

      ```css
      div {
        margin-top: 10px;
        margin-right: 15px;
        margin-bottom: 20px;
        margin-left: 25px;
      }
      ```
   2. Border

      - Pengertian: Border adalah garis yang mengelilingi elemen. Border berada di antara padding dan margin, dan bisa diatur ketebalan, gaya, dan warnanya.
      - Fungsi: Border memberikan garis atau bingkai di sekitar elemen, yang bisa digunakan untuk menonjolkan elemen atau membagi konten.
      - Cara Implementasi: Border dapat diatur dengan properti border yang mencakup ukuran, gaya, dan warna, atau secara spesifik untuk setiap sisi. Contoh untuk mengimplementasikannya sebagai berikut :
     
        ```css
        div {
        border-top: 2px solid black;
        border-right: 3px dashed red;
        border-bottom: 4px dotted blue;
        border-left: 5px solid green;
         }
        ```
   3. Padding

      - Pengertian: Padding adalah ruang di dalam elemen, antara konten elemen dan batas (border) elemen. Padding memberikan ruang di dalam elemen, sehingga konten tidak menempel pada border.
      - Fungsi: Padding menambah ruang di dalam elemen untuk memberi jarak antara konten dan border. Ini membantu membuat konten terlihat lebih rapi dan teratur.
      - Cara Implementasi: Padding dapat diatur untuk seluruh elemen, atau secara terpisah untuk atas, kanan, bawah, dan kiri. Contoh untuk mengimplementasikannya sebagai berikut :
     
        ```css
        div {
           padding-top: 10px;
           padding-right: 15px;
           padding-bottom: 20px;
           padding-left: 25px;
         }
        ```
        
   **4. Jelaskan konsep flex box dan grid layout beserta kegunaannya!**
   - Konsep Flex Box:

     Flexbox adalah model layout satu dimensi yang digunakan untuk mengatur tata letak elemen di sepanjang satu sumbu (horizontal atau vertikal). Flexbox memudahkan pengaturan dan distribusi ruang di antara item dalam container yang fleksibel, baik dalam satu baris atau satu kolom. Flexbox sangat cocok digunakan untuk tata letak yang membutuhkan fleksibilitas, terutama dalam hal penyesuaian ukuran elemen berdasarkan ukuran layar dan ruang yang tersedia.

     Kegunaan Flex box:
     - Membuat tata letak navigasi horizontal (navbar) dengan mudah.
     - Menyusun card yang fleksibel dan responsif.
     - Membuat footer yang tetap di bawah dan mendistribusikan item di dalamnya secara merata.
     - Cocok untuk layout sederhana yang hanya membutuhkan baris atau kolom.

   - Konsep Grid Layout:

     Grid Layout adalah model tata letak dua dimensi yang memungkinkan Anda untuk membuat layout berdasarkan baris dan kolom. CSS Grid menawarkan fleksibilitas yang lebih besar dibandingkan Flexbox dalam mengatur elemen di sepanjang dua dimensi (baik horizontal maupun vertikal). Grid sangat cocok untuk membuat layout yang kompleks seperti halaman web yang memiliki beberapa elemen dengan tata letak yang berbeda-beda dalam satu grid.

     Kegunaan Grid Layout:
     - Membuat layout halaman yang kompleks dengan banyak elemen.
     - Menata dashboard dengan beberapa panel atau widget.
     - Membuat layout galeri gambar atau album foto yang tersusun rapi.
     - Cocok untuk desain responsif yang lebih terstruktur dan sistematis, terutama ketika harus mengelola banyak elemen dalam berbagai baris dan kolom.

   **5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!**'
   
1. Menghubungkan CSS dengan menambahkan <script src="https://cdn.tailwindcss.com"> didalam file base.html.

2. Untuk menambah fitur edit product, kita membuat function didalam views.py dan melakukan routingnya di urls.py. Berikut contoh functionnya:

      ```python
         def edit_mood(request, id):
            # Get mood entry berdasarkan id
            mood = MoodEntry.objects.get(pk = id)
         
            # Set mood entry sebagai instance dari form
            form = MoodEntryForm(request.POST or None, instance=mood)
         
            if form.is_valid() and request.method == "POST":
              # Simpan form dan kembali ke halaman awal
              form.save()
              return HttpResponseRedirect(reverse('main:show_main'))
         
            context = {'form': form}
            return render(request, "edit_mood.html", context)
      ```

3. Menambahkan import di views.py yaitu from django.shortcuts import .., reverse da from django.http import .., HttpResponseRedirect
4. Membuat halaman edit product.
5. Melakukan routing di urls.py untuk edit productnya.
6. Menambahkan tombol edit product di main.html.
7. Untuk menambah fitur delete product, kita membuat function didalam views.py dan melakukan routingnya di urls.py. Berikut contoh functionnya:

   ```python
   def delete_mood(request, id):
       # Get mood berdasarkan id
       mood = MoodEntry.objects.get(pk = id)
       # Hapus mood
       mood.delete()
       # Kembali ke halaman awal
       return HttpResponseRedirect(reverse('main:show_main'))
   ```

8. Menambahkan tombol delete product di main.html.
9. Untuk membuat navbar, kita membuat files di root directory didalam templates dengan nama navbar.html.
10. Isi sesuai dengan keinginan kita.
11. Agar navbar muncul dipage yang kita inginkan, tambahkan {% include 'navbar.html' %} dimasing-masing file html yang kita inginkan untuk navbar muncul.
12. Untuk mengelola static files, pada settings.py tambahkan code berikut:

    ```python
    MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware', #Tambahkan tepat di bawah SecurityMiddleware
    ...
    ]
   
    ```

13. Tambahkan code berikut juga:

   ```python
      ...
   STATIC_URL = '/static/'
   if DEBUG:
       STATICFILES_DIRS = [
           BASE_DIR / 'static' # merujuk ke /static root project pada mode development
       ]
   else:
       STATIC_ROOT = BASE_DIR / 'static' # merujuk ke /static root project pada mode production
   ...
   ```

14. Membuat file global.css yang berguna untuk mendesign page anda dengan membuat directory bernama static diroot directory dan didalam directory membuat directory bernama css.
15. Agar CSS dan tailwind dapat terhubung, kita melakukan routing di base.html dengan menambahkan line berikut didalam tag head <script src="https://cdn.tailwindcss.com"></script> dan <link rel="stylesheet" href="{% static 'css/global.css' %}"/>
16. Lakukan styling dihalaman yang anda ingin style, jika anda ingin menambahkan animasi kompleks anda bisa menambahkan styling sendiri di global.css
</details>

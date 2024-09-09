1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
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

2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
   ![Untitled Diagram drawio](https://github.com/user-attachments/assets/9ef27e87-448f-4ce7-821d-78bb94589679)

   1. Pertama, pengguna akan melakukan permintaan HTTP, yang kemudian akan diproses oleh View. Untuk mengetahui apa yang diminta dan apa yang akan diberikan tanggapan, akan menentukan 
      urls.py. Kemudian, berdasarkan pattern url yang diminta, akan menentukan function View yang akan dijalankan di Views.py.
   2. Kedua, Data yang dibutuhkan untuk ditampilkan diminta oleh tampilan; data tersebut sudah tercantum dalam function view yang dijalankan, dan tampilan akan mendapatkan field data           yang tersedia di models.py.
   3. Untuk menentukan berkas HTML yang akan dipopulasikan dengan data pada Template, View akan meminta berkas HTML yang telah ditentukan dalam function View. Setelah mendapatkan berkas 
      HTML yang diminta, kemudian User akan menerima HTML yang telah dipopulasikan dengan data dalam bentuk HTTP.
      
3. Jelaskan fungsi git dalam pengembangan perangkat lunak!
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

4. Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?

   Menurut saya, karena Django adalah salah satu framework yang mudah dipelajari untuk pemula. Django juga menggunakan bahasa python yang merupakan bahasa pemrograman populer dan ramah      untuk pemula. Django memiliki dokumentasi terbaik dibandingkan framework lainnya, bagi pemula yang baru pertama kali belajar framework web, dokumentasi yang bagus bisa menjadi panduan    utama untuk menyelesaikan masalah tanpa kebingungan. Secara keseluruhan, Django adalah pilihan yang ideal bagi pemula karena kesederhanaan, keteraturan, dan dokumentasi yang kuat,        serta fitur-fitur yang langsung siap digunakan.

6. Mengapa model pada Django disebut sebagai ORM?

   Model pada Django disebut sebagai ORM (Object-Relational Mapping) karena model dalam Django berfungsi sebagai jembatan antara objek-objek dalam kode Python dan tabel-tabel dalam basis    data relasional.

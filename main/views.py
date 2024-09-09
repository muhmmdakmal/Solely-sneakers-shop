from django.shortcuts import render

def show_main(request):
    context = {
        'name' : 'Converse Chuck Taylor All Star Vulcanized Hi X Off-White',
        'image_url': 'C:/Users/Lenovo/OneDrive/Desktop/Kuliah/PBP/Solely-sneakers-shop/main/templates/ConverseOW.jpg',
        'price': 'IDR.10,500,000',
        'description': 'Seri ini, yang dirancang oleh Virgil Abloh dari Off-White dan Nike, menggabungkan ketiga brand untuk versi baru yang menarik dari Converse Chuck Taylor klasik. Sepasang sepatu dari seri "Ghosting" ini hadir dalam warna putih, kerucut, dan biru es. Mereka memiliki bahan yang berbeda di seluruh bagian, serta sol tembus pandang biru es, tali pengikat merah, merek hitam, dan bagian atas tembus pandang yang direkonstruksi untuk sesuai dengan temanya. Tersedia bersama dengan koleksi Off-White x Nike "Ghosting" lainnya, akan dirilis pada 1 November 2017.',
        'name_creator':'Muhammad Akmal Abdul Halim',
        'npm_creator':'2306245125',
        'class_creator':'PBP-D'
    }

    return render(request, "main.html", context)
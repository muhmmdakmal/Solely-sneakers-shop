from django.shortcuts import render, redirect
from main.forms import ProductForm
from main.models import Product
from django.http import HttpResponse
from django.core import serializers

def show_main(request):
    products_entries = Product.objects.all()
    context = {
        'name' : 'Converse Chuck Taylor All Star Vulcanized Hi X Off-White',
        'image_url': 'C:/Users/Lenovo/OneDrive/Desktop/Kuliah/PBP/Solely-sneakers-shop/main/templates/ConverseOW.jpg',
        'price': 'IDR.10,500,000',
        'description': 'Seri ini, yang dirancang oleh Virgil Abloh dari Off-White dan Nike, menggabungkan ketiga brand untuk versi baru yang menarik dari Converse Chuck Taylor klasik. Sepasang sepatu dari seri "Ghosting" ini hadir dalam warna putih, kerucut, dan biru es. Mereka memiliki bahan yang berbeda di seluruh bagian, serta sol tembus pandang biru es, tali pengikat merah, merek hitam, dan bagian atas tembus pandang yang direkonstruksi untuk sesuai dengan temanya. Tersedia bersama dengan koleksi Off-White x Nike "Ghosting" lainnya, akan dirilis pada 1 November 2017.',
        'name_creator':'Muhammad Akmal Abdul Halim',
        'npm_creator':'2306245125',
        'class_creator':'PBP-D',
        'products_entries' : products_entries
    }

    return render(request, "main.html", context)

def create_rating(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_rating.html", context)

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
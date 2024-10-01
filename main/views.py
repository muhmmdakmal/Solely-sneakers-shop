from django.shortcuts import render, redirect, reverse, get_object_or_404
from main.forms import ProductForm
from main.models import Product
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseRedirect
from django.urls import reverse
from django.core import serializers
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import datetime

@login_required(login_url='/login')
def show_main(request):
    products_entries = Product.objects.filter(user=request.user)
    context = {
        'name': request.user.username,
        'name_product' : 'Converse Chuck Taylor All Star Vulcanized Hi X Off-White',
        'price': 'IDR.10,500,000',
        'description': 'Seri ini, yang dirancang oleh Virgil Abloh dari Off-White dan Nike, menggabungkan ketiga brand untuk versi baru yang menarik dari Converse Chuck Taylor klasik. Sepasang sepatu dari seri "Ghosting" ini hadir dalam warna putih, kerucut, dan biru es. Mereka memiliki bahan yang berbeda di seluruh bagian, serta sol tembus pandang biru es, tali pengikat merah, merek hitam, dan bagian atas tembus pandang yang direkonstruksi untuk sesuai dengan temanya. Tersedia bersama dengan koleksi Off-White x Nike "Ghosting" lainnya, akan dirilis pada 1 November 2017.',
        'name_creator':'Muhammad Akmal Abdul Halim',
        'npm_creator':'2306245125',
        'class_creator':'PBP-D',
        'products_entries' : products_entries,
        'last_login': request.COOKIES['last_login']
    }

    return render(request, "main.html", context)

def create_product(request):
    form = ProductForm(request.POST, request.FILES)

    if form.is_valid() and request.method == "POST":
        rating_entry = form.save(commit=False)
        rating_entry.user = request.user
        rating_entry.save()
        return redirect('main:show_main')

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

def login_user(request):
   if request.method == 'POST':
      form = AuthenticationForm(data=request.POST)

      if form.is_valid():
        user = form.get_user()
        login(request, user)
        response = HttpResponseRedirect(reverse("main:show_main"))
        response.set_cookie('last_login', str(datetime.datetime.now()))
        return response

   else:
      form = AuthenticationForm(request)
   context = {'form': form}
   return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

def edit_product(request, id):
    # Get rating entry berdasarkan id
    product = get_object_or_404(Product, pk = id)

    # Set product entry sebagai instance dari form
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)

        if form.is_valid() and request.method == "POST":
            # Simpan form dan kembali ke halaman awal
            form.save()
            return HttpResponseRedirect(reverse('main:show_main'))
        
    else:
        form = ProductForm(instance=product)

    context = {'form': form}
    return render(request, "edit_product.html", context)

def delete_product(request, id):
    # Get product berdasarkan id
    product = Product.objects.get(pk = id)
    # Hapus product
    product.delete()
    # Kembali ke halaman awal
    return HttpResponseRedirect(reverse('main:show_main'))
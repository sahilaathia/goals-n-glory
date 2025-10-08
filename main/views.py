import datetime
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.core import serializers
from main.forms import ProductForm
from main.models import Product

@login_required(login_url='/login')
def show_main(request):
    filter_type = request.GET.get("filter", "all")  # default 'all'

    if filter_type == "all":
        product_list = Product.objects.all()
    else:
        product_list = Product.objects.filter(user=request.user)

    context = {
        'app_name' : 'Goals n\' Glory',
        'name': request.user.username,
        'npm' : '2406495716',
        'class': 'PBP B',
        'product_list': product_list,
        'last_login': request.COOKIES.get('last_login', 'Never')
    }

    return render(request, "main.html", context)

def add_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        product_entry = form.save(commit = False)
        product_entry.user = request.user
        product_entry.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "add_product.html", context)

@login_required(login_url='/login')
def show_product(request, id):
    product = get_object_or_404(Product, pk=id)

    context = {
        'product': product
    }

    return render(request, "product_detail.html", context)

def show_xml(request):
    product_list = Product.objects.all()
    xml_data = serializers.serialize("xml", product_list)
    return HttpResponse(xml_data, content_type="application/xml")

from django.http import JsonResponse
from .models import Product

def show_json(request):
    products = Product.objects.all()
    data = [
        {
            'id': str(product.id),
            'name': product.name,
            'price': product.price,
            'description': product.description,
            'thumbnail': product.thumbnail,
            'category': product.category,
            'category_display': product.get_category_display(),
            'is_featured': product.is_featured,
            'brand': product.brand,
            'size': product.size,
            'color': product.color,
            'stock': product.stock,
            'user_id': product.user.id if product.user else None,
        }
        for product in products
    ]
    
    return JsonResponse(data, safe=False)

def show_xml_by_id(request, product_id):
    try:
        product_item = Product.objects.filter(pk=product_id)
        xml_data = serializers.serialize("xml", product_item)
        return HttpResponse(xml_data, content_type="application/xml")
    except Product.DoesNotExist:
        return HttpResponse(status=404)

def show_json_by_id(request, product_id):
    try:
        product = Product.objects.select_related('user').get(pk=product_id)
        data = {
            'id': str(product.id),
            'name': product.name,
            'price': product.price,
            'description': product.description,
            'thumbnail': product.thumbnail,
            'category': product.category,
            'category_display': product.get_category_display(),
            'is_featured': product.is_featured,
            'brand': product.brand,
            'size': product.size,
            'color': product.color,
            'stock': product.stock,
            'user_id': product.user.id if product.user else None,
            'user_username': product.user.username if product.user else 'Anonymous',
        }
        return JsonResponse(data)
    except Product.DoesNotExist:
        return JsonResponse({'detail': 'Not found'}, status=404)
    
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
    product = get_object_or_404(Product, pk=id)
    form = ProductForm(request.POST or None, instance=product)
    if form.is_valid() and request.method == 'POST':
        form.save()
        return redirect('main:show_main')

    context = {
        'form': form,
        'product': product
    }

    return render(request, "edit_product.html", context)

def delete_product(request, id):
    product = get_object_or_404(Product, pk=id)
    product.delete()
    return HttpResponseRedirect(reverse('main:show_main'))

@csrf_exempt
@require_POST
def add_product_ajax(request):
    name = request.POST.get("name")
    brand = request.POST.get("brand")
    price = request.POST.get("price")
    stock = request.POST.get("stock")
    size = request.POST.get("size")
    color = request.POST.get("color")
    category = request.POST.get("category")
    thumbnail = request.POST.get("thumbnail")
    is_featured = request.POST.get("is_featured") == 'on'
    user = request.user

    new_product = Product(
        name=name,
        brand=brand,
        price=price,
        stock=stock,
        size=size,
        color=color,
        category=category,
        thumbnail=thumbnail,
        is_featured=is_featured,
        user=user
    )
    new_product.save()
    return HttpResponse(b"CREATED", status=201)

@csrf_exempt
def edit_product_ajax(request, id):
    if request.method == 'POST':
        product = get_object_or_404(Product, pk=id)
        form = ProductForm(request.POST, instance=product)

        if form.is_valid():
            form.save()
            return JsonResponse({"status": "success", "message": "Product updated successfully!"})
        else:
            return JsonResponse({"status": "error", "errors": form.errors}, status=400)
    return JsonResponse({"status": "error", "message": "Invalid request method."}, status=405)

@csrf_exempt
def delete_product_ajax(request, id):
    if request.method == 'POST':
        try:
            product = Product.objects.get(pk=id)
            if product.user == request.user:
                product.delete()
                return JsonResponse({"status": "success", "message": "Product deleted successfully."})
            else:
                return JsonResponse({"status": "error", "message": "You are not authorized to delete this product."}, status=403)
        except Product.DoesNotExist:
            return JsonResponse({"status": "error", "message": "Product not found."}, status=404)
    return JsonResponse({"status": "error", "message": "Invalid request method."}, status=405)

@csrf_exempt
def register_ajax(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({
                "status": "success",
                "message": "Account created successfully! You can now log in.",
                "redirect_url": reverse("main:login")
            })
        else:
            errors = {field: error[0] for field, error in form.errors.items()}
            return JsonResponse({
                "status": "error",
                "message": "Please correct the errors below.",
                "errors": errors
            }, status=400)
    return JsonResponse({"status": "error", "message": "Invalid request method."}, status=405)

@csrf_exempt
def login_ajax(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                response_data = {
                    "status": "success",
                    "message": "Login successful!",
                    "redirect_url": reverse("main:show_main")
                }
                response = JsonResponse(response_data)
                response.set_cookie('last_login', str(datetime.datetime.now()))
                return response
        
        return JsonResponse({
            "status": "error",
            "message": "Invalid username or password. Please try again."
        }, status=400)

    return JsonResponse({"status": "error", "message": "Invalid request method."}, status=405)

@csrf_exempt
def logout_ajax(request):
    if request.method == 'POST':
        logout(request)
        response_data = {
            "status": "success",
            "message": "You have been logged out successfully!",
            "redirect_url": reverse("main:login")  # Redirect to login page
        }

        response = JsonResponse(response_data)
        response.delete_cookie('last_login')

        return response
    return JsonResponse({"status": "error", "message": "Invalid request method."}, status=405)

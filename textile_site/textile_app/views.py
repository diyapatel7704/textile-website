from django.shortcuts import render, redirect, get_object_or_404
from django.core.mail import send_mail
from django.contrib import messages
from .models import (
    Product,
    Enquiry,
    Business,
    Infrastructure,
    WhyChooseUs,
    Testimonial
)
import urllib.parse


def home(request):

    business = Business.objects.first()

    products = Product.objects.all()[:4]

    why_choose = WhyChooseUs.objects.all()

    testimonials = Testimonial.objects.all()[:3]

    return render(request, 'textile_app/home.html', {
        'business': business,
        'products': products,
        'why_choose': why_choose,
        'testimonials': testimonials
    })


def products(request):

    products = Product.objects.all()

    # SEARCH
    search = request.GET.get('search')

    if search:
        products = products.filter(name__icontains=search)

    # CATEGORY FILTER
    category = request.GET.get('category')

    if category:
        products = products.filter(category__icontains=category)

    # UNIQUE CATEGORY LIST
    categories = Product.objects.values_list(
        'category',
        flat=True
    ).distinct()

    return render(request, 'textile_app/products.html', {
        'products': products,
        'categories': categories
    })


def product_detail(request, id):

    product = get_object_or_404(Product, id=id)

    if request.method == "POST":

        name = request.POST.get('name')
        phone = request.POST.get('phone')
        quantity = request.POST.get('quantity') or "Not specified"
        message = request.POST.get('message') or "No message"

        Enquiry.objects.create(
            name=name,
            phone=phone,
            product=product.name,
            quantity=quantity,
            message=message
        )

        try:
            send_mail(
                "New Enquiry",
                f"Name: {name}\nPhone: {phone}\nProduct: {product.name}\nQuantity: {quantity}\nMessage: {message}",
                "diyup2004@gmail.com",
                ["diyup2004@gmail.com"],
                fail_silently=True
            )

        except:
            pass

        messages.success(request, "Enquiry submitted successfully!")

        text = f"Hello, I am {name}. I want {product.name}. Quantity: {quantity}."

        encoded = urllib.parse.quote(text)

        whatsapp_url = f"https://wa.me/917990753825?text={encoded}"

        return redirect(whatsapp_url)

    return render(request, 'textile_app/product_detail.html', {
        'product': product
    })


def about(request):

    infra = Infrastructure.objects.first()

    why_choose = WhyChooseUs.objects.all()

    testimonials = Testimonial.objects.all()[:3]

    return render(request, 'textile_app/about.html', {
        'infra': infra,
        'why_choose': why_choose,
        'testimonials': testimonials
    })


def contact(request):

    if request.method == "POST":

        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        Enquiry.objects.create(
            name=name,
            phone=phone,
            product="General Inquiry",
            quantity="N/A",
            message=message
        )

    return render(request, 'textile_app/contact.html')
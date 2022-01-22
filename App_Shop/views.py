from django.shortcuts import render

# Import views

from django.views.generic import ListView, DetailView

# Models

from App_Shop.models import Product, Category

#Mixin
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class Home(ListView):
    model = Product
    template_name = 'App_Shop/home.html'

class ProductDetail(DetailView):
    model = Product
    template_name = "App_Shop/product_detail.html"

def searchbar(request):
    if request.method == 'GET':
        search = request.GET.get('search')
        post = Product.objects.all().filter(name=search)
        return render(request, 'searchbar.html',{'post':post})


categories  = Category.objects.all()
contex = {
    'categories':categories
}

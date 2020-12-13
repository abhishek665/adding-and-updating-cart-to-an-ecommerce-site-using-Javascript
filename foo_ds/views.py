from django.shortcuts import render
from .models import Items
# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
import json
import ast
from django.contrib.auth import logout, login, authenticate


def home(request):
    item = Items.objects.all()
    items = list(item.values())
    breakfast = list(Items.objects.filter(catname="breakfast").values())
    lunch = list(Items.objects.filter(catname="lunch").values())
    dinner = list(Items.objects.filter(catname="dinner").values())
    desert = list(Items.objects.filter(catname="desert").values())
    return render(request, 'home.html', {'items': items, 'breakfast':breakfast, 'lunch': lunch, 'dinner':dinner, 'desert': desert})


def nicotine_zone(request, cat):
    request.user.is_authenticated()
    return render(request, 'autoaddress.html')


def checkout(request):
    c = request.POST.get('back_cart')
    check_price = int(request.POST.get('total_price'))
    cart = ast.literal_eval(c)
    total = 0
    for i in cart:
        sid = i[0]
        item = list(Items.objects.filter(sid=sid).values())[0]
        print(item)
        price = int(item['price'])
        qty = int(i[1])
        total += price * qty
        print(total)
    print(cart, check_price, total)
    if check_price != total:
        return HttpResponse("You Fraud ")
    return HttpResponse("order Received Successfully")

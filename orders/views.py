from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
import datetime
import operator
import json
from django import forms
from .models import * 
from django.http import Http404
from datetime import datetime
import re

# Create your views here.
def index(request):
	regular = Regular.objects.all()
	sicilian = Sicilian.objects.all()
	toppings = Toppings.objects.all()
	subs = Subs.objects.all()
	pasta = Pasta.objects.all()
	salads = Salads.objects.all()
	dinner = Dinner.objects.all()
	return render(request, "orders/index.html", {
		"regular": regular,
		"sicilian": sicilian,
		"toppings": toppings,
		"subs": subs,
		"pasta": pasta,
		"salads": salads,
		"dinner": dinner
		})

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "orders/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "orders/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        run(username)
        run(email)
        run(password)
        # Ensure password matches confirmation
        if password != confirmation:
            return render(request, "orders/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "orders/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "orders/register.html")

def cart(request):
    user = User.objects.get(username = request.user)
    orders = list(Order.objects.filter(username=user))
    if user.add1:
        address = True
    else:
        address=False

    return render(request, "orders/cart.html",{
        "orders":orders,
        "address": address,
        "user": user
        })

def addtocart(request, username, cat, item, item1, quantity1, item2, quantity2):
    user = User.objects.get(username = username)
    p1 = float(0)
    p2 = float(0)
    if user:
        orders = Order()
        orders.username = user
        orders.item = item
        orders.confirmed == "no"
        if cat == "rpizza":
            rpizza= Regular.objects.get(r_name=item)
            if item1 == "small":
                p1 = float(rpizza.r_small)
                orders.item1 = item1
            if item2 == "large":
                p2 = float(rpizza.r_large)
                orders.item2 = item2
        elif cat == "spizza":
            spizza = Sicilian.objects.get(s_name=item)
            if item1 == "small":
                p1 = float(spizza.s_small)
                orders.item1 = item1
            if item2 == "large":
                p2 = float(spizza.s_large)
                orders.item2 = item2
        elif cat == "subs":
            subs = Subs.objects.get(sub_name=item)
            if item1 == "small":
                p1 = float(subs.sub_small)
                orders.item1=item1
            if item2 == "large":
                p2 = float(subs.sub_large)
                orders.item2=item2
        elif cat == "pasta":
            if(item1 == "empty")&(item2 =="empty"):
                orders.item = "pasta"
                orders.item1 = item
                pasta = Pasta.objects.get(p_name=item)
                p1= float(pasta.price)
        elif cat == "salad":
            if(item1 == "empty")&(item2 =="empty"):
                orders.item = "salad"
                orders.item1 = item
                salads = Salads.objects.get(salad=item)
                p1= float(salads.price)
        elif cat == "dinner":
            dinner = Dinner.objects.get(d_name=item)
            if item1 == "small":
                p1 = float(dinner.d_small)
                orders.item1=item1
            if item2 == "large":
                p2 = float(dinner.d_large)
                orders.item2=item2
        elif cat == "toppings":
            if(item1 == "empty")&(item2 =="empty"):
                orders.item = "toppings"
                orders.item1 = item
        if quantity1 != 0:
            orders.quantity1 =int(quantity1)
            p1 = p1 * float(quantity1)
        if quantity2 != 0:
            orders.quantity2 = int(quantity2)
            p2 = p2 * float(quantity2)
        price = float(p1 + p2)
        orders.price= float(price)
        orders.save()
    else:
        raise Http404("User Not Found")
    return HttpResponse("Added to Cart!")

def add_address(request, method="POST"):
    user = User.objects.get(username=request.user)
    user.add1 = request.POST["add1"]
    user.add2 = request.POST["add2"]
    user.city = request.POST["city"]
    user.state = request.POST["state"]
    user.zipcode = request.POST["zip"]
    user.contact = request.POST["contact"]
    user.save()
    return HttpResponseRedirect(reverse("cart"),{
        "address": True,
        "add": user
        })

def your_orders(request, confirmed):
    now = datetime.now()
    user = User.objects.get(username=request.user)
    orders = list(Order.objects.filter(username=user))
    if confirmed == "yes":
        for i in range(0,len(orders)):
            orders[i].confirmed = "yes"
    if(len(orders)!=0):
        for i in range(0,len(orders)):
            if orders[i].confirmed == "yes":
                c = ConfirmedOrders()
                c.username = user
                c.item = orders[i].item
                c.item1 = orders[i].item1
                c.item2 = orders[i].item2
                c.quantity1= orders[i].quantity1
                c.quantity2 = orders[i].quantity2
                c.price = orders[i].price
                c.date = now.strftime("%Y-%m-%d")
                c.time = now.strftime("%H:%M")
                c.save()
                orders[i].delete()
    return render(request, "orders/confirmed_orders.html", {
        "orders": ConfirmedOrders.objects.all(),
        "username": user
        })

def cancelorder(request, orderid, cart):
    user = User.objects.get(username=request.user)
    if user:
        if cart == "no":
            c = ConfirmedOrders.objects.get(id=orderid)
            c.delete()
        else:
            o = Order.objects.get(id=orderid)
            o.delete()
    else:
        raise Http404("User not Found")
    return HttpResponse("Order Removed!")

def change_add(request):
    user = User.objects.filter(username=request.user)
    user.update(add1=None)
    user.update(add2=None)
    user.update(city=None)
    user.update(state=None)
    user.update(zipcode=None)
    user.update(contact=None)
    return HttpResponseRedirect(reverse("cart"))

def run(string): 
  
    # Make own character set and pass  
    # this as argument in compile method 
    regex = re.compile('[\[\]\}\{_!#$%^&*()<>?/\|}{~:]') 
      
    # Pass the string in search  
    # method of regex object.     
    if(regex.search(string) == None):
        if(re.search("\s", string)):
            raise Http404("Space is not allowed, Invalid "+ string)
        print("String is accepted") 
          
    else: 
        raise Http404("Special Characters are not allowed, Invalid "+ string)
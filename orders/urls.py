from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("register", views.register, name="register"),
    path("logout", views.logout_view, name="logout"),
    path("cart", views.cart, name="cart"),
    path("addtocart/<str:username>/<str:cat>/<str:item>/<str:item1>/<int:quantity1>/<str:item2>/<int:quantity2>", views.addtocart, name="addtocart"),
    path("add_address", views.add_address, name="add_address"),
    path("your_orders/<str:confirmed>", views.your_orders, name="your_orders"),
    path("cancelorder/<int:orderid>/<str:cart>", views.cancelorder, name="cancelorder"),
    path("change_add", views.change_add, name="change_add")
]

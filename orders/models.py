from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class User(AbstractUser):
	add1 = models.TextField(blank=True, null=True)
	add2 = models.TextField(blank=True, null=True)
	city = models.CharField(max_length=100, blank=True, null=True)
	state = models.CharField(max_length=100,blank=True, null=True)
	zipcode = models.IntegerField(blank=True, null=True)
	contact = models.IntegerField(blank=True, null=True)

class Regular(models.Model):
	r_name = models.CharField(max_length = 100)
	r_small = models.FloatField()
	r_large = models.FloatField()
	r_image = models.ImageField(default='default.jpg', blank=True)
	def __str__(self):
		return f"{self.r_name}: {self.r_small}, {self.r_large}"
		
class Sicilian(models.Model):
	s_name = models.CharField(max_length = 100)
	s_small = models.FloatField()
	s_large = models.FloatField()
	s_image = models.ImageField(default='default.jpg', blank=True)
	def __str__(self):
		return f"{self.s_name}: {self.s_small}, {self.s_large}"

class Toppings(models.Model):
	t_name = models.CharField(max_length = 100)
	def __str__(self):
		return f"{self.t_name}"

class Subs(models.Model):
	sub_name = models.CharField(max_length = 100)
	sub_small = models.FloatField()
	sub_large = models.FloatField()
	sub_image = models.ImageField(default='default.jpg', blank=True)
	def __str__(self):
		return f"{self.sub_name}: {self.sub_small}, {self.sub_large}"

class Pasta(models.Model):
	p_name = models.CharField(max_length = 100)
	price = models.FloatField()
	p_image = models.ImageField(default='default.jpg', blank=True)
	def __str__(self):
		return f"{self.p_name}: {self.price}"

class Salads(models.Model):
	salad = models.CharField(max_length = 100)
	price = models.FloatField()
	salad_image = models.ImageField(default='default.jpg', blank=True)
	def __str__(self):
		return f"{self.salad}: {self.price}"
		
class Dinner(models.Model):
	d_name = models.CharField(max_length = 100)
	d_small = models.FloatField()
	d_large = models.FloatField()
	d_image = models.ImageField(default='default.jpg', blank=True)
	def __str__(self):
		return f"{self.d_name}: {self.d_small}, {self.d_large}"

class Order(models.Model):
	username = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
	item = models.CharField(max_length=100, blank=True, null=True)
	item1 = models.CharField(max_length=100, blank=True, null=True)
	item2 = models.CharField(max_length=100, blank=True, null=True)
	quantity1 = models.IntegerField(null=True, blank=True)
	quantity2 = models.IntegerField(null=True, blank=True)
	price = models.FloatField(blank=True, null=True)
	confirmed = models.CharField(max_length=100, blank=True, null=True)

	def __str__(self):
		return f"[{self.item} {self.item1} X {self.quantity1} + {self.item2} x {self.quantity2} : {self.price}]"

DELIVERY_STATUS = (
	("Your food is getting ready", "1"),
	("Out for Delivery", "2"),
	("Delivered", "3"),
	("Invalid Order", "4")
)
class ConfirmedOrders(models.Model):
	username = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
	status = models.CharField(
		max_length=100, 
		choices = DELIVERY_STATUS,
		default = "Your food is getting ready"
		)
	item = models.CharField(max_length=100, blank=True, null=True)
	item1 = models.CharField(max_length=100, blank=True, null=True)
	item2 = models.CharField(max_length=100, blank=True, null=True)
	quantity1 = models.IntegerField(null=True, blank=True)
	quantity2 = models.IntegerField(null=True, blank=True)
	price = models.FloatField(blank=True, null=True)
	date = models.CharField(max_length=100, null=True)
	time = models.CharField(max_length=100, null=True)
	def __str__(self):
		return f"[{self.username}: {self.item}]"
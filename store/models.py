from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.
class Categories(models.Model):
	title = models.CharField(max_length=150)
	image =image = models.ImageField(default='default-product.jpg', upload_to='Uploads')

	def __str__(self):
		return self.title

class Product(models.Model):
	category = models.ForeignKey(Categories, 
		on_delete=models.CASCADE, related_name='Products')
	name=models.CharField(max_length=250)
	origin_place = models.CharField(max_length=250)

	def __str__(self):
		return f'{self.name}'

class Product_Item(models.Model):
	Product=models.ForeignKey(Product, 
		on_delete=models.CASCADE,related_name='items')

	price=models.FloatField(default = 0.00, blank=False,
								help_text=("""Price per item"""),
                            	verbose_name=('Price'),
                            	validators=[ MinValueValidator(0)])
	discount = models.FloatField(default = 0, blank=False,
								help_text=("Discount offer"),
                            	verbose_name=('Discount'),
                            	validators=[MinValueValidator(0)])
	weight = models.CharField(max_length=20, blank=False)

	about=models.TextField(blank=True, null=True,help_text=("Describe the product."),
                            	verbose_name=('About The Item'),) #Richtextfield if wants to include pictures
	howtouse=models.TextField(blank=True, null=True,help_text=("Write how to consume/use the item."),
                            	verbose_name=('How to use'),) #Richtextfield if wants to include pictures
	benefits=models.TextField(blank=True, null=True,help_text=("Write how will the product benefit them."),
                            	verbose_name=('Benefits'),) #Richtextfield if wants to include pictures
	ingredient=models.TextField(blank=True, null=True,help_text=("Write the things that are included in the pakaging."),
                            	verbose_name=('Ingredients'),) #Richtextfield if wants to include pictures
	
	def __str__(self):
		return f'{self.Product.name}-{self.weight}'
class Product_Item_Images(models.Model):
	item = models.ForeignKey(Product_Item, 
		on_delete=models.CASCADE, related_name='images')
	image = models.ImageField(default='default-product.jpg', upload_to='Uploads')

class Customer(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
	name = models.CharField(max_length=200, null=True)
	email = models.CharField(max_length=200, null=True)
	phone_number = models.CharField(max_length=10)

	def  __str__(self):
		return self.name

class Order(models.Model):
	customer = models.ForeignKey(Customer, 
		on_delete=models.SET_NULL,
		 blank=True, null=True)
	date_orderd = models.DateTimeField(auto_now_add=True)
	complete = models.BooleanField(default=False, null=True, blank=False)
	transaction_id = models.CharField(max_length=200, null=True)

	def __str__(self):
		return f'{self.customer.name}-{self.id}'

	@property
	def get_cart_total(self):
		orderitems = self.orderitem_set.all()
		total =sum([item.get_total for item in orderitems])
		return total

	@property
	def get_cart_items(self):
		orderitems = self.orderitem_set.all()
		total =sum([item.quantity for item in orderitems])
		return total

class OrderItem(models.Model):
	product=models.ForeignKey(Product_Item, on_delete=models.SET_NULL, null=True)
	order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
	quantity = models.IntegerField(default=0, null=True, 
				blank=True, validators=[ MinValueValidator(0)] )
	date_added = models.DateTimeField(auto_now_add=True)

	def  __str__(self):
		return self.product.__str__()

	@property
	def get_total(self):
		total=self.product.price * self.quantity
		return total
	

class ShippingAddress(models.Model):
	customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
	order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
	address = models.CharField(max_length=200, null=False)
	city = models.CharField(max_length=200, null=False)
	state = models.CharField(max_length=200, null=False)
	zipcode = models.CharField(max_length=200, null=False)
	date_added = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.customer.name
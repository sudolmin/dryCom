from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator, MinLengthValidator, MaxLengthValidator
# Create your models here.
class Categories(models.Model):
	title = models.CharField(max_length=150)
	image = models.ImageField(default='default-product.jpg', upload_to='Uploads')

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

	price=models.DecimalField(max_digits=9, decimal_places=2,
								default = 0.00, blank=False,
								help_text=("""Price per item"""),
                            	verbose_name=('Price'),
                            	validators=[ MinValueValidator(0)])
	discount = models.DecimalField(max_digits=9, decimal_places=2,
								default = 0, blank=False,
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

class User(AbstractUser):
	email = models.EmailField(unique=True)

class Customer(User):
	phone_number = models.CharField(max_length=10)

	class Meta:
		verbose_name = 'Customer'
		verbose_name_plural = 'Customers'

	def  __str__(self):
		return f'{self.first_name} {self.last_name}'

class Order(models.Model):
	customer = models.ForeignKey(Customer, 
		on_delete=models.SET_NULL,
		 blank=True, null=True)
	date_orderd = models.DateTimeField(auto_now_add=True)
	complete = models.BooleanField(default=False, null=True, blank=False)
	reciept_id = models.CharField(max_length=20, null=True)

	def __str__(self):
		return f'{self.customer.first_name}-{self.id}-{self.reciept_id}'

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
	pincode = models.CharField(max_length=200, null=False)
	date_added = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.customer.first_name


class PaymentDetail(models.Model):
	order = models.OneToOneField(Order, on_delete=models.SET_NULL, null=True)
	name = models.CharField(max_length=50)
	contact_no = models.CharField(max_length=10)
	email = models.EmailField()
	address = models.TextField(null=False)
	city = models.CharField(max_length=50, null=False)
	state = models.CharField(max_length=30, null=False)
	pincode = models.CharField(max_length=6, null=False)
	date_added = models.DateTimeField(auto_now_add=True)
	payondelivery = models.BooleanField(default=False)
	status = models.CharField(max_length=20, default='None')
	razpayorder_id = models.CharField(max_length=50, default='None')
	paymentID = models.CharField(max_length=50, default='Unpaid')
	canceled = models.BooleanField(default=False)

	@property
	def shippingDict(self):
		self._shippingDict={}
		self._shippingDict['Customer Name']=self.name
		self._shippingDict['Email']=self.email
		self._shippingDict['Contact No.']=self.contact_no
		self._shippingDict['Amount']=float(self.order.get_cart_total)
		self._shippingDict['Shipping address']=f'Address-{self.address}, City-{self.city}, State-{self.state}, Pincode-{self.pincode}'
		return self._shippingDict
	
	def __str__(self):
		return self.name




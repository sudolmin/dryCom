from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.
class Categories(models.Model):
	title = models.CharField(max_length=150)

	def __str__(self):
		return self.title

class Product(models.Model):
	category = models.ForeignKey(Categories, on_delete=models.CASCADE)
	name=models.CharField(max_length=250)
	origin_place = models.CharField(max_length=250)

class Product_Item(models.Model):
	Product=models.ForeignKey(Product, on_delete=models.CASCADE)
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
	
class Product_Item_Images(models.Model):
	item = models.ForeignKey(Product_Item, on_delete=models.CASCADE)
	image = models.ImageField(default='default-product.jpg', upload_to='ProfilePics')
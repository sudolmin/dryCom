from django.db import models
from store.models import User
from PIL import Image
class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	image = models.ImageField(default='default.png', upload_to='profile_pics')

	def __str__(self):
		return f'{self.user.username} Profile'

	def save(self, *args, **kwargs):
		super(Profile, self).save( *args, **kwargs)

		img =Image.open(self.image.path)

		if img.height > 300 or img.width > 300:
			output_size = (300, 300)
			# img.thumbnail(output_size)
			im_new = self.crop_max_square(img)
			im_new.save(self.image.path, quality=80)

	def crop_max_square(self, pil_img):
		return self.crop_center(pil_img, min(pil_img.size), min(pil_img.size))

	def crop_center(self, pil_img, crop_width, crop_height):
	    img_width, img_height = pil_img.size
	    return pil_img.crop(((img_width - crop_width) // 2,
                         (img_height - crop_height) // 2,
                         (img_width + crop_width) // 2,
                         (img_height + crop_height) // 2))
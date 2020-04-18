from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Model to vinculate a profile with a User
class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	image = models.ImageField(default='default.jpg', upload_to='profile_pics')

	def __str__(self):
		return f'{self.user.username} Profile'

# When save method in django is overrided use *args, **kwargs
	def save(self, *args, **kwargs):
		super().save(*args, **kwargs)
		# Open image path
		img = Image.open(self.image.path)

		if img.height > 300 or img.width > 300:
			output_size = (300, 300)
			img.thumbnail(output_size)			# Resize image
			img.save(self.image.path)
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile

# Module to automatically create the user profile when does the registration
# ---------------------------------------------------------------------------
# signal --> post_save
# sender --> User
# When a user is saved then send 'post_save' signal and this signal is going
# to be received by '@receiver' and this receiver is gonna create the profile
# function 'create_profile' whitch will take all the arguments that the post_save
# signal pass to it.
# The function is saying that when a user is created, create a profile object
# with the user iqual to the instance of the user that was created.

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
	if created:
		Profile.objects.create(user=instance)

# Function that save the instance profile
@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
	instance.profile.save()
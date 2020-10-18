from django.db.models.signals import post_save
from django.dispatch import receiver
from store.models import Customer
from .models import Profile

@receiver(post_save, sender=Customer)
def create_profile(sender, instance, created, **kwargs):
    if created:
    	Profile.objects.create(user=instance)

@receiver(post_save, sender=Customer)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()

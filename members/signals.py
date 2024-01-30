from .models import Profile
from django.db.models.signals import post_delete, pre_delete
from django.dispatch import receiver
from django.contrib.auth.models import User


@receiver(pre_delete, sender=User)
def delete_post(sender, instance, **kwargs):
    if Profile.objects.filter(user=instance).exists():
        profile = Profile.objects.get(user=instance)
        profile.delete()
        print(f'Profile {profile.id} deleted from DB with image {profile.image}')

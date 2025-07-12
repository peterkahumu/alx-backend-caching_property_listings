from django.core.cache import cache
from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver

from .models import Property


@receiver(post_save, sender=Property)
def clear_cache_on_save(sender, instance, **kwargs):
    cache.delete('all_properties')


@receiver(post_delete, sender=Property)
def clear_cache_on_delete(sender, instance, **kwargs):
    cache.delete('all_properties')

from django.db import models
from django.dispatch import receiver
from django.db.models.signals import pre_save
from django.contrib.auth.models import User

class Url(models.Model):
    url_name = models.CharField(verbose_name='URL', max_length = 100, db_index = True, unique = True)
    url_status = models.CharField(verbose_name='URL_status', max_length = 20, null=True)
    url_checker = models.BooleanField(default=True)
    def __str__(self):
        return self.url_name

@receiver(pre_save, sender=User)
def update_username_from_email(sender, instance, **kwargs):
    user_email = instance.email
    username = user_email[:30]
    n = 1
    while User.objects.exclude(pk=instance.pk).filter(username=username).exists():
        n += 1
        username = user_email[:(29 - len(str(n)))] + '-' + str(n)
    instance.username = username

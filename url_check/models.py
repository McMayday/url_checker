from django.db import models


class Url(models.Model):
    url_name = models.CharField(verbose_name='URL', max_length = 100, db_index = True, unique = True)
    url_status = models.CharField(verbose_name='URL_status', max_length = 20, null=True)
    url_checker = models.BooleanField(default=True)
    def __str__(self):
        return self.url_name

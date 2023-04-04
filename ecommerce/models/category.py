from django.conf import settings
from django.db import models
from django.contrib import admin


class Category(models.Model):
    name = models.CharField(max_length=63)
    desc = models.TextField(blank=True, verbose_name="description")
    img = models.ImageField(blank=True, upload_to="categories")

    def __str__(self) -> str:
        return self.name
    
    @property
    def absolute_image_url(self):
        return "{0}{1}".format(settings.MEDIA_URL, self.img)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'desc')
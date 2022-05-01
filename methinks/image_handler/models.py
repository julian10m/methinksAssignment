from django.db import models
from django.urls import reverse
import os 

class Image(models.Model):
    image = models.ImageField(upload_to='images/%Y/%m/%d/')
    created = models.DateTimeField(auto_now_add=True)

    @property
    def filename(self):
        return os.path.basename(self.image.name)

    def get_absolute_url(self):
        return reverse('imageHandler:image_detail',
                        args = [self.pk])

    class Meta:
        ordering = ('-created',)

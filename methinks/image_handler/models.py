from django.db import models
import os 

class Image(models.Model):
    image = models.ImageField(upload_to='images/%Y/%m/%d/')
    created = models.DateTimeField(auto_now_add=True)

    @property
    def filename(self):
        return os.path.basename(self.image.name)
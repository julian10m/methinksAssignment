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

    def __str__(self):
        return f'{self.filename}'

class Comment(models.Model):
    image = models.ForeignKey(Image, 
                             on_delete=models.CASCADE,
                             related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('created',)
    
    def __str__(self):
        return f'Comment by {self.name} on {self.image}'

from django.db import models

from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User 




# Create your models here.
class Core(models.Model):

    title = models.CharField(max_length=200)
    excpert = models.TextField(null=True) 
    author = models.ForeignKey(User , on_delete=models.CASCADE)
    slug = models.SlugField(max_length=200 , unique=True)
    image = models.ImageField(upload_to ='uploads/')
    updated = models.DateTimeField(auto_now=True)
    puplished = models.DateTimeField(default=timezone.now)



    def get_absolute_url(self):
        return reverse("core:singleview", args=[self.slug] )
    
    class Meta:

        ordering = ['-puplished']
        verbose_name_plural = 'Core'


    def __str__(self):

        return self.title     
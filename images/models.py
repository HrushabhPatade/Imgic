from django.db import models

class Image(models.Model):
    text = models.CharField(max_length=300)
    generated_image= models.ImageField(upload_to='images')
    
    def __str__(self):
        return str(self.text)

# Create your models here.

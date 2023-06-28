from django.contrib import admin
from images.models import Image

class ImageAdmin(admin.ModelAdmin):
    list_display=('text', 'generated_image')
    
admin.site.register(Image, ImageAdmin)



# Register your models here.

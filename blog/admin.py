from django.contrib import admin

# Register your models here.
from .models import  Category,Author

admin.site.register(Category)
admin.site.register(Author)
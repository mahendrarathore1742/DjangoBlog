from django.contrib import admin

# Register your models here.
from .models import  PostData




class Postadmin(admin.ModelAdmin):
	class Media:
		js=('custom.js',)


admin.site.register(PostData, Postadmin)
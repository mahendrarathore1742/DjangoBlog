from django.db import models

# Create your models here.
 


class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=50,null=True,blank=True)

    def __str__(self):
        return self.name;



class Author(models.Model):
	author = models.CharField(max_length=200)
	slug = models.SlugField(max_length=50,null=True,blank=True);
	def __str__(self):
		return self.author;



    






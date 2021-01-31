from django.db import models
from blog.models  import Category,Author
from django.db.models.signals import pre_save
from django.utils.text import slugify

class PostData(models.Model):
	Title=models.CharField(max_length=100,blank=False,null=False)
	slug = models.SlugField(unique=True,editable=False)
	cover_image=models.ImageField(upload_to='documents/',default='')
	Content= models.TextField()
	Category=models.ForeignKey(Category, on_delete=models.CASCADE)
	author = models.ForeignKey(Author, on_delete=models.CASCADE)
	published_date = models.DateTimeField(auto_now_add=True)
	published = models.BooleanField(default=True)

	def __str__(self):
		return str(self.Category);

	def get_absolute_url(self):
		return reverse("posts:detail",kwargs={'slug':self.slug});

def create_slug(instance,new_slug=None):
	slug=slugify(instance.Title);
	if new_slug is not None:
		slug=new_slug;
	qs=PostData.objects.filter(slug=slug).order_by('-id');
	exists=qs.exists();
	if exists:
		new_slug=f"{slug}-{qs.first().id}";
		return create_slug(instance,new_slug=new_slug);
	return slug;
	
def pre_save_receiver(sender,instance,*args,**kwars):
	if not instance.slug:
		instance.slug=create_slug(instance);
pre_save.connect(pre_save_receiver,sender=PostData);




	


 



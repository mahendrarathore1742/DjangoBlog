from django import forms;
from .models import PostData;



class Datapost(forms.ModelForm):
	class Meta:
		model=PostData;
		fields='__all__'
 
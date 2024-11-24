from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    category = forms.ModelMultipleChoiceField(
        queryset=Post._meta.get_field('category').related_model.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        label="Categories"
    )
    
    class Meta:
        model = Post
        fields = '__all__'
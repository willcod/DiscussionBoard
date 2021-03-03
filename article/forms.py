from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['content']
        labels = {'content': 'Content:'}
        widgets = {'content': forms.Textarea(attrs={'cols': 80})}
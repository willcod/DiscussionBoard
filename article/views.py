from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import ArticleForm
from .models import Article

# Create your views here.
def index(request):
    articles = Article.objects.order_by('created_time')
    return render(request, 'index.html', {'articles':articles})

def new_article(request):

    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = ArticleForm()
    else:
        # POST data submitted; process data.
        form = ArticleForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.authors = User.objects.first()
            new_entry.save()
            return redirect('article:index')

    # Display a blank or invalid form.
    context = {'form': form}
    return render(request, 'article/new_article.html', context)
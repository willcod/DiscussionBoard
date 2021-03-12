from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render
from django.contrib.auth import logout, login

# Create your views here.
def logout_view(request):
    """Log the user out."""
    logout(request)
    return render(request, 'index.html')


def register(request):
    if request.method != 'POST':
        form = UserCreationForm()
    else:
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            login(request, new_user)
            return redirect('article:index')

    context = {'form':form}
    return render(request, 'users/register.html', context)
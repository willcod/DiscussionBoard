from django.shortcuts import render
from django.contrib.auth import logout

# Create your views here.
def logout_view(request):
    """Log the user out."""
    logout(request)
    return render(request, 'index.html')
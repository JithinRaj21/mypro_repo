from django.shortcuts import render


from .models import Book


# Create your views here.
def home(request):
    books = Book.objects.all()

    return render(request, 'home.html', {'book': books})

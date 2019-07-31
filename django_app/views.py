from django.shortcuts import render
from django_app.models import Post
# Create your views here.
def home(request):
    context={
    'posts':Post.objects.all()
    }
    return render(request,'django_app/home.html',context)


def about(request):
    return render(request,'django_app/about.html')

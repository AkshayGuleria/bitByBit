from django.shortcuts import render
from blog.models import Post


# Create your views here.
def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/index.html', context)


def contact(request):
    return render(request, 'blog/contact.html')

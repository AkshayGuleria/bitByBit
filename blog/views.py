from django.shortcuts import render
from datetime import date

posts = [
    {
        'author': 'Messanger of God',
        'title': 'First Dummy post',
        'content': 'First row',
        'date_posted': date(2019, 2, 9)
    },
    {
        'author': 'Babaji derey waley',
        'title': 'Second Dummy post',
        'content': 'Second row',
        'date_posted': date(2019, 2, 10)
    }
]


# Create your views here.
def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/index.html', context)


def contact(request):
    return render(request, 'blog/contact.html')

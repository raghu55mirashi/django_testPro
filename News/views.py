from django.shortcuts import render, redirect
from .register_form import Registration
from .models import Register, News
from .add_news import AddNews


def home(request):

    context = {
        'name': 'Raghu'
    }
    return render(request, 'home.html', context)


def news(request):

    data = News.objects.all()
    context = {
        'news': data
    }
    return render(request, 'news.html', context)


def newsdate(request, year):
    data = News.objects.filter(pub_date__year=year)
    context = {
        'created': year,
        'news': data
    }
    return render(request, 'news.html', context)


def contact(request):
    return render(request, 'contact.html', {})


def register(request):
    context = {
        'form': Registration
    }
    return render(request, 'register.html', context)


def adduser(request):
    form = Registration(request.POST)

    if form.is_valid():
        myregister = Register(username=form.cleaned_data['username'],
                              password=form.cleaned_data['password'],
                              email=form.cleaned_data['email'],
                              phone=form.cleaned_data['phone'])
        myregister.save()

    return redirect('home')


def addnews(request):
    context = {
        'form': AddNews
    }

    return render(request, 'addnews.html', context)


def addnewnews(request):
    form = AddNews(request.POST)

    if form.is_valid():
        mynews = News(author=form.cleaned_data['author'],
                      title=form.cleaned_data['title'],
                      desc=form.cleaned_data['desc'])
        mynews.save()

    return redirect('home')


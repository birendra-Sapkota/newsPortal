import datetime

from django.contrib import messages
from django.contrib.auth import (login, logout, authenticate, get_user_model)
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from datetime import date, timedelta

# Create your views here.
from accounts.models import Author, Article


def dashboard(request):
    day_last_week = date.today() - timedelta(days=9)

    articles_last_week = Article.objects.filter(date_created__range=(day_last_week, datetime.datetime.now()))


    date_today = datetime.datetime.now().date()

    a = 0
    b = 10
    views_list_count = []
    views_list_date = []
    for i in range(11):
        start_date = date.today() - timedelta(days=b)
        b -= 1
        articles = Article.objects.all().filter(date_created__range=(start_date, start_date + timedelta(days=1)))

        views_count = 0
        for article in articles:
            views_count = views_count + int(article.views_count)
        views_list_count.append(views_count)
        date_str = str(start_date.month) + "/" +str(start_date.day)
        views_list_date.append(date_str)

        max_range = max(views_list_count) + 1/2*(max(views_list_count))
    content = {
        'articles': articles_last_week,
        'label': views_list_date,
        'data': views_list_count,
        'max':max_range
    }

    return render(request, "admin_templates/index.html", content)


def register(request):
    if request.method == 'POST':
        email = request.POST['email']
        username = request.POST['username']
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        password = request.POST['password']
        confirm_password = request.POST['confirmpassword']

        user = User.objects.filter(username=username)

        if not user:
            if password == confirm_password:
                new_user = User.objects.create_user(username=username, email=email, first_name=first_name,
                                                    last_name=last_name)
                new_user.set_password(password)
                new_user.save()
                new_user_author = Author.objects.create(user=new_user)
                messages.success(request, "user is succesfully created.")
                return redirect('admin-register')
            else:
                messages.error(request, "password does not match")
                return redirect('admin-register')
        else:
            messages.error(request, "User already exists")
            print("username already exists")
            return redirect('admin-register')


    else:
        pass
    return render(request, "admin_templates/register.html")


def createPost(request):
    if request.method == 'POST':
        print("procesing=================")
        title = request.POST['title']
        title_caption = request.POST['title_caption']
        picture = request.FILES['cover_picture']
        tag = request.POST['tag']
        article_content = request.POST['content']
        article_summary = request.POST['summary']
        user = User.objects.filter(username=request.user.username).first()
        author = Author.objects.filter(user=user).first()
        new_post = Article.objects.create(author=author, title=title, title_caption=title_caption, picture=picture,
                                          date_created=datetime.datetime.now(), tags=tag, views_count=0,
                                          content=article_content, summary=article_summary)
        new_post.save()
        messages.success(request, "New post created successfully!!")
        return redirect('createpost')

    return render(request, "admin_templates/createpost.html")


def viewPost(request):
    username = request.user.username
    user = User.objects.all().filter(username=username).first()
    current_author = Author.objects.all().filter(user=user).first()
    current_user_articles = Article.objects.all().filter(author=current_author)
    all_articles = Article.objects.all()
    if user.is_superuser:
        content = {
            'articles': all_articles
        }
    else:
        content = {
            'articles': current_user_articles
        }

    return render(request, "admin_templates/viewpost.html", content)


def loginadmin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = User.objects.filter(username=username).first()

        if not user:
            messages.error(request, "User not found. Please provide valid credentials.")
            return redirect('login')

        else:
            if user.check_password(password):
                user_auth = authenticate(username=username, password=password)
                login(request, user_auth)
                return redirect('adminindex')
            else:
                messages.error(request, "Invalid user credentials.")
                return redirect('login')

    return render(request, 'admin_templates/login.html', )


def logoutadmin(request):
    logout(request)

    return redirect('login')

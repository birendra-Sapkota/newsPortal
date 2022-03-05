from django.shortcuts import render
from accounts.models import Author, Article, User


# Create your views here.
def homeContent(request):
    articles_header = Article.objects.all().last()
    all_post = Article.objects.all().order_by('-date_created')[5:9]
    article_for_body = Article.objects.all().order_by('-date_created')[1:5]
    a = 0
    article_body = {}
    for article in article_for_body:
        if a == 0:
            article_body['article_left'] = article
        else:
            key = "article_right" + str(a)
            article_body[key] = article
        a += 1

    content = {
        'articles_header': articles_header,
        'article_for_body': article_body,
        'all_post': all_post,
    }
    return render(request, "index.html", content)


def article(request, id):
    id = id
    article = Article.objects.all().filter(id=id).first()
    for_next = Article.objects.all().filter(tags=article.tags).order_by('-date_created')
    article.views_count = str(int(article.views_count) + 1)
    article.save()

    next = {}
    a = 0
    article_content = article.content
    paragraph = article_content.split('<paragraph>')

    for nxt in for_next:
        if a == 0:
            next['left'] = nxt
        else:
            key = 'right' + str(a)
            next[key] = nxt
        a += 1
    article_body = {"art": article,
                    "prg": paragraph}

    content = {
        'artcle': article_body,
        'next_post': next,

    }

    return render(request, 'article.html', content)


def about(request):
    return render(request, "about.html")


def politics(request):
    articles = Article.objects.all().filter(tags='Politics')
    content = {
        'articles': articles
    }
    return render(request, "politics.html", content)


def economics(request):
    articles = Article.objects.all().filter(tags='Economics')
    content = {
        'articles': articles
    }
    return render(request, "economics.html", content)


def international(request):
    articles = Article.objects.all().filter(tags='International')
    content = {
        'articles': articles
    }
    return render(request, "international.html", content)


def sport(request):
    articles = Article.objects.all().filter(tags='Sports')
    content = {
        'articles': articles
    }
    return render(request, "sport.html", content)


def tech(request):
    articles = Article.objects.all().filter(tags='Technology')
    content = {
        'articles': articles
    }
    return render(request, "technology.html", content)

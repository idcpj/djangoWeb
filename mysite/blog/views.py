from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import render_to_string
from . import models


def index(request):
    # 写法一
    # oneArticle = models.Article.objects.get(pk = 1)
    # 写法二
    Article = models.Article.objects.all()
    return render(request, 'blog/index.html', {"articles": Article})


def article_page(request, article_id):
    article = models.Article.objects.get(pk=article_id)
    return render(request, 'blog/article_page.html', {'article': article})


def edit_page(request, article_id):
    if str(article_id) == '0':
        return render(request, 'blog/edit_page.html')

    article = models.Article.objects.get(pk=article_id)
    return render(request, 'blog/edit_page.html', {'article': article})


def add(request):
    id = request.POST.get('id')
    title = request.POST.get('title', 'TITLE')
    content = request.POST.get('content', 'CONTENT')

    # 修改
    if id:
        article = models.Article.objects.get(pk=id)
        article.title = title
        article.content = content
        article.save()
        return render(request, 'blog/article_page.html', {'article': article})
    else:
        models.Article.objects.create(title=title, content=content)

        return HttpResponseRedirect('/blog/index')  # 跳转首页

        # return HttpResponse(content) # 调试

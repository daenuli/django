from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.utils import timezone
from django.core.files.storage import FileSystemStorage
# from .forms import UploadFileForm
# from django.template import loader
from .models import Article
from category.models import Category

def index(request):
    article = Article.objects.order_by('-pub_date')
    context = {'article': article}
    return render(request, 'article/index.html', context)

def create(request):
    category = Category.objects.all()
    return render(request, 'article/create.html', {'category': category})

def store(request):
    myfile = request.FILES['myfile']
    # form = UploadFileForm(request.POST, request.FILES)
    c = Article()
    c.category_id = request.POST['category_id']
    c.title = request.POST['title']
    c.content = request.POST['content']
    c.pub_date = timezone.now()
    c.image = myfile.name
    c.save()

    fs = FileSystemStorage()
    filename = fs.save(myfile.name, myfile)

    return HttpResponseRedirect(reverse('article:index'))

def edit(request, article_id):
    try:
        article = Article.objects.get(pk=article_id)
        category = Category.objects.all()
    except Article.DoesNotExist:
        raise Http404("Article does not exist")
    return render(request, 'article/edit.html', {'article': article, 'category': category})

def update(request, article_id):
    c = Article.objects.get(pk=article_id)
    c.category_id = request.POST['category_id']
    c.title = request.POST['title']
    c.content = request.POST['content']
    c.pub_date = timezone.now()
    c.save()
    return HttpResponseRedirect(reverse('article:index'))

def delete(request, article_id):
    c = Article.objects.get(pk=article_id)
    c.delete()
    return HttpResponseRedirect(reverse('article:index'))

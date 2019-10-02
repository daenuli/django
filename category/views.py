from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
# from django.template import loader
from .models import Category

def index(request):
    category = Category.objects.all()
    context = {'category': category}
    return render(request, 'category/index.html', context)

def create(request):
    return render(request, 'category/create.html')

def store(request):
    # return HttpResponse(request.POST['name'])
    c = Category(name=request.POST['name'])
    c.save()
    return HttpResponseRedirect(reverse('category:index'))

def edit(request, category_id):
    try:
        category = Category.objects.get(pk=category_id)
    except Category.DoesNotExist:
        raise Http404("Category does not exist")
    return render(request, 'category/edit.html', {'category': category})

def update(request, category_id):
    c = Category.objects.get(pk=category_id)
    c.name = request.POST['name']
    c.save()
    return HttpResponseRedirect(reverse('category:index'))

def delete(request, category_id):
    c = Category.objects.get(pk=category_id)
    c.delete()
    return HttpResponseRedirect(reverse('category:index'))

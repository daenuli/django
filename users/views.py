from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.contrib.auth.hashers import make_password
# from django.template import loader
from .models import Users

def index(request):
    users = Users.objects.all()
    context = {'users': users}
    return render(request, 'users/index.html', context)

def create(request):
    return render(request, 'users/create.html')

def store(request):
    # return HttpResponse(request.POST['name'])
    c = Users()
    c.name = request.POST['name']
    c.email = request.POST['email']
    c.password = make_password(request.POST['password'])
    c.save()
    return HttpResponseRedirect(reverse('users:index'))

def edit(request, users_id):
    try:
        users = Users.objects.get(pk=users_id)
    except Users.DoesNotExist:
        raise Http404("Users does not exist")
    return render(request, 'users/edit.html', {'users': users})

def update(request, users_id):
    c = Users.objects.get(pk=users_id)
    c.name = request.POST['name']
    c.email = request.POST['email']
    c.password = make_password(request.POST['password'])
    c.save()
    return HttpResponseRedirect(reverse('users:index'))

def delete(request, users_id):
    c = Users.objects.get(pk=users_id)
    c.delete()
    return HttpResponseRedirect(reverse('users:index'))

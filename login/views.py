from django.shortcuts import render

def index(request):
    context = {'latest_question_list': 'hello'}
    return render(request, 'login/index.html', context)

from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
def machine_learning(request):
    session = request.session['name'] = 'Abu Bakkar Siddikk'

    context = {
        'title': 'Machine Learning',
        'heading': 'Machine Learning',
        'subheading': 'Machine Learning',
        'content': 'Machine Learning Course Open for Registration',
        'request': session,
        'lists': ['Machine Learning', 'Deep Learning', 'Data Analysis', 'Data Science', 'Artificial Intelligence']
    }
    # Django Template Builtins Tags you all need to know
    # https://docs.djangoproject.com/en/4.2/ref/templates/builtins/
    return render(request, 'machine_learning.html', {'data': context}, status=200)


def registration(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST or None)
        if form.is_valid():
            form.save()
            return HttpResponse('User Created')
    else:
        form = UserCreationForm()

    return render(request, 'registration.html', {'form': form})

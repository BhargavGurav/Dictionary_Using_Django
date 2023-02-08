from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
import requests
# Create your views here.

def base(request):
    return render(request, 'base.html')

def home(request):
    context = {'response' : ''}
    if request.method == 'POST':
        query = request.POST['query']
        if query == "" or query == " ":
            messages.warning(request, 'Please Enter a word')
        else:
            r = requests.get(f'https://api.dictionaryapi.dev/api/v2/entries/en/{query}' )
            try:
                dictionary = r.json()[0]
            except:
                messages.warning(request, 'No word found!')
                return render(request, 'home.html', context)

            if dictionary:    
                messages.success(request, f"{dictionary['meanings'][0]['definitions'][0]['definition']}")
            # context['response'] = dictionary['meanings'][0]['definitions'][0]["definition"]
    return render(request, 'home.html', context)
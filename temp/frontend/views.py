from django.shortcuts import render
from api.views import check

def index(request):
    context = {}
    result = check()
    context['temp'] = result.get("temperature")
    context['humidity'] = result.get("humidity")
    return render(request, 'home.html', context)

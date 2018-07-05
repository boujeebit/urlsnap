from django.shortcuts import render
import json

from history.models import History

def history(request):
    # print(request.session['history'])
    if 'history' in request.session:
        json1_data = json.loads(request.session['history'])
    else:
        json1_data = ''
    
    return render(request, "history.html", {'local': True, 'data': json1_data})


def userHistory(request):
    history = History.objects.all()
    return render(request, "history.html", {'local': False, 'data': history})

from django.shortcuts import render
import json

def history(request):
    # print(request.session['history'])
    if 'history' in request.session:
        json1_data = json.loads(request.session['history'])
    else:
        json1_data = ''
    
    return render(request, "history.html", {'data': json1_data})
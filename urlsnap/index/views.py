from django.shortcuts import render
from django.utils import timezone
from core.volumes import static
import docker, uuid, sys
from django.core import serializers
from history.models import History

from history.models import History

import json

def getImage(URL):
    client = docker.from_env()

    unique_filename = str(uuid.uuid4()) + ".png"

    vols = {static: {'bind': '/home/pptruser/images', 'mode': 'rw'}}

    client.containers.run( image='urlsnap', auto_remove=True, cap_add=['SYS_ADMIN'], volumes=vols, command=URL + " " + unique_filename)

    # print(URL, unique_filename)
    return unique_filename

# Create your views here.
def index(request):
    if 'history' in request.session:
        history = json.loads(request.session['history'])
        print(history)
    else:
        history = []

    if request.POST:
        if request.POST['URL']:
            filename = getImage(request.POST['URL'])
            #For testing
            #filename = str(uuid.uuid4()) + ".png"

            if request.user.is_authenticated:
                newhistory = History(url=request.POST['URL'], filename=filename, querytime=timezone.now(), user=request.user)
                newhistory.save()
            else:
                newhistory = {'url': request.POST['URL'], 'filename': filename, 'querytime': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") }

                history.append(newhistory)

                request.session['history'] = json.dumps(history)

            return render(request, "index.html", {'link': filename})
        else:
            return render(request, "index.html")
    else:
        return render(request, "index.html")
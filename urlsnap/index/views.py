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

    status = client.containers.run( image='urlsnap', auto_remove=True, cap_add=['SYS_ADMIN'], volumes=vols, command=URL + " " + unique_filename)

    # print(URL, unique_filename)
    return unique_filename, status.decode("utf-8").rstrip()

# Create your views here.
def index(request):
    if 'history' in request.session:
        history = json.loads(request.session['history'])
        print(history)
    else:
        history = []

    if request.POST:
        if request.POST['URL']:
            filename, status = getImage(request.POST['URL'])
            #For testing
            #filename = str(uuid.uuid4()) + ".png"
            if status is '0':
                if request.user.is_authenticated:
                    newhistory = History(url=request.POST['URL'], filename=filename, querytime=timezone.now(), user=request.user)
                    newhistory.save()
                else:
                    newhistory = {'url': request.POST['URL'], 'filename': filename, 'querytime': timezone.now() }

                    history.append(newhistory)

                    request.session['history'] = json.dumps(history)

            return render(request, "index.html", {'link': filename, 'status': status})
        else:
            return render(request, "index.html")
    else:
        return render(request, "index.html")
from django.shortcuts import render
from core.volumes import static
import docker, uuid, sys

def getImage(URL):
    client = docker.from_env()

    unique_filename = str(uuid.uuid4()) + ".png"

    vols = {static: {'bind': '/home/pptruser/images', 'mode': 'rw'}}

    client.containers.run( image='urlsnap', auto_remove=True, cap_add=['SYS_ADMIN'], volumes=vols, command=URL + " " + unique_filename)

    print(URL, unique_filename)
    return unique_filename


# Create your views here.
def screen(request):
    if request.POST:
        if request.POST['URL']:
            print(request.POST['URL'])
            filename = getImage(request.POST['URL'])
            return render(request, "screen.html", {'link': filename})
        else:
            return render(request, "screen.html")
    else:
        return render(request, "screen.html")
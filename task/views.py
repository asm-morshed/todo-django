from django.http import HttpResponse

def index(request):
    return HttpResponse("Here is your daily task list")
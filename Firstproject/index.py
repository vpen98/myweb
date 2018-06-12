from django.http import HttpResponse
import datetime

def Helloworld(request):
    return HttpResponse("Hello World! ")
def  nowtime(request):
    now = datetime.datetime.now()
    html ="this time %s" % now
    return HttpResponse(html)

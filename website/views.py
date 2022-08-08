from django.http import HttpResponse, JsonResponse

def index(request):
    return HttpResponse("<h1>Home Page</h1>")

def about(request):
    return HttpResponse("I'm Pooyan!")

def contact(request):
    return HttpResponse("contact via pooyan@gmail.com")

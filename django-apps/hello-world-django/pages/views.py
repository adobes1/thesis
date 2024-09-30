from django.shortcuts import HttpResponse

def home_page_view(request):
    return HttpResponse("<h1>Hello, World!<h1>")

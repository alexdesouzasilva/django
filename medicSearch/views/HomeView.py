from django.http import HttpResponse


def home_view(request):
    return HttpResponse('<h1>Hello, Maria Eduarda!! </h1>', status=200)
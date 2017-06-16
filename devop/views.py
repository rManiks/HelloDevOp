from django.http import HttpResponse

def index(request):
	return HttpResponse("<h1 class='color:blue' >Hello, I am a python App...</h1>")

from django.http import HttpResponse

def index(request):
	return HttpResponse("<h1>Hello DevOps World, I am a Python app! Lets try a auto deploy<h1>")

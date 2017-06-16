from django.http import HttpResponse

def index(request):
	return HttpResponse("<h1>Hello, I am a python App... Lets do devops now</h1>")

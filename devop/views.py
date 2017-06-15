from django.http import HttpResponse

def index(request):
	return HttpResponse("Hello DevOps World, I am a Python app! Through DevOp now")

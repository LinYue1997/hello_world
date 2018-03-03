from django.http import HttpResponse

def index(request):
	return HttpResponse("hello,world.Your're at the polls index.")
# Create your views here.
from django.http import HttpResponse

def showcolor(request, color):
	resp = HttpResponse()
	resp.write(color)
	return resp


def main(request):
	resp = HttpResponse()
	resp.write("This is the main page")
	return resp
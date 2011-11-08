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


def getAverageRgb(pixels):
	if not pixels:
		return (0,0,0)
	
	pixCount =  len(pixels)

	finalR = sum(p[0] for p in pixels)/pixCount
	finalG = sum(p[1] for p in pixels)/pixCount
	finalB = sum(p[2] for p in pixels)/pixCount

	return (finalR, finalG, finalB)


def getHexadecimal(rgb):
	if not rgb:
		return "#000000"
	return "#%02X%02X%02X" % (rgb[0],rgb[1],rgb[2])

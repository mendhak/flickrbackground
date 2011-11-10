# Create your views here.
import re
from django.http import HttpResponse
import webcolors

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

	return finalR, finalG, finalB


def getHexadecimalFromRgb(rgb):
	if not rgb:
		return "#000000"
	return "#%02X%02X%02X" % (rgb[0],rgb[1],rgb[2])


def getColorByName(colorName):
	hexValue = "#000000"

	if not colorName:
		return hexValue

	colorName = colorName.lower()
	colorName = colorName.replace(' ', '')

	if colorName in webcolors.css3_names_to_hex:
		hexValue = webcolors.css3_names_to_hex[colorName]

	return hexValue


def isHexString(inputString):

	if not inputString:
		return False

	hexRe = re.compile("[a-fA-F0-9]{6}")
	return hexRe.match(inputString)

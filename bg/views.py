# Create your views here.

#sudo apt-get install python-imaging
#sudo pip install webcolors

import Image
import StringIO
import re
import urllib
from xml.dom import minidom
from django.http import HttpResponse, Http404
from django.shortcuts import render_to_response
from django.template.context import RequestContext
import webcolors
from bg import flickrapi


def showcolor(request, color, photoid):

	flickrPhotoId = getPhotoId(photoid, request)

	if not flickrPhotoId:
		raise Http404

	photoUrl = flickrapi.getLargestSizeUrl("b4fe2a004c947c42b2be8f2796796105", flickrPhotoId)

	if not photoUrl:
		raise Http404

	hexColor = getColor(color, photoUrl)

	returnUrl = "http://www.flickr.com/photo.gne?id=" + flickrPhotoId

	fullWidth = False

	if color.lower() == "full":
		fullWidth = True

	return render_to_response('display.html', {'hexColor': hexColor, 'photoUrl': photoUrl, 'returnUrl': returnUrl,
	                                           'fullWidth': fullWidth}, context_instance=RequestContext(request))


def main(request):
	resp = HttpResponse()
	return render_to_response('bg.html', {'domain': request.get_host()}, context_instance=RequestContext(request))


def getPhotoId(photoId, request):
	if photoId:
		return photoId

	if request:
		referrer = getReferrerFromRequest(request)
		photoId = flickrapi.getPhotoIdFromUrl(referrer)
		return photoId


def getColor(colorString, photoUrl):

	if not colorString:
		return "#000000"

	if colorString.lower() == "magic":
		rgbArray = getRemoteImageRgb(photoUrl)
		averageRgb = getAverageRgb(rgbArray)
		return getHexadecimalFromRgb(averageRgb)

	if isHexString(colorString):
		return "#" + colorString.lower()

	return getColorByName(colorString)



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
	return ("#%02X%02X%02X" % (rgb[0],rgb[1],rgb[2])).lower()


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


def getReferrerFromRequest(req):
	if "HTTP_REFERER" in req.META:
		return req.META["HTTP_REFERER"]

	return None


def getRemoteImageRgb(photoUrl):
	remoteimg = urllib.urlopen(photoUrl)
	imgs = StringIO.StringIO(remoteimg.read())
	img = Image.open(imgs)

	return list(img.getdata())


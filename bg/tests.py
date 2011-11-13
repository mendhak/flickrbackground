"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""
from unittest.case import skipIf
from django.http import HttpRequest

from django.test import TestCase
from django.test.client import Client
from bg import views, flickrapi
from bg.flickrapi import FlickrPhoto


class SimpleTest(TestCase):

	SKIP_HTTPREQUEST_TESTS = True

	def test_getAverageRgb_rgbTuples_GetsAverage(self):
		"""
		Passes an array of rgb values, gets an average back
		"""
		averageRgb = views.getAverageRgb([(50,50,50), (0,0,0), ])
		self.assertEqual(averageRgb[0], 25)
		self.assertEqual(averageRgb[1], 25)
		self.assertEqual(averageRgb[2], 25)

	def test_getAverageRgb_rgbTuples_OddResult_GetsLowerInteger(self):
		"""
		Passes a slightly more complex array of tuples
		The tuples' average is not a whole number
		Function should return the lower integer
		"""
		averageRgb = views.getAverageRgb([(50,50,50), (0,0,0), (1,33,17), (88,2,113), (0,2,2), (0,2,2), ])
		self.assertEqual(averageRgb[0], 23)
		self.assertEqual(averageRgb[1], 14)
		self.assertEqual(averageRgb[2], 30)

	def test_getAverageRgb_rgbTuples_Null_ReturnsBlack(self):
		"""
		Passes in a None to the getAverageRgb method, gets black back
		"""
		averageRgb = views.getAverageRgb(None)
		self.assertEqual(averageRgb[0],0)
		self.assertEqual(averageRgb[1],0)
		self.assertEqual(averageRgb[2],0)

	def test_getHexadecimalFromRgb_rgb_gets_hexadecimal(self):
		"""
		Passes an RGB value, gets a hexadecimal for CSS back
		"""
		hex = views.getHexadecimalFromRgb((131,44,17))
		self.assertEqual(hex, "#832c11")

	def test_NullRgb_ReturnsBlack(self):
		"""
		Passes a null RGB in, gets black back
		"""
		hex = views.getHexadecimalFromRgb(None)
		self.assertEqual("#000000", hex)

	def test_getColorByName_CssColorName_GetsHexValue(self):
		"""
		Pass in a color name, get a hex value back
		"""
		hex = views.getColorByName("red")
		self.assertEqual("#ff0000", hex)

	def test_getColorByName_AnyCaseName_GetsHexValue(self):
		"""
		Pass in a color name in a jumbled case, returns hex value
		"""
		hex = views.getColorByName("DArkMaGeNta")
		self.assertEqual("#8b008b", hex)

	def test_getColorByName_MultipleWordsColorName_GetsHexValue(self):
		"""
		Passes in a multi-word color, with spaces, gets a hex value back
		"""
		hex = views.getColorByName("Light Slate Gray")
		self.assertEqual("#778899", hex)
		
	def test_getColorByName_InvalidColorName_GetsBlackHex(self):
		"""
		Passes in a nonsense color name, gets black as a default back
		"""
		hex = views.getColorByName("The Colour of Magic")
		self.assertEqual("#000000", hex)

	def test_getColorByName_NullColorName_GetsBlackHex(self):
		"""
		Passes in a null color name, gets black back
		"""
		hex = views.getColorByName(None)
		self.assertEqual("#000000", hex)

	def test_isHexString_HexString_IsAValidHexString(self):
		"""
		Passes a hex string without the #, returns a boolean true
		"""
		isHex = views.isHexString("FFAC79")
		self.assertTrue(isHex)

	def test_isHexString_AnyCaseHexString_IsAValidHexString(self):
		"""
		Passes a hex string without the # in jumble case, returns a boolean true
		"""
		isHex = views.isHexString("a3CeDd")
		self.assertTrue(isHex)

	def test_isHexString_NonHexString_IsNotAValidHexString(self):
		"""
		Passes nonsense word, returns a boolean false
		"""
		isHex = views.isHexString("DDXXyio2k;")
		self.assertFalse(isHex)

	def test_isHexString_NullString_IsNotAValidHexString(self):
		"""
		Passes a null string in, gets a boolean false
		"""
		isHex = views.isHexString(None)
		self.assertFalse(isHex)


	def test_getReferrerFromRequest_Url_GetsReferrer(self):
		"""
		Given a URL request, returns the referrer
		"""

		r = HttpRequest()
		r.method == "GET"
		r.path == '/magic'
		r.META["HTTP_REFERER"] = 'test referrer'

		referrer = views.getReferrerFromRequest(r)
		self.assertEqual(referrer, 'test referrer')

	def test_getReferrerFromRequest_UrlWithoutReferrer_ReturnsNone(self):
		"""
		If a request with no referrer is passed in, None is returned
		"""

		r = HttpRequest()
		r.method == "GET"
		r.path == '/magic'

		referrer = views.getReferrerFromRequest(r)
		self.assertEqual(referrer, None)


	def test_getFlickrPhotoId_FlickrURL_ReturnsPhotoID(self):
		"""
		Given a flickr photo page URL, return the Photo ID
		"""
		photoId = flickrapi.getPhotoIdFromUrl("http://flickr.com/photos/mendhak/12345")
		self.assertEqual("12345", photoId)

	def test_getFlickrPhotoId_FlickrUrlExtended_ReturnsPhotoID(self):
		"""
		Given a long Flickr URL, return the PHOTO ID
		"""
		photoId = flickrapi.getPhotoIdFromUrl("http://www.flickr.com/photos/mendhak/123456/in/photostream/lightbox/2452")
		self.assertEqual("123456", photoId)

	def test_getFlickrPhotoId_FlickrInvalidUrl_ReturnsNone(self):
		"""
		Given an invalid flickr URL, returns None
		"""
		photoId = flickrapi.getPhotoIdFromUrl("http://www.flickr.com/photos/mendhak")
		self.assertEqual(photoId, None)

	def test_getFlickrPhotoId_None_ReturnsNone(self):
		"""
		For a None 'flickr url', returns None
		"""
		photoId = flickrapi.getPhotoIdFromUrl(None)
		self.assertEqual(photoId, None)

	def test_getImageUrl_FlickrPhoto_FlickrImageUrl(self):
		photo = FlickrPhoto()
		photo.farm = "7"
		photo.id  = "6245582355"
		photo.secret = "8a62f2a6e1"
		photo.server = "6043"

		flickrPhotoUrl = flickrapi.getImageUrl(photo, "z" )
		self.assertEqual(flickrPhotoUrl, "http://farm7.static.flickr.com/6043/6245582355_8a62f2a6e1_z.jpg")


	def test_getPhotoId_PhotoId_PhotoId(self):
		photoid = views.getPhotoId("12345",None)
		self.assertEqual("12345", photoid)

	def test_getPhotoId_None_None(self):
		photoId = views.getPhotoId(None,None)
		self.assertEqual(photoId, None)

	def test_getPhotoId_RequestReferrer_PhotoId(self):
		req = HttpRequest()
		req.META["HTTP_REFERER"] = 'http://www.flickr.com/photos/mendhak/12345/in/lightbox'

		photoId = views.getPhotoId(None, req)
		self.assertEqual(photoId, "12345")

	def test_getPhotoId_PhotoIdAndReferrer_PhotoIdPreferred(self):
		req = HttpRequest()
		req.META["HTTP_REFERER"] = 'http://www.flickr.com/photos/mendhak/12345/in/lightbox'

		photoId = views.getPhotoId("67890", req)
		self.assertEqual(photoId, "67890")

	def test_Client_NoPhotoIdAvailable_404(self):
		c = Client()
		resp = c.get('/black')
		self.assertEqual(resp.status_code, 404)

	def test_getColor_Name_Hexadecimal(self):
		hex = views.getColor("Red", None)
		self.assertEqual(hex, "#ff0000")

	def test_getColor_Hex_Hexadecimal(self):
		hex = views.getColor("Ff00a7", None)
		self.assertEqual(hex, "#ff00a7")

	def test_getColor_None_Black(self):
		hex = views.getColor(None, None)
		self.assertEqual(hex, "#000000")

	@skipIf(SKIP_HTTPREQUEST_TESTS, "Skipping method because it hits an external resource, use sparingly")
	def test_getColor_MagicWithUrl_AverageUrl(self):
		hex = views.getColor("magic", "http://farm7.static.flickr.com/6099/6304815985_ca9ffc2873_b.jpg")
		self.assertEqual(hex, "#5081cd")

	@skipIf(SKIP_HTTPREQUEST_TESTS, "Skipping method because it hits an external resource, use sparingly")
	def test_getColor_MagicCaseInsensitive_AverageUrl(self):
		hex = views.getColor("maGiC", "http://farm7.static.flickr.com/6099/6304815985_ca9ffc2873_b.jpg")
		self.assertEqual(hex, "#5081cd")

	@skipIf(SKIP_HTTPREQUEST_TESTS, "Skipping method because it hits an external resource, use sparingly")
	def test_ClientUrl_ColorPhotoId_TemplateInvoked(self):
		c = Client()
		resp = c.get('/black/6304815985')
		self.assertEqual(resp.templates[0].name, "display.html")
		self.assertEqual(resp.context['photoUrl'], "http://farm7.static.flickr.com/6099/6304815985_ca9ffc2873_b.jpg")

	@skipIf(SKIP_HTTPREQUEST_TESTS, "Skipping method because it hits an external resource, use sparingly")
	def test_ClientUrl_MagicPhotoId_TemplateInvoked(self):
		c = Client()
		resp = c.get('/magic/6304815985')
		self.assertEqual(resp.templates[0].name, "display.html")
		self.assertEqual(resp.context['hexColor'], "#5081cd")

	@skipIf(SKIP_HTTPREQUEST_TESTS, "Skipping method because it hits an external resource, use sparingly")
	def test_ClientUrl_ColorUrlReferrer_TemplateInvoked(self):
		c = Client()
		resp = c.get('/red', {}, HTTP_REFERER='http://flickr.com/photos/mendhak/6304815985/in/photostream')
		self.assertEqual(resp.templates[0].name, "display.html")
		self.assertEqual(resp.context['hexColor'], "#ff0000")

	def test_ClientUrl_Bg_MainTemplateInvoked(self):
		c = Client()
		resp = c.get("/backgrounds")
		self.assertEqual(resp.templates[0].name, "bg.html")

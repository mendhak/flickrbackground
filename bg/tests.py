"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""
from django.http import HttpRequest

from django.test import TestCase
from django.test.client import Client
from bg import views, flickrapi


class SimpleTest(TestCase):


	def getAverageRgb_rgbTuples_GetsAverage(self):
		"""
		Passes an array of rgb values, gets an average back
		"""
		averageRgb = views.getAverageRgb([(50,50,50), (0,0,0), ])
		self.assertEqual(averageRgb[0], 25)
		self.assertEqual(averageRgb[1], 25)
		self.assertEqual(averageRgb[2], 25)

	def getAverageRgb_rgbTuples_OddResult_GetsLowerInteger(self):
		"""
		Passes a slightly more complex array of tuples
		The tuples' average is not a whole number
		Function should return the lower integer
		"""
		averageRgb = views.getAverageRgb([(50,50,50), (0,0,0), (1,33,17), (88,2,113), (0,2,2), (0,2,2), ])
		self.assertEqual(averageRgb[0], 23)
		self.assertEqual(averageRgb[1], 14)
		self.assertEqual(averageRgb[2], 30)

	def getAverageRgb_rgbTuples_Null_ReturnsBlack(self):
		"""
		Passes in a None to the getAverageRgb method, gets black back
		"""
		averageRgb = views.getAverageRgb(None)
		self.assertEqual(averageRgb[0],0)
		self.assertEqual(averageRgb[1],0)
		self.assertEqual(averageRgb[2],0)

	def getHexadecimalFromRgb_rgb_gets_hexadecimal(self):
		"""
		Passes an RGB value, gets a hexadecimal for CSS back
		"""
		hex = views.getHexadecimalFromRgb((131,44,17))
		self.assertEqual(hex, "#832C11")

	def test_NullRgb_ReturnsBlack(self):
		"""
		Passes a null RGB in, gets black back
		"""
		hex = views.getHexadecimalFromRgb(None)
		self.assertEqual("#000000", hex)

	def getColorByName_CssColorName_GetsHexValue(self):
		"""
		Pass in a color name, get a hex value back
		"""
		hex = views.getColorByName("red")
		self.assertEqual("#ff0000", hex)

	def getColorByName_AnyCaseName_GetsHexValue(self):
		"""
		Pass in a color name in a jumbled case, returns hex value
		"""
		hex = views.getColorByName("DArkMaGeNta")
		self.assertEqual("#8b008b", hex)

	def getColorByName_MultipleWordsColorName_GetsHexValue(self):
		"""
		Passes in a multi-word color, with spaces, gets a hex value back
		"""
		hex = views.getColorByName("Light Slate Gray")
		self.assertEqual("#778899", hex)
		
	def getColorByName_InvalidColorName_GetsBlackHex(self):
		"""
		Passes in a nonsense color name, gets black as a default back
		"""
		hex = views.getColorByName("The Colour of Magic")
		self.assertEqual("#000000", hex)

	def getColorByName_NullColorName_GetsBlackHex(self):
		"""
		Passes in a null color name, gets black back
		"""
		hex = views.getColorByName(None)
		self.assertEqual("#000000", hex)

	def isHexString_HexString_IsAValidHexString(self):
		"""
		Passes a hex string without the #, returns a boolean true
		"""
		isHex = views.isHexString("FFAC79")
		self.assertTrue(isHex)

	def isHexString_AnyCaseHexString_IsAValidHexString(self):
		"""
		Passes a hex string without the # in jumble case, returns a boolean true
		"""
		isHex = views.isHexString("a3CeDd")
		self.assertTrue(isHex)

	def isHexString_NonHexString_IsNotAValidHexString(self):
		"""
		Passes nonsense word, returns a boolean false
		"""
		isHex = views.isHexString("DDXXyio2k;")
		self.assertFalse(isHex)

	def isHexString_NullString_IsNotAValidHexString(self):
		"""
		Passes a null string in, gets a boolean false
		"""
		isHex = views.isHexString(None)
		self.assertFalse(isHex)

#
# To process /magic URLs:

#example: http://flickr.com/photos/username/234124/in/photostream
#Get the '234124' out
#Call flickr API, get photo details
#Get medium size URL
#Request it
#Use the GetAverageRGB method


	def getReferrerFromRequest_Url_GetsReferrer(self):
		"""
		Given a URL request, returns the referrer
		"""

		r = HttpRequest()
		r.method == "GET"
		r.path == '/magic'
		r.META["HTTP_REFERER"] = 'test referrer'

		referrer = views.getReferrerFromRequest(r)
		self.assertEqual(referrer, 'test referrer')

	def getReferrerFromRequest_UrlWithoutReferrer_ReturnsNone(self):
		"""
		If a request with no referrer is passed in, None is returned
		"""

		r = HttpRequest()
		r.method == "GET"
		r.path == '/magic'

		referrer = views.getReferrerFromRequest(r)
		self.assertEqual(referrer, None)
		

	def getFlickrPhotoId_FlickrURL_ReturnsPhotoID(self):
		"""
		Given a flickr photo page URL, return the Photo ID
		"""
		photoId = flickrapi.getPhotoIdFromUrl("http://flickr.com/photos/mendhak/12345")
		self.assertEqual("12345", photoId)

	def getFlickrPhotoId_FlickrUrlExtended_ReturnsPhotoID(self):
		"""
		Given a long Flickr URL, return the PHOTO ID
		"""
		photoId = flickrapi.getPhotoIdFromUrl("http://www.flickr.com/photos/mendhak/123456/in/photostream/lightbox/2452")
		self.assertEqual("123456", photoId)

	def getFlickrPhotoId_FlickrInvalidUrl_ReturnsNone(self):
		"""
		Given an invalid flickr URL, returns None
		"""
		photoId = flickrapi.getPhotoIdFromUrl("http://www.flickr.com/photos/mendhak")
		self.assertEqual(photoId, None)

	def getFlickrPhotoId_None_ReturnsNone(self):
		"""
		For a None 'flickr url', returns None
		"""
		photoId = flickrapi.getPhotoIdFromUrl(None)
		self.assertEqual(photoId, None)

	def getPhotoInfo(self):
		flickrPhoto = flickrapi.getPhotoInfo("a39dfdf51784c76fa3234f88bec38b0e", "6245582355")
		print flickrPhoto.farm
		self.assertEqual(flickrPhoto.farm, "7")
		
"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from django.test.client import Client
from bg import views


class SimpleTest(TestCase):


	def test_rgbTuples_GetsAverage(self):
		"""
		Passes an array of rgb values, gets an average back
		"""
		print "test_rgbTuples_GetsAverage"
		averageRgb = views.getAverageRgb([(50,50,50), (0,0,0), ])
		self.assertEqual(averageRgb[0], 25)
		self.assertEqual(averageRgb[1], 25)
		self.assertEqual(averageRgb[2], 25)

	def test_rgbTuples_OddResult_GetsLowerInteger(self):
		"""
		Passes a slightly more complex array of tuples
		The tuples' average is not a whole number
		Function should return the lower integer
		"""
		print "test_rgbTuples_OddResult_GetsLowerInteger"
		averageRgb = views.getAverageRgb([(50,50,50), (0,0,0), (1,33,17), (88,2,113), (0,2,2), (0,2,2), ])
		self.assertEqual(averageRgb[0], 23)
		self.assertEqual(averageRgb[1], 14)
		self.assertEqual(averageRgb[2], 30)

	def test_rgbTuples_Null_ReturnsBlack(self):
		"""
		Passes in a None to the getAverageRgb method, gets black back
		"""
		print "test_rgbTuples_Null_ReturnsBlack"
		averageRgb = views.getAverageRgb(None)
		self.assertEqual(averageRgb[0],0)
		self.assertEqual(averageRgb[1],0)
		self.assertEqual(averageRgb[2],0)

	def test_rgb_gets_hexadecimal(self):
		"""
		Passes an RGB value, gets a hexadecimal for CSS back
		"""
		print "test_rgb_gets_hexadecimal"
		hex = views.getHexadecimalFromRgb((131,44,17))
		self.assertEqual(hex, "#832C11")

	def test_NullRgb_ReturnsBlack(self):
		"""
		Passes a null RGB in, gets black back
		"""
		print "test_NullRgb_ReturnsBlack"
		hex = views.getHexadecimalFromRgb(None)
		self.assertEqual("#000000", hex)

	def test_CssColorName_GetsHexValue(self):
		"""
		Pass in a color name, get a hex value back
		"""
		print "test_CssColorName_GetsHexValue"
		hex = views.getColorByName("red")
		self.assertEqual("#ff0000", hex)

	def test_AnyCaseName_GetsHexValue(self):
		"""
		Pass in a color name in a jumbled case, returns hex value
		"""
		print "test_AnyCaseName_GetsHexValue"
		hex = views.getColorByName("DArkMaGeNta")
		self.assertEqual("#8b008b", hex)

	def test_MultipleWordsColorName_GetsHexValue(self):
		"""
		Passes in a multi-word color, with spaces, gets a hex value back
		"""
		print "test_MultipleWordsColorName_GetsHexValue"
		hex = views.getColorByName("Light Slate Gray")
		self.assertEqual("#778899", hex)
		
	def test_InvalidColorName_GetsBlackHex(self):
		"""
		Passes in a nonsense color name, gets black as a default back
		"""
		print "test_InvalidColorName_GetsBlackHex"
		hex = views.getColorByName("The Colour of Magic")
		self.assertEqual("#000000", hex)

	def test_NullColorName_GetsBlackHex(self):
		"""
		Passes in a null color name, gets black back
		"""
		print "test_NullColorName_GetsBlackHex"
		hex = views.getColorByName(None)
		self.assertEqual("#000000", hex)

	def test_HexString_IsAValidHexString(self):
		"""
		Passes a hex string without the #, returns a boolean true
		"""
		print "test_HexString_IsAValidHexString"
		isHex = views.isHexString("FFAC79")
		self.assertTrue(isHex)

	def test_AnyCaseHexString_IsAValidHexString(self):
		"""
		Passes a hex string without the # in jumble case, returns a boolean true
		"""
		print "test_AnyCaseHexString_IsAValidHexString"
		isHex = views.isHexString("a3CeDd")
		self.assertTrue(isHex)

	def test_NonHexString_IsNotAValidHexString(self):
		"""
		Passes nonsense word, returns a boolean false
		"""
		print "test_NonHexString_IsNotAValidHexString"
		isHex = views.isHexString("DDXXyio2k;")
		self.assertFalse(isHex)

	def test_NullString_IsNotAValidHexString(self):
		"""
		Passes a null string in, gets a boolean false
		"""
		print "test_NullString_IsNotAValidHexString"
		isHex = views.isHexString(None)
		self.assertFalse(isHex)





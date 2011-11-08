"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from bg import views


class SimpleTest(TestCase):
	def test_basic_addition(self):
		"""
		Tests that 1 + 1 always equals 2.
		"""
		print "test_basic_addition"
		self.assertEqual(1 + 1, 2)

	def test_rgbTuples_GetsAverage(self):
		"""
		Passes an array of rgb values, gets an average back
		"""
		print "rgbTuples_GetsAverage"
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
		print "rgbTuples_OddResult_GetsLowerInteger"
		averageRgb = views.getAverageRgb([(50,50,50), (0,0,0), (1,33,17), (88,2,113), (0,2,2), (0,2,2), ])
		self.assertEqual(averageRgb[0], 23)
		self.assertEqual(averageRgb[1], 14)
		self.assertEqual(averageRgb[2], 30)

	def test_rgbTuples_Null_ReturnsBlack(self):
		"""
		Passes in a None to the getAverageRgb method, gets black back
		"""
		print "rgbTuples_Null_ReturnsBlack"
		averageRgb = views.getAverageRgb(None)
		self.assertEqual(averageRgb[0],0)
		self.assertEqual(averageRgb[1],0)
		self.assertEqual(averageRgb[2],0)

	def test_rgb_gets_hexadecimal(self):
		"""
		Passes an RGB value, gets a hexadecimal for CSS back
		"""
		hex = views.getHexadecimal((131,44,17))
		self.assertEqual(hex, "#832C11")

	def test_NullRgb_ReturnsBlack(self):
		"""
		Passes a null RGB in, gets black back
		"""
		hex = views.getHexadecimal(None)
		self.assertEqual("#000000", hex)
		



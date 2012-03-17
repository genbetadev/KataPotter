from twisted.trial import unittest

from kataPotter.katapotter import BooksPack

class BooksPackTest(unittest.TestCase):
	"""
	Tests for BooksPack class
	"""

	def test_zero_books(self):		
		books = BooksPack([])
		self.assertTrue(books.calculate() == 0)

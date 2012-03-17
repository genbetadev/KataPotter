from twisted.trial import unittest

from kataPotter.katapotter import BooksPack

class BooksPackTest(unittest.TestCase):
	"""
	Tests for BooksPack class
	"""

	def test_zero_books(self):		
		books = BooksPack([])
		self.assertTrue(books.calculate() == 0)

	def test_one_to_five_book(self):
		for i in range(1, 6):
			books = BooksPack([i])
		self.assertTrue(books.calculate() == 8*i)
	
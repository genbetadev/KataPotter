from twisted.trial import unittest

from kataPotter.katapotter import BooksPack

class BooksPackTest(unittest.TestCase):
	"""
	Tests for BooksPack class
	"""

	def test_zero_books(self):		
		books = BooksPack([])
		self.assertTrue(books.calculate() == 0)

	def test_one_book(self):
		books = BooksPack([1])
		self.assertTrue(books.calculate() == 8)

	def test_two_books(self):
		books = BooksPack([2])
		self.assertTrue(books.calculate() == 8*2)
from twisted.trial import unittest

from kataPotter.katapotter import BooksPack

class BooksPackTest(unittest.TestCase):
	"""
	Tests for BooksPack class
	"""

	def test_zero_books(self):		
		books = BooksPack([])
		self.assertEqual(books.calculate(), 0)

	def test_one_to_five_book(self):
		for i in range(1, 6):
			books = BooksPack([i])
		self.assertEqual(books.calculate(), 8*i)
	
	def test_two_dif_books(self):
		books = BooksPack([1, 1])
		self.assertEqual(books.calculate(), (8*2)*0.95)

	def test_two_dif_one_not_books(self):
		books = BooksPack([2, 1])
		self.assertEqual(books.calculate(), ((8*2)*0.95)+8)
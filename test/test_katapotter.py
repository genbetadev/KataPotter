
#Copyright (c) 2012 - Oscar Campos <oscar.campos@member.fsf.org>
# See LICENSE for details

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

	def test_edge_case_one(self):
		books = BooksPack([2, 2, 2, 1, 1])
		self.assertEqual(books.calculate(), 2 * (8 * 4 * 0.80))

	def test_edge_case_two(self):
		books = BooksPack([5, 5, 4, 5, 4])
		self.assertEqual(books.calculate(), 
			3 * (8 * 5 * 0.75) + 2 * (8 * 4 * 0.8))
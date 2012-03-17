
# -*- test-case-name: test.katapotter.test_katapotter -*-
# Copyright (c) 2012 - Oscar Campos <oscar.campos@member.fsf.org>
# See LICENSE for more details 

class BooksPack(object):
	"""
	List of books to pack
	"""

	def __init__(self, books):
		self._books = books


	def calculate(self):
		try:
			if len(self._books) == 1:
				return self._books[0] * 8
			else:
				return (self._books[0] + self._books[1]) * 8 * 0.95
		except IndexError:
			return 0
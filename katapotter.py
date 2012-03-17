
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
		return 0

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
		price = 0
		discounts = [0, 1, 0.95, 0.90, 0.80, 0.75]
		packs = []

		for books_number in self._books:			
			for i in range(0, books_number):				
				if len(packs) <= i:
					packs.append(0)

				packs[i] +=1;
		
		for pack in packs:			
			price += (8 * pack) * discounts[pack]

		return price
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import csv, sys

class ReaderCSV(object):
	def __init__(self, name):
		self.filename=name
		pass
			
	def reader(self):
		try:
			f=open(self.filename, 'rb')
			self.reader = csv.reader(f, delimiter=',')
		except:
			sys.exit('Arquivo invalido!\n')
	
	def getLine(self):
		try:
			self.reader()
		finally:
			return self.reader.next()
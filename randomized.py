#!/usr/bin/env python
# -*- coding: utf-8 -*-
from random import randint, randrange

class Randomized(object):
	listConnectors=["de", "do", "dos", "da", "e"]
	def __init__(self): pass
	def getEmail(self): pass
	def getRandomDate(self): pass
	def setListConnectors(self): pass
	def setEmail(self): pass
	def setDate(self): pass
	def removeConnectors(self, list):
		for i in list:
			if i in self.listConnectors:
				list.remove(i)
		return list

class RandonEmailByName(Randomized):
	#gerando bem até 30 emails
	def getEmail(self, nome, qtd):
		especial=["","", ".", "_"]
		res=[]
		while qtd:
			mail=""
			#randint determina a profundidade de sobrenomes
			nomes=nome[0:randint(1, len(nome))]
			
			#remove conectores dos nomes
			nomes=self.removeConnectors(nomes)
			
			#sorteia um nome principal
			s=randint(0, len(nomes)-1)
			
			#sorteia caracter especial
			separador=especial[randint(0,3)]
			
			for n in nomes:
				if nomes[s]==n:
					mail+=n
				else:
					mail+= n if(randrange(100)>randrange(100)) else n[0]
				mail+=separador
			if mail[len(mail)-1] == separador:
				mail=mail[:-1]
			if mail+"@id.uff.br" not in res:
				res.append(mail+"@id.uff.br")
				qtd-=1
		return res
		
class RandonEmailByLastname(Randomized):
	def getEmail(self, nome, qtd):
		especial=["","", ".", "_"]
		res=[]
		while qtd:
			mail=""
			nomes=nome[1:] #somente sobrenomes
			nomes=self.removeConnectors(nomes)			
			s=randint(0, len(nomes)-1)
			separador=especial[randint(0,3)]
			
			for n in nomes:
				if nomes[s]==n:
					mail+=n
				else:
					mail+= n if(randrange(100)>randrange(100)) else n[0]
				mail+=separador
			if mail[len(mail)-1] == separador:
				mail=mail[:-1]
			if mail+"@id.uff.br" not in res:
				res.append(mail+"@id.uff.br")
			qtd-=1
		return res
		
		
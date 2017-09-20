#!/usr/bin/env python
# -*- coding: utf-8 -*-
from file import ReaderCSV
from randomized import RandonEmailByName, RandonEmailByLastname

class Aluno(object):
	nome=[]
	matricula = telefone = email = uffmail = status = None 
	
	def __init__(self, list):
		self.nome, self.matricula, self.telefone, self.email, self.uffmail, status = list
		self.nome=self.nome.split(" ")
	
	def isActive(self):
		return self.status=="Ativo"

class SearchMatricula(ReaderCSV):
	def __init__(self):
		self.filename="alunos.csv"
	
	def getLine(self, mat):
		try:
			while 1:
				res=Aluno(super(SearchMatricula, self).getLine())
				if res.matricula==mat and res.isActive:
					return res
		except: 
			return 0

def main():
	m = ""
	while not m:
		m = raw_input('Digite sua matricula: ')
	search=SearchMatricula()
	aluno=search.getLine(m)
	
	m = ""
	while not m:
		m = raw_input('Gerar email por: \n  0-Nome \n  1-Sobrenome\nOP:')
	
	email=RandonEmailByName() #default
	if m=='1':
		email=RandonEmailByLastname()
	#elif m=='2':
	
	if aluno:
		print "\n{0}, por favor escolha um dos emails abaixo:\n".format(aluno.nome[0])
		emails=email.getEmail(aluno.nome, 10)
		for e in emails:
			print "{0} - {1}".format(emails.index(e), e)

		m = ""
		while not m:
			m = raw_input('\nOP:')
		print """A criacao de seu e-mail ({0}) sera feita nos proximos minutos.
Um SMS foi enviado para {1} com a sua senha de acesso.""".format(emails[int(m)],aluno.telefone)
		
	else:
		print "ERRO: Matricula de aluno invalida!"
	
	


if __name__=='__main__':
	main()
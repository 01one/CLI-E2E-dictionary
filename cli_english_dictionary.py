#  Copyright 2022 Mahid
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY
import os
from pprint import pprint
import pickle
try:
	with open('DictionaryData.pickle', 'rb') as data:
		dictionary_data= pickle.load(data)
except:
	from zipfile import ZipFile
	mainfile = ZipFile('DictionaryData.zip', 'r')
	mainfile.extractall()
	mainfile.close()
	with open('DictionaryData.pickle', 'rb') as data:
		dictionary_data= pickle.load(data)
	
word=dictionary_data[0]
meaning=dictionary_data[1]
run=True
while run:
	x=str(input("Enter your word: "))
	x=x.upper()
	if x in word:
		y=word.index(x)
		print("Word Number: ", y)
		pprint(meaning[y])
	if x=="ENDD":
		run=False
	elif x=="CLS":
		try:
			os.system("cls")
		except:
			os.system("clear")

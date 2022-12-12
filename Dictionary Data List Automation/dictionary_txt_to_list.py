#  2022 Mahid
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY
from string import punctuation
import pickle
dict_data=[]
dict_data1=[]



try:
	data = open('dictionary_main.txt')
except:
	from zipfile import ZipFile
	mainfile = ZipFile('dictionary_main.zip', 'r')
	mainfile.extractall()
	mainfile.close()
	data = open('dictionary_main.txt')


LineList = data.readlines()
num_line=0
global c_1
c_1=''
run=True
while run:
	line=LineList[num_line]
	if not any(p in line[:-1] for p in punctuation):
		if line.isupper():
			if line[:-1]=="ENDDICTIONARY":
				dict_data1.append(c_1)
				run=False
			else:
				line=line[:-1]
				
				dict_data.append(line)
				if c_1=='':
					pass
				else:
					dict_data1.append(c_1)
				c_1=''
	else:
		c_1=c_1+line[:-1]
	num_line+=1
	
all_data=[dict_data,dict_data1]

"""
#Read Data
with open('DictionaryData.pickle', 'rb') as data:
	dictionary_data= pickle.load(data)
	#print(dictionary_data)# """

#"""
#Write Data
with open('DictionaryData.pickle', 'wb') as data:
	pickle.dump(all_data, data)
	data.close()#"""

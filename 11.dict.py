#print key if appear >2 times in a dictionary

import ast
import collections

def listkey(d,a):
	for key in d:
		a.append(key)
		if isinstance(d[key], dict):
			listkey(d[key], a)
	return a


def readIn():
	file=str(input("Give a name of file:"))
	try:
		fn=open(file,'r')
	except IOError: 
		print("Error: File does not appear to exist.")
		return 0
	return fn.read()

fn=readIn()
print(fn)
a=[]
d=ast.literal_eval(fn) #gia na to metatrepsei se dictionary
res = listkey(d,a)
print([item for item, count in collections.Counter(res).items() if count > 2])

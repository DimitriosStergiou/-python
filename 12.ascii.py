
def readIn():
	file=str(input("Give a name of file:"))
	try:
		fn=open(file,'r')
	except IOError: 
		print("Error: File does not appear to exist.")
		return 0
	return fn.read()

s=readIn()
myList=[]
for c in s:
	k=128-ord(c)
	myList.append(chr(k))
print(myList)
for i in range(len(myList)):
	print(myList[len(myList)-i-1], end="")
print("")

import requests
def numbers(fox):
	num=''
	for x in fox:
		if x=="]":
			break
		else:
			num=num+x
	return num
def createList():
	myList=[]
	for i in range(81):
		myList.append(int(0))
	return myList

def statistic(stat):
	for i in range(80):
		s=(stat[i+1]/25)*100
		print("Number ", i+1 ,": Appears ", stat[i+1], " times in January. ",s,"%")

count=852886 #drawid klirosis
stat=createList() #empty list for statistic

for i in range(25):
	string='https://api.opap.gr/draws/v3.0/1100/'
	string=string+str(count)
	response = requests.get(string)
	fox=response.text
	k=fox.find("winningNumbers")
	k=k+25 #Begin
	k2=k+60 #end
	num=numbers(fox[k:k2])
	num2=num.split(",")
	for n in range(len(num2)):
		num2[n]=int(num2[n])
	print(num2)
	count=count+180 #paei sto drawid tis epomenis meras 1i klirosi
	for m in range(81):
		if m in num2:
			stat[m]=stat[m]+1

statistic(stat)
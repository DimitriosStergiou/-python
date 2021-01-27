#Fermat Theorem a^p=a (mod p)
#If we multiply both sides with a^-1, we get a^(p-1)=1(mod p) for 1<=a<p
from math import exp
import random 

fibonacci_numbers = [0, 1]
n=int(input("Enter a sequence Fibonacci term:"))
for i in range(2,n):
	fibonacci_numbers.append(fibonacci_numbers[i-1]+fibonacci_numbers[i-2])
p=fibonacci_numbers[len(fibonacci_numbers)-1]
c=0
while c<20:
	a=random.randint(1,p-1)
	f=a**(p-1)
	if (f%p) ==1:
		print("Prime number is:", a)
		break;
	if c==19:
		print("Not a prime number!")
	c+=1



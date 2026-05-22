n=int(input("factorial of number : "))

fac=1

for x in range(1,n+1):
	fac*=x
	x+=1
print("factorial of ", n ," is " ,fac)
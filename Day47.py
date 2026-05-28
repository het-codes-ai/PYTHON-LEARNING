n=int(input("enter your number  "))

if (-999999999)<n<3:
	print(n , " is neither prime nor composite")

for i in range (2,n,1):
	
	if n%i==0:
		print("COMPOSITE")
		break
		
	else:
		print("PRIME")
		break
		
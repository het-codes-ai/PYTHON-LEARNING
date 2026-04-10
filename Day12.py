print('HI!!')
print('I am you calculator')

a=float(input("Tell me your 1st number "))
b=float(input("tell me your 2nd number "))
o=input("Which operator do you want to use add/minus/multiply/divide")
if o=="sum" or o=="+" or o=="add":
	ans=a+b
	print(a,'+',b,'=',ans)
	
if o=="minus" or o=="-":
	ans=a-b
	print(a,'-',b,'=',ans)	

if o=="multiply" or o=="×" or o=="x":
	ans=a*b
	print(a,'×',b,'=',ans)

if o=="division" or o=="÷" or o=="/":
	ans=a/b
	print(a,'÷',b,'=',ans)	
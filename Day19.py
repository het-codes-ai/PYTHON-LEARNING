list1=[]
list1.append(input("enter list element"))
list1.append(input("enter list element"))
list1.append(input("enter list element"))
list1.append(input("enter list element"))
list1.append(input("enter list element"))
copy1=list1.copy()
rev1=list(reversed(list1))

print(" This is list : ",copy1)
print(" This is reversed list : ",rev1)

if copy1==rev1:
	print("Given list is a palindrome")

else:
	print("Given list is not a palindrome")






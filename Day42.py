list=["a","b","c","d"]

def ele(n):
	if n>=len(list):
		return "END OF LIST"
	print(list[n])
	return ele(n+1)
	
	
print(ele(0))

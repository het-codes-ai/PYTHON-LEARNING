correct_user="admin25"
correct_pass="2598"

entered_user=input("ENTER YOUR USERNAME:")
entered_pass=input("ENTER YOUR PASSWORD:")
if entered_user==correct_user and entered_pass==correct_pass: 
	print('ACCESS GRANTED!')
elif entered_user==correct_user:
	print('PASSWORD INCORRECT!!! TRY AGAIN!!!')
else:
	print('USERNAME NOT FOUND')
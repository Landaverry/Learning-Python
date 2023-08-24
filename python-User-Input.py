#Python User input 
test=input()
#takes the user's input and prints it.
print(test)

#Prompting a user to enter their IP: 
test=input("Enter Your IP Address:")
print(test)

#Combining Loops and conditional statements with user input
while True: 
	test=input("Enter Your IP Address:")
	print(">>> {}".format(test))
	if test == "exit" or test =="Exit":
		break
	else:
		print("exploiting..")
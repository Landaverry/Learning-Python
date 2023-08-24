#Error and Exception Handling within python
#Python does very little error handling at compile and execution time
#Instead python defers almost all checks on each line until that line runs
#If a mistake is made or an edge case is missed, a try catch block or exception should be implemented
#Try - Lets block of code be tested
#except - Handles any errors
#finally - executes regardless of the results of the try and accept blocks. 
#Python has a few errors that can be raised, syntax, identation, arithmetic, etc.

try: 
	#File that does not exist
	f = open("Text-Not-Exist.txt")
except: 
	#Catch all for errors. However this error message will display at the sign of any exception
	print("The file does not exist!")


#Another example - 
#Where the exception will change based on the error thrown by Python
try:
	f=open("Text-Not-Exist.txt")
#Specific file not found exception handler
except FileNotFoundError:
	print("The file does not exist!")
#Catch all for all other exceptions
except Exception as e:
	print(e)
finally:
	print("Try-Block reached finally. This prints regardsless of error or not")


#Assertions
n = 1
assert(1 != 0)
print(1/n)

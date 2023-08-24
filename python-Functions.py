#Functions and Code Reuse.
#Functions only run when its called. 
#print is a function but you can create your own

def function1():
	print("This is a function!")

#functions can also a value
def returnValue():
	return "This is a value returned from a function"
x = returnValue()
print(x)

#Values can also be passed into functions as a value
def parameterPassing(s):
	print("\t{}".format(s))
parameterPassing("parameter")

#Functions can be passed in multiple values
def multiValue(s1,s2):
	print("{} {}".format(s1,s2)) 
multiValue("any","thing")
multiValue(s2="be",s1="apple")

def default(s1="default"):
	#Parameter can be blank and will use default as the value
	#if a parameter is passed it will use that value instead
	print("{}".format(s1))
default("Anything")
default()

#Functions can also handle an unknown number of variables/arguments
#use list comprhension
def unknownargs(s1,*more):
	print("{} {}".format(s1,"".join([s for s in more])))
unknownargs("Function")
unknownargs("1,2,3,4,5,6","a","b")

#function for dictionaries 
def dictionar(**ks):
	for a in ks:
		print(a,ks[a])
dictionar(a="1",b="2",c="3")

#functions could expect several types of data types: 
#String, float, integer, list
def dataTypes(s,f,i,l):
	print(type(s))
	print(type(f))
	print(type(i))
	print(type(l))
dataTypes("s",1.0,2,['L','i','s','t'])

#Variables can either be local or global. 
#Variables declared in the main body of code are global and can be used across the whole body of code.
#variables declared in within a function are local scope and can only bes used by that function.
v=9
def local():
	global v
	v+=1
	val=100
	print(val+v)
	#Val is only availble within this function
	#to use v it must be declared as global
local()
#Functions can call other functions
def firstfunction():
	print("this is a function")

def functioncall():
	firstfunction()
	print("Second Function calling firstfunction")
functioncall()

#recursive functions
#Need a termination condition otherwise the execution will run indefinetly
def recursive(x):
	print(x)
	if x > 0:
		recursive(x-1)
recursive(10)
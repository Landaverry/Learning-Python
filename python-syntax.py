#Booleans and writing conditionals 
valid = True

not_valid = False

print(valid)
print(not_valid)

print(valid==True)
print(not_valid==True)

print(valid==not_valid)
print(not_valid!=valid)
print(not not_valid)
print(not valid)

print((10<9)==True)
print(10==10)
print(10!=100)
print(10>=100)
print(10<=100)

print(10>5 or 10<15)
print(10>5 and 10<5)
print(bool(1))
print(bool(0))
print("---------------------------------------")
#Arithmetic & Math operators
print(10+10)
print(10-10)
print(10*10)
print(10/10)
print(10 % 3)
print(10**10)

x=10
y=20
print(x)
x+=1
print(x)

y-=x
print(y)
x*=5
print(x)
print(x % y)

print("---------------------------------------")
#Binary Operators
print(bin(x))
print(bin(y))

print(bin(x)[2:].rjust(4,"0"))
print(bin(y)[2:].rjust(4,"0"))

print(bin(x+y)[2:].rjust(4,"0"))
print(x+y)

print(bin(x|y)[2:].rjust(4,"0")) #bitwise or
print(bin(x&y)[2:].rjust(4,"0")) #bitwise and

print(bin(x>>1)[2:].rjust(4,"0")) #bitwise shift to the right by 1

print(bin(y<<4)[2:].rjust(4,"0")) #bitwise shift to the left by 4

print("---------------------------------------------")
#Tuples
tuple_items = ("Item1", "Item2", "Item3")
tuple_Num=(1,4,6)

print(tuple_Num)
print(tuple_items)

tuple_repeat=("Combine!",)*4
mixed_tuple=("A",1,"B",2)
#Tuples are immutable. They cannot be changed or appended but they can be combined
tuple_Combined=tuple_repeat+mixed_tuple
print(tuple_Combined)

#tuples can be unpacked.
item1, item2, item3 = tuple_items
print(item1)
print(item2)
print(item3)

print("Item2" in tuple_items)
print(tuple_items.index("Item2"))
print("item4" in tuple_items)

print(mixed_tuple[0])
print(mixed_tuple[len(mixed_tuple)-1])

#extract number of elements using slices. The number after the colon is not inclusive
print(mixed_tuple[0:3])

#Lists 
list_string=["A","B","C","D","F"]
print(list_string)

list_mixed=[[],list(),"Egg", 2.2,5,("A")]

print(list_mixed)
print(type(list_mixed))
list_mixed[0]="Changed index"
print(list_mixed)

del list_mixed[2]
list_mixed.insert(2,1000)

list_mixed.append([])
print(list_mixed)

list_mixed.reverse()
print(list_mixed)

list2=[2,1,3,4]
list_mixed.extend(list2)
print(list_mixed)

list2.sort()
print(list2)

print("-------------------------------------------------")
#Dictionaries
#Use {} 
#If performance is important use dictionaries 

dict1={"a":1,"b":2,"c":3}
print(dict1)
print(type(dict1))
print(len(dict1))

print(dict1["a"])
print(dict1.get("a"))

print(dict1.keys())
print(dict1.values())
print(dict1.items())

dict1["a"] = 1
print(dict1)

dict1["d"]=4
print(dict1)

dict1["a"]=0
print(dict1)
dict1.update({"a":1})
print(dict1)

dict1.pop("c")
print(dict1)
#delete dictionary entries
del dict1['b']
print(dict1)
#nested dictionary
dict1['c']={"a":1, "b":2}
print(dict1)
#define dictionaries
dict2={}
print(dict2)
dict3 =dict()
print(dict3)
print("--------------------------------------------------")
#Sets 
#sets can store mutltiple values in one variable. 
#Great if you don't care about order of the data
set1 = {"a", "b", "c"}
#Similiar to dictionaries but there is no key pair. There is no indexs
print(set1)
print(set1)
print(type(set1))

#Sets cannot have duplicate values
#Sets can be of any value not just strings

set2={"a","a","a"}
print(set2)

set3={"a",0,False}
set4=set(("b",4,True))
#True = 1 and False = 0
print(set3)
print(set4)

set1.add("d")
print(set1)

set3.update(set4)

print(set1)
print(set3)

list1=["a","b","c","d"]

set4={4,5,6}
print(list1)
print(set4)

set4.update(list1)
print(set4)

set5={4,5,6}
#union of two sets. 
set6=set4.union(set5)
print(set6)


#remove() & discard() will remove items for the set. However, Remove() will error
#if the item is not in the set. 
#Only use pop() if you do not care the order of the set. 
print("-----------------------------------------------------------")

#Conditional Statements
#Based on the condition of true or false
if True:
	print("True")
#Not Going to print
if False:
	print("False")
if not False:
	print("Not False")

if 1<1:
	print("1 < 1")
elif 1 <= 1:
	print("1 <= 1")
else:
	print("else 1")


if 1<1:
	print("1 < 1")
elif 1 < 1:
	print("1 < 1")
elif 2 <= 2:
	print("2 <= 2")
else:
	print("else reached")

if 1<1:
	print("1 < 1")
elif 1 < 1:
	print("1 < 1")
elif 2 < 2:
	print("2 <= 2")
else:
	print("else reached")
#and & or operators
if 1>0 and 0<1:
	print("1 is greater than 0 & 0 is less than 1")

if 1<0 or 5>1:
	print("1 less than 0 OR 5 greater than 1")

#Using or and and together
if (0==0 or 1==1) and 5==5:
	print("0=0 or 1=1 AND 5=5")

#Conditionals are very useful because they can enable different actions based on the results of comparisons
#Conditionals are executed in linear order. 
#always consider potential edge cases.










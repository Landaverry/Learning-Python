#List Comprehension - Provide a shorter syntax to create a list based on some iterable
list1=['a','b','c','d']
print(list1)

list2 = [x for x in list1]
print("List2: " + str(list2))

#using Conditionals with Comprehensions
list3=[x for x in list1 if x =='a' or x=='c']
print("List3:" + str(list3))

#Using ranges
list4 = [x for x in range(10)]
print("List4: " + str(list4))

#applying Octal function to each function as its being added to the list
list5 = [oct(x) for x in range(10)]
print("List5: " + str(list5))

#Turnary Conditionals
list6 = [bin(x) if x>0 else "X" for x in range(10)]
print("List6: " + str(list6))

list7 = [x*x for x in range(10)]
print("List7: " + str(list7))

#Using nested expressions
list8=[[1,2,3,4],[5,6,7,8],[9,10,11,12]]
print("List8:" + str(list8))
#Take the element y, from list x and put it into its own list
#Takes the elements from the nested lists and combines them into one
list9=[y for x in list8 for y in x]
print("List9:" + str(list9))

#Can also apply to sets
set1={x+x for x in range(5)}
print("Set1:"+str(set1))

list10=[c for c in "Test-String-List"]
#Break string into individual characters 
print("List10:" + str(list10))
#Joining back the string with the * character between each character
print("Joining of the * characters in a list:"+"*".join(list10))

list11=[]
for c in "string":
	list11.append(c)
	print("Appending characters to list" + str(list11))
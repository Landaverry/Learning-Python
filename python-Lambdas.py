#Lambdas are anonymous function without names
#can have any number of arguments but only one expression

add_4=lambda x : x+4
print(add_4(4))

add = lambda x,y: x+y
print(add(2,2))

#Lambda is useful for short expression 
is_even = lambda x: x % 2 ==0
print(is_even(2))
print(is_even(3))

blocks = lambda x, y: [x[i:i+y] for i in range(0,len(x),y)]
print(blocks("string",2))

order = lambda x: [ord(i) for i in x]
print(order("ABCDEFGHIJabcder@#$%203456"))


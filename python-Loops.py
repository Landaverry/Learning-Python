#Loops
a=1
while a<10:
	a+=1
	print(a)
print("---")
for i in range(5):
	print(i+6)
print("---")
for i in range(3):
	for j in range(5):
		print(i,j)
print("---")
for i in range(5):
 	if i==2: 
 		i%=3
 	print(i)
 	continue
print("---")

for c in "test-string":
	print(c)

print("---")
for key, value in {"a":2,"b":3,"c":4}.items():
	print(key,value)
print("---")

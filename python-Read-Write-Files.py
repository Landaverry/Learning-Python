#Reading and Writing to Files
#Python has standard functions for reading from or writing to files.
f = open('python-Loops.py')
#Displays file name, access mode and encoding.
print(f)

# you can specify if text is text or binary
#read each line in file. 
print(f.read())

#Create an array of each line in the file
print(f.readlines())
#Could be useful to search for particular words or IOCs during a incident? 
#Readlines can result in an empty array, this is beacuse python has read to the end of the file.
#To reset this, you must run: 
f.seek(0)
#This will return the starting position of the file to the beginning. 
print(f.readlines())
#End of the file has been reached, seek must be used again. 
f.seek(0)
#Now to iterate over each line and strip each \n within the array
for line in f:
	print(line.strip())
#Close File
f.close()

#Writing to a text file. W - represents write
f = open("python-write-test.txt", "w")
#If the code above is ran, the python compiler will error because the file does not exist
#However if within python code the file is written to, Python will create a file. 
f.write("This is a test line of code that writes into a this txt file")
f.close()
#To append text to a particular file it must be opened in append mode. 
f = open("python-write-test.txt","a")
f.write("An appended line of text that was added within python code")
f.close()

#Additional functions to determine the status of a file
print("Name of file:" + f.name)
print("Closed or Open:" + str(f.closed))
print("File Mode:" + f.mode)

#using the file object as an interator.
#In this instance using the rockyou.txt password file, as an example to brute force passwords.
with open('rockyou.txt', encoding='latin-1') as f:
	for line in f:
		pass
#This will take a while as each entry within the rockyou.txt would be iterated through.



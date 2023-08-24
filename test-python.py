#Variable Types
name = "John"
name_length = 4
name_list = ["Lisa","Ron","eak","nancy"]
print(type(name_list))
name1, name2, name3, name4 = name_list
print(name1)
print(name4)

name_tuple=("nuet", "00048C")
print(type(name_tuple))

name_dictionary={"john",4,"00048c",6}
print(type(name_dictionary))

name_boolen = True
print(type(name_boolen))

name_range=range(6)
print(type(name_range))

print(name_list)
print(name_tuple)
print(name_dictionary)
print(name_boolen)
print(name_range)

#Working with Numbers
number_int =1
number_float=1.25
print(number_int)
print(number_float)

number_complex = 3.14j
print(type(number_complex))
number_hex=0xa
print(number_hex)
print(type(number_hex))

number_octal=0o10
print(type(number_octal))

print(number_int+number_octal)

print(bin(6969))
print(hex(6969))
print(oct(6969))

#String Formatting
string1="I am a String"
print(string1)

string2='I am a String 2'
print(string2)

string3="""I 
am 
a long string
...!!"""
print(string3)
string4 = "I \'am\' a \"String\""
print(string4)

string5="Print backslashes \\ \\ and hex \x41 \x42"
print(string5)

string6="Mutli-String"*3
print(string6)
print(len(string6))
print(string6.startswith("u"))
print(string6.index("-"))
print(string6.upper())
print(string6.lower())

messy_string = "hdkj;bj  hdop;ih hhtps 			378907ry"
print(messy_string)
print(messy_string.strip())
print(messy_string.replace(";","REPLACEMENT"))

print(messy_string.split())
print(messy_string.split(";"))

string4="Modfied string"
print(string4)
print(string4.encode())
print(string4.encode("utf-8"))
print(string4.rjust(25,"x"))
print(string4.ljust(22,"X"))

print("CONCAT"+"A string")
print("length of String6 - " + str(len(string6)))

print("Length of String4 is {} Characters long".format(len(string4)))
# string_investigation.py
# By: Aidan
# Date: 15/6/2022

from audioop import mul


name = "Aidan"

print("Welcome", name)

name = 'Aidan'
print ('Welcome', name)
name = "John O'Sullivan"
print(name)
message = 'press the "red" button'
print (message)

# escape characters

message ="this \n message \n has multiple \n lines"
print (message)

message = "press the \"red\" button"
print (message)

print("1\t23456 \t \t 3")
print("10\t2\t\t3")
print("100\t2\t\t3.36786")
print("1000\t2\t\t3")

file = "c:\\my documents\\newfile.txt"

print (file)

multi_line_string='''
            this 
            is
            a 
            multiline
            string
'''

print (multi_line_string)


name = "Aidan"
age = 21


message = "Welcome " + name + " you are " + str(21)

print (message)

# string.format is the old way of putting variables into a string
message = "Welcome {} you are {}"
print(message.format(name, age))

# since python 3.6 we can use "f-strings"

message = f"Welcome { name } you are { age }"
print(message)

a = 10
b = 20

message = f"{ a } + { b } = { a + b }"

print (message)

# round brackets functions / function calls  ()
# square brackets lists / arrays 
# curly brackets f string substitutions

# in addition:
# () for tuple
# {} for dictionary
# [] 


# ternary operator in a an f-string
from random import randint
r = randint(1, 100)
message = f"The number { r } is { ('large' if r>50 else 'small') }"
print(message)


name = "Aidan"

print(name.upper())

message = "this is a message that has some words. this is the second line."

words = message.split(" ")

for word in words:
    print(word.upper())

print ("=================================")
# words.sort()

for word in words:
    print(word.upper())


print (message.title())



print("aidan".upper())

print("======================================")
print (words)

print(" ".join(words))







































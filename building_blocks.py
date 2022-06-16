# building_blocks.py
# By: Aidan
# Date: 15/6/2022

print("these are the building blocks")


# Building Block #2 - variable

name = "Aidan"
print (name)

#  firstName = "aidan" in python we don't use camel case
first_name = "Aidan"
last_name = "Killeen"

fname = "Aidan"
lname = "Killeen"

fn = "Aidan"
ln = "Killeen"

the_first_name_of_the_employee = "Aidan"

a = 20
b = 10

# Building block #3 - expression
c = a + b

print(c)

d = 1.23456

print (d)

e = a / b
print (e)

big_number = 1234567890111213141516171819187654322123232323342439797345
bigger_number = big_number * 10

print (bigger_number)
pi = 3.14159

notpi = int(pi)

print (notpi)


answer = ((a + b) * c) / (d + e)    # use brackets to clearly identify the precedence

print (answer)

print ("the answer is ", answer)


message = "Welcome " + name

print(message)


# building block #4 - functions

def greet(name):
    print ("Welcome " + name)

greet("Aidan")




greet("Alice")
# greet()




# Building Block #5 - List / Array

list = ["red", "green", "blue", "orange"]


print(list)

print(list[0])
print(list[1])

print(len(list))

print(list[len(list)-1])    # print last item in list

# print(list[999]) # index out of range

test_string = "abcdefghijklmnopqrstuvwxyz"

print(len(test_string))
print(test_string[0])
print(test_string[len(test_string)-1])

# pythonic ways of accessing a list
print (test_string[1:5])
print (test_string[10:25])
print (test_string[:10])
print (test_string[10:])
print (test_string[:])
print (test_string[-5])
print (test_string[-1]) # more concise way of getting the last item
print (test_string[-10:])
print (test_string[-10:-5])
print (test_string[10:-10])


days = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]

print(days)
print(days[-1])
print(days[1:-1])           # why is -1 not the last element???





# Building Block #6 - Loop

count = 1

print ("starting")
while count <= 10:
    print (count)
    count = count + 1

print("finished")

print(list)

for item in list:
    print(item)

print(test_string)

for letter in test_string:
    print (letter)

for letter in test_string[10:-10]:
    print (letter)

# pythonic for loop 

numbers = range(1, 10)

for number in numbers:
    print (number)

for number in range(1, 11):
    print (number)

for number in range(1, 11, 3):
    print (number)


# use a function that isn't one of the built in functions
# get access (import) the random number function from the standard library called random

print("==============================================")
from random import randint

r = randint(1, 10)
print (r)

# Building Block #7 - Conditional Statements (if statement)

if r > 5:
    print (r, "is big")
else:
    print (r, "is small")

print ("==================================")


if r <= 3:
    print (r, "is small")
elif r <= 7:
    print (r, "is medium")
else:
    print (r, "is large")


print ("=====================================")
# ternary operator

r = randint(1, 10)

print (r)

if r<5:
    message = "the value is " + str(r) + ", it is small"
else:
    message = "the value is " + str(r) + ", it is large"


print (message)

# do the same thing
message = "the value is " + str(r) + (",it is small" if r<5 else ",it is large")

print(message)


# Building Block #8 - Objects - TBD


































































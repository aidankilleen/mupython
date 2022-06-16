from random import randint

r = randint(1, 10)

print (r)

name = "Aidan"


message = f"Hello {name}"

print (message)


person = {'name':'Aidan', 'age':21}

message = "Hello, {name}. You are {age}.".format(**person)

print (message)


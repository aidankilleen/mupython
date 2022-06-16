# input_investigation.py
# Name: Aidan
# Date: 16/6/2022

from numpy import True_


print("What is your name?")

# name = input("Enter username:")
# print(name)

finished = False
colours = []
while finished == False:

    colour = input("Enter a colour:")

    if colour == "":
        finished = True
    else:
        colours.append(colour)

colours = set(colours)
print (colours)
print ("finished")


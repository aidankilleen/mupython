# file_input_investigation.py
# By: Aidan
# Date: 16/6/2022

f = open("test.txt")

contents = f.read()

print(contents)

colour_file = open("colours.txt")
contents = colour_file.readlines()
colour_list = set(contents)

print(colour_list)

colour_file.close()

colour_file = open("colours.txt")

line = colour_file.readline()

colour_list = []

while line != "":
    print(line)
    line = colour_file.readline()
    colour = line.strip()
    colour_list.append(colour)

colour_list = set(colour_list)
colour_file.close()

print(colour_list)
print("finished")

# new attempt at reading the colours

colour_file = open("colours.txt")
colour_list = []
finished = False

while finished != True:
    line = colour_file.readline()

    if line == "":
        finished = True
    else:
        colour_list.append(line.strip())

colour_list = set(colour_list)
print(colour_list)



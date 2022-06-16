# file_output_investigation.py
# By: Aidan
# Date: 16/6/2022


f = open("names.txt", "a")  # r = read only   w = write   a = append

names = ["Alice", "Bob", "Carol", "Dan"]

for name in names:
    f.write(f"{name}\n")

f.close()


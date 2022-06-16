
students = {"Alice", "Bob", "Carol", "Dan", "Alice", "Dan"}

print(students)

python_class = {"Alice", "Bob", "Carol", "Dan"}
fortran_class = {"Alice", "Eve", "Fred", "Carol"}

all_students = python_class.union(fortran_class)
both = python_class.intersection(fortran_class)
diff1 = python_class.difference(fortran_class)
diff2 = fortran_class.difference(python_class)
print (all_students)
print (both)
print (diff1)
print (diff2)

numbers = [1, 3, 2, 5, 3, 7, 6, 6, 7, 5, 7, 4, 2, 1]

unique_list = set(numbers)
print(unique_list)

unique_list = set({})

for number in numbers:
    unique_list.add(number)

print(unique_list)

ul = list(unique_list)

print(ul)


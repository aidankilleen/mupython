# tuple_investigation.py
# By: Aidan
# Date: 16/6/2022

t = (1, 2, 4, 7, 9, 10)

print (t)

for item in t:
    print(item)


def analyse_data(list):
    sum = 0
    count = 0
    while (count < len(list)):
        sum = sum + list[count]
        count = count + 1
    average = sum / len(list)
    return (sum, average)

answer = analyse_data([1, 2, 3, 4, 5])

print (f"sum={answer[0]} average={answer[1]}")

# list = [1,2,3,4,5]


a = 1
b = 2

print (f"a={a} b={b}")

# swap two variables
# traditional way = create a temporary variable

t = a
a = b
b = t

print (f"a={a} b={b}")


# use case for tuple - swap two variables

(a,b) = (b,a)

print (f"a={a} b={b}")

# use case for tuple - do multiple assignments 

answer = analyse_data([1,6,2,8,3,9,10,4])

(sum, average) = answer

print (f"sum={sum} average={average}")

(sum, average) = analyse_data([5,5,5,5,5])

print (f"sum={sum} average={average}")

# do not redefine built-in function names like list
# list = [1,2,3]

t = (2,2,2,2)
l = list(t)

print (t)
print (l)










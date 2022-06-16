# error_investigation.py
# By: Aidan
# Date: 16/6/2022


# 3 types of errors
#
# syntax errors - vs code will highlight these in red
# runtime errors 
# logic - we'll use the debugger to get these

from random import randint

a = 100
b = 0

# try:
#     answer = a / b
# except ZeroDivisionError:
#     print ("you can't divide by zero")


# try:
#     do_something()
#     do_something_else()
# except SomeError:

# except SomeotherError:

# except:







# c - style "defensive programming"
# if b != 0:
#   answer = a / b

# rt = do_something()

# if rt == -1:
#     # some error
# elif rt == -2:
#     # some other error
# elif rt == -3:
#     # yet another error
# else
#     # code actually worked
# rt = do_something_else()

# if rt == -1:
#     # some error
# elif rt == -2:
#     # some other error
# elif rt == -3@
#     # yet another error
# else
#     # code actually worked







a = 100
b = 0
numbers = [1, 2, 3]

r = randint(1, 5)

try:
    if r == 1:
        answer = a / b
    elif r == 2:
        answer = numbers[3]
    elif r == 3:
        answer = non_function()
    elif r == 4:
        answer = int("one")
    else:
        answer = 42 # no error occurred
except ZeroDivisionError:
    print("you can't divide by zero")
    answer = a
except NameError:
    print("check your code - invalid function call")
    answer = 0
except ValueError:
    print(f"can't convert \"one\" to a number")
    answer = 1
except:
    print("something went wrong")
    answer = 0
finally:
    print (f"The answer is {answer}")

    
print ("Finished")

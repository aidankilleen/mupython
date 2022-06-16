# raise_exception_investigation.py
# Name: Aidan
# Date: 16/6/2022

def do_something(number):

    try:
        result = int(number) + 1
    except:
        result = 1
        raise Exception("invalid parameter type, you must supply a number")
    return result

try:
    answer = do_something(1)
    print(answer)    
    answer = do_something("1")
    print(answer)    
    answer = do_something("one")
    print(answer)    
except:
    print("something went wrong")



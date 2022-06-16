# analyse_data.py
# By: Aidan
# Date: 16/6/2022

# miscellaneous functions for analysing data

title = "The Data Analysis Project"

days = ("mon", "tue", "wed", "thu", "fri", "sat", "sun")

def greet(name):
    print (f"Hello {name}")

def analyse_data(list):
    sum = 0
    count = 0
    while (count < len(list)):
        sum = sum + list[count]
        count = count + 1
    average = sum / len(list)
    return (sum, average)

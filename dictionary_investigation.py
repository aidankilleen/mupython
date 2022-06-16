# dictionary_investigation.py
# By: Aidan
# Date: 16/6/2022

user = {
    "name": "Aidan", 
    "title": "Trainer", 
    "email": "aidan.killeen@gmail.com"
}

print(user["name"])
print(user["title"])
print(user["email"])

user["email"]="aidan@professional.ie"

print(user)
print(user.keys())

keys = user.keys()
for key in keys:
    print (key)

values = user.values()
print(values)

for key in keys:
    print (f"{key} = {user[key]}")


python_course = {
    "trainer": "Aidan", 
    "students": ["Anthony", "Nick", "Saeed", "..."]
}

for student in python_course["students"]:
    print(student)

data = [1, 2, 3, 4]

# in python the items in the list do not need to be the same
data2 = [1, "one", 1.1, [1,1,1]]

# same for a tuple
t = (3, 3.3, "three", [33.3,3])

# same for a dictionary
answer = {
    "sum": 25, 
    "average": 5.5, 
    "max": 5, 
    "min": 5, 
    "day": "Monday"
}


python_course = {
    "trainer": "Aidan", 
    "students": ["Anthony", "Nick", "Saeed", "..."]
}


python_courses = [
    {
        "trainer":"Aidan", 
        "client": "Maynooth University",
        "students": ("Anthony", "Nick", "...")
    }, 
    {
        "trainer": "Bill", 
        "client": "Chemical Industry Skillnet", 
        "students": ("Alice", "Bob", "Carol", "Dan")
    }
]
for course in python_courses:
    print(course["client"])








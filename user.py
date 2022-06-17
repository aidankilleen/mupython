class User:

    def __init__(self, id, name, email):
        self.id = id
        self.name = name
        self.email = email

    def display(self):
        print(f"ID\t{self.id}")
        print(f"Name\t{self.name}")
        print(f"Email\t{self.email}")

u = User(1, "Alice", "alice@gmail.com")
u2 = User(2, "Bob", "bob@gmail.com")

users = [
    User(1, "Alice", "alice@gmail.com"), 
    User(2, "Bob", "bob@gmail.com"), 
    User(3, "Carol", "carol@gmail.com"), 
    User(4, "Dan", "dan@gmail.com")
]

for user in users:
    user.display()

print(type(users))
print(type(u))

import numpy as np

r = np.random.randint(1, 10, (1, 10))

print(type(r))

print (r)

sum = r[0][0] + r[0][1]

print(sum)

subset = r[0, 0:2]

print (subset)

sum = subset.sum()

print (sum)












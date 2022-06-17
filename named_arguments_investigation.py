# named_arguments_investigation.py
# By: Aidan
# Date: 17/6/2022


def show_info(id, name="no name", email="no email", phone="no phone"):
    print(f"ID:\t { id }")
    print(f"Name:\t { name }")
    print(f"Email:\t { email }")
    print(f"Phone:\t { phone }")

show_info(1, "Aidan", "aidan.killeen@gmail.com", "0872035060")
show_info(phone="087222222", name="Fred", email="fred@gmail.com", id=9)
show_info(1, "Alice", "alice@gmail.com")
show_info(1, "Bob")
show_info(1, )

show_info(1, email="aidan@gmail.com")




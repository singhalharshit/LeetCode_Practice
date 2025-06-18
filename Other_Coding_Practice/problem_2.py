"""
    Movie ticket pricing as per age
    12 rs for 18 and 18+ 8rs for children and 2rs discount on wednesday
"""

day = input("Enter the day: ")
age = int(input("Enter an age: "))

if age >=18:
    if day != "Wednesday":
        print("Ticket Price is 12rs")
    else:
        print("Ticket price is 10 rs")
else:
    if day != "Wednesday":
        print("Ticket Price is 8 rs")
    else:
        print("Ticket price is 6 rs")
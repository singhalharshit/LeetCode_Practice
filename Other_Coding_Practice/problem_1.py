"""
    Age Group Categorization 
    Child <13, Teenager (13-19), Adult(20-59), Senior Citizen >60
"""

age = int(input("Enter an age: "))
if age>0 and age < 13:
    print("Child")
elif age >= 13 and age<=19:
    print("Teenager")
elif age>=20 and age<=59:
    print("Adult")
else:
    print("Senior Citizen")

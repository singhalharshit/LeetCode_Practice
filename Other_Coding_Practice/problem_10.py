"""
    Keep asking for user input until they give anything between 1-10
"""

# num = int(input("Enter an input"))

while True:
    num = int(input("Enter an input: "))
    if 0< num <=10:
        print(num)
        break
    else:
        num = int(input("Enter an input: "))
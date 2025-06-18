"""
    Reverse a string using loop
"""

string = input("Enter a string to reverse: ")

count = len(string)

for i in range(count+1):
    print(string[count-1],end='')
    count-=1
    if count==0:
        break

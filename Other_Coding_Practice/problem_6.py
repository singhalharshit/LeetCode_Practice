"""
    Print the multiplication table for a given number upto 10, but skip the fifth iteration
"""

num= int(input("Enter a number for table: "))

for i in range(1,11):
    if i==5:
        pass
    else:
        print(f"{num}*{i} = ",num*i)

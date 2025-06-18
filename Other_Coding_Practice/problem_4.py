"""
    Given a list count how many positive numbers into it
"""

l=[0, 5, -3, 9, -2, -8, 7]
count=0
for i in range(len(l)):
    if l[i] >0:
       count+=1

print(count)


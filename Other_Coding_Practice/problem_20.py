"""
    Write a function that takes variable number of arguments and returns their sum
"""

def calc(*args):
    sum=0
    for i in args:
        sum+=i
    return sum


print(calc(3,4,5,6))
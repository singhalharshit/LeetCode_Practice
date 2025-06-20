"""
    Write a function that returns both area and circumference of a circle given it's radius
"""

# def calc(x):
#     area= (3.14*(x*x))
#     circumference = 2*3.14*x
#     return area,circumference



# using import math module

import math

def calc(x):
    area = math.pi*(x*x)
    circumference = 2*math.pi*x
    return area,circumference

print(calc(7))
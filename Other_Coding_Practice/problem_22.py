"""
    Create a recursive function that calculates the factorial of a number
    Recursive - it is a technique to call the function again and again inside the function itself
"""

# Normal way 

# def fact(x):
#     num=1
#     for i in range(1,x):
#         num*=x
#         x-=1
#     return num



def fact(x):
    if x==0:
        return 1
    else:
        return x * fact(x-1)

print(fact(6))
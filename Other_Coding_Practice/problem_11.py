"""
    Prime number checker
"""

num = int(input("Enter an input: "))

is_prime = True

if num>1:
    for i in range(2,num):
        if (num%i)==0:
            is_prime = False

print(is_prime)
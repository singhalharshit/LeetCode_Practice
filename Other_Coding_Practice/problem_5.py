"""
    sum of n even number
"""

num = int(input("Enter a number: "))
sum=0
for i in range(num+1):
    if i%2==0:
        sum+=i

print(sum)
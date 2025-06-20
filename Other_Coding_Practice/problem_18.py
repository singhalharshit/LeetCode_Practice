"""
    Write a function that greets a user. If no name is provided it should greet with a default name
"""

def greet(x="Default Name"):
    return "Welcome to the Party",x


print("1",greet())
print("2",greet("Some random name"))
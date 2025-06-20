"""
    Create a function that accepts any number of keyword arguments and prints them in the format key:value
"""


def kwargs(**kwargs):
    for key,values in kwargs.items():
        return f"{key}:{values}"
    
print(kwargs(name="Harshit", age=23, language="Python", country="India", role="Developer"))



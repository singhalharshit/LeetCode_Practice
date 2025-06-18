"""
    Given a string find the first non repeated character
"""

string = "teeter"
for i in string:
    if string.count(i) > 1:
        pass
    elif string.count(i) ==1:
        print(i)
        break
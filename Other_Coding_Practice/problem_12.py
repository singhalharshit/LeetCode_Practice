"""
    List Uniqueness Checker - Check if all the elements in a list are unique. If a duplicate is found exit the loop and print the duplicate
"""


l=[101, "apple", 42, "banana", 73, "carrot", "apple", 99, "date", 42, "egg"]

# for i in l:
#     if l.count(i)>1:
#         print(i)
#         break

# Another method by set

l1= set()

for i in l:
    if i in l1:
        print(i)
        break
    l1.add(i)


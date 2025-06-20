"""
    Generally scopes start from {} like a scope of functions and what not 
    function test(){

    }
    This is how a function scope is defined  
    So here is the case when you make a scope it's like you have a new memory inside the scope so whatever is inside a scope it can't be accessed outside of it.
       
"""

username = "Global_xyz"

def func():
    username= "xyz"
    return username
print(username)
print(func())

# Now here you can see that I have declared two variables with the same name but in different location one inside a function which is limited to only the function "func" and one is global and can be accessed anywhere even within the function.


username_1= "Global_xyz_1"

def func_1():
    # username_1= "xyz"
    return username_1
print(username_1)
print(func_1())

# Now into this case we can see that as soon as commented out the username_1, it printed out the global variable so hence inside the block/scope/namesapce first priority is always given to the local variable and then to a global variable and also a global variable can be called inside a function or any scope but not a variable defined inside a function can be called outside it.

# We will check this here


new_username="Shubham"

def printsurname():
    surname="Sharma"
    return surname

print(new_username)
print(printsurname())
# print(surname)


# You see when we did print(surname) it broke since it could not find any variable surname inside the code since we were calling it outside it's scope

# More with scopes
x=99

def calc(y):
    z=x+y
    return z


print(calc(1))

# So here we can see that x was taken from the global scope

a=56

def func3():
    global a
    a=88
    return a

# so now into this case we can see that how do we modify the value of global variable but yeah this practice should be avoided

func3()
print(a)


# Bit more tricky

def f1():
    a=27
    def f2():
        print(a)
    return f2()

res= f1()
print(res)
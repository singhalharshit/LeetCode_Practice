# Object Types / Data Types

- Number 
- String
- List -> [] -> A Continuous Memory space with multiple indexing
- Tuple -> () -> 
- Dictionary -> {}
- Set -> ()
- Files
- Boolean -> True
- None 

### Internal Working of Python 

- Python treats integers and string in a complete different way internally since python is a number powerful language 
- Python has memory reference before the variable is assigned
- so what happens when we declare a variable let say we declared score = 10 so at first 10 is made then it's reference is made and then it is assigned to a variable (in this case score)
- SO REMEMBER THIS THING - That all the datatype stays into memory and never goes to variable, variable just store references so let's say that score = 10 here score just has reference of int it's not that, that my score has datatype int
- So data object exists in memory, and variables just point to them
- Garbage collection in python for strings and integer is never done immediately it is always done bit late.
- To Explain memory reference let's take an example -  let say we have a variable a = 5 and b = 2 so now 5 reference is in a and 2 reference is in b. Next we did a= a+2 and now we know that a = 7. But 7 does not directly get's assigned into a at first the object is created (into our case 7 is created) and it's reference is assigned into a and now 5 reference is empty so garbage collector won't collect it immediately it will do it after sometime
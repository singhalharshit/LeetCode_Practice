"""
    Grade Calculator 
    A (90-100)
    B (80-89)
    C (70-79)
    D (60-69)
    F Below 60

"""

Total_Grade = int(input("Enter Grade: "))

if Total_Grade >=90 and Total_Grade <=100:
    print("A")
elif Total_Grade <=89 and Total_Grade >=80:
    print("B")
elif Total_Grade <=79 and Total_Grade >=70:
    print("C")
elif Total_Grade <=69 and Total_Grade >=60:
    print("D")
else:
    print("F")
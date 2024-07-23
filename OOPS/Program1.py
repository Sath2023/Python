class Student:

## THE FIRST CONSTRUCTOR IS CALLED AS DEFAULT CONSTRUCTOR
    def __init__(self,name,marks):
        print("Adding student to the database")
    # name = "Sathvik"

## THE BELOW CONSTRUCTOR IS KNOWN AS PARAMETERIZED CONSTRUCTORS
    def __init__(self,name,marks):
        self.name = name 
        self.marks = marks
        print("Adding student to the database")
s1 = Student("Sathvik.N.B.Math",99)
print("Name is:",s1.name,"marks is",s1.marks)

s2 = Student("V.Adithya",99)
print("Name is",s2.name,"marks is",s2.marks)
        
### INTERNALLY s1 IS SAME AS self
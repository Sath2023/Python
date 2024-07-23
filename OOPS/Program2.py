class Student:
    college_name = "Presidency University" ## CLASS ATTRIBUTE
    def __init__(self,name,marks):
        self.name = name ## OBJECT ATTRIBUTE
        self.marks = marks ## OBJECT ATTRIBUTE

    def welcome(self):
        print("Welcome",self.name)

    def get_marks(self):
        print("Marks of",self.name,"is",self.marks)
s1 = Student("Sathvik.N.B.Math",99)
print("Student details : \nName :",s1.name,"\nMarks :",s1.marks,"\nCollege :",Student.college_name)
s1.welcome()
s1.get_marks()
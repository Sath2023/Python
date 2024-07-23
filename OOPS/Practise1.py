## CREATE A STUDENT CLASS THAT TAKES NAME AND 3 SUBJECT MARKS AS ARGUMENTS IN CONSTRUCTOR. THEN CREATE A METHOD THAT CALCULATES AVERAGE OF THE MARKS


## THIS IS BY INSERTING MARKS INDIVIDUALLY
class Student:
    def __init__(self,name,marks1,marks2,marks3):
        self.name = name
        self.marks1 = marks1
        self.marks2 = marks2
        self.marks3 = marks3

    def avg(self):
        sum = 0
        sum = self.marks1 + self.marks2 + self.marks3
        average = sum/3
        return average
    
s1 = Student("Sathvik.N.B.Math",99,98,97)
print("Yo",s1.name,"you scored :",s1.avg())

## CALCULATING AVERAGE BY PROVIDING A LIST AS AN INPUT

class Stud:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

    @staticmethod
    def hello():
        print("Hello")
    def get_avg(self):
        sum = 0
        for val in self.marks:
            sum += val
        print("Hi",self.name,"you have secured an average of",sum/3)
new_student = Stud("SATHVIK",[96,97,98])
new_student.get_avg()
new_student.hello()
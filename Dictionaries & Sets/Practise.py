furniture = {
    "table" : "It is a piece of furniture",
    "cat" : "a small animal",
    "car" : "an automobile"
}
print(furniture)

subjects = {"Python","Java","C++","Javascript","Java","Python","Java","C++","C"}
count = len(subjects)
print("The number of classrooms required are : ",count)

student_marks = {}
marks1 = int(input("Enter the marks of first subject : "))
student_marks.update({"Maths":marks1})
marks2 = int(input("Enter the marks of second subject : "))
student_marks.update({"Science":marks2})
marks3 = int(input("Enter the marks of third subject : "))
student_marks.update({"Kannada":marks3})
print("Marks obtained by the student is : ",student_marks)

## PRINTING 9 and 9.0
values = {
    ("float",9.0),
    ("int",9)
}
print(values)
print("Deciding the Grade of the Student")
name = str(input("Enter your name : "))
sub1 = str(input("Enter the subject1 name : "))
sub2 = str(input("Enter the subject2 name : "))
sub3 = str(input("Enter the subject3 name : "))
marks1 = int(input("Enter the marks of first subject : "))
marks2 = int(input("Enter the marks of second subject : "))
marks3 = int(input("Enter the marks of third subject : "))
sum = marks1 + marks2 + marks3
avg = sum/3
if avg < 35:
    print(name, "Has failed in Exam")
elif avg >= 35 and avg < 60:
    print(name, "Has passed the exam")
elif avg >= 60 and avg < 75:
    print(name, "Has passed the exam in First Division")
else:
    print(name, "Has passed the exam in Distinction")
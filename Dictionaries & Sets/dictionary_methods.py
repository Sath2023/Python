student = {
    "name" : "NAME",
    "marks" : { 
        "maths" : 90,
        "english" : 80,
        "science" : 70
    }
}
print("The different keys in the student are : ",list(student.keys()))
print("The different values in the ductionary are : ",list(student.values()))
print("The different items in the student are : ",list(student.items()))
print("The length of the student is : ",len(student))
print("The value the name key contains is : ",student.get("name"))
print(student["marks"]["maths"])

student.update({"city":"Bengaluru"})
print("The updated student dictionary is : ",student)
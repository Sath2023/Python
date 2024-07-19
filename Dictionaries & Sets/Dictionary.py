info = {
    "key" : "value",
    "name" : "Sathvik N B Math",
    "age" : 20,
    "address" : "Bangalore",
    "phone" : "1234567890",
}

print(info)
print(type(info))
print(info["name"])

## NESTED DISCTIONARIES

nested_dict = {
    "name" : "Sathvik",
    "marks" : 
    {
        "maths" : 90,
        "science" : 80,
        "english" : 70
    }
}

print(nested_dict)
print("The marks obtained in maths is : ",nested_dict["marks"]["maths"])
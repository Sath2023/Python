print("Arithmetic Operations : ")
num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number : "))
operation = input("Enter the operation to be performed : ")
if(operation == "add"):
    print("The operation selected is : ",operation," thus the sum is :",(num1 + num2))
elif(operation == "sub"):
    if(num2 > num1):
        print("The operation selected is : ",operation," thus the difference is : ",(num2 - num1))
    else:
        print("The operation selected is : ",operation," thus the difference is : ",(num1 - num2))
elif(operation == "mul"):
    print("The operation selected is : ",operation," thus the product is : ",(num1 * num2))
elif(operation == "div"):
    if(num2 == 0):
        print("Divison not possible")
    else:
        print("The operation selected is : ",operation," thus the quotient is : ",(num1 / num2))
elif(operation == "floor_division"):
    if(num2 == 0):
        print("Divison not possible")
    else:
        print("The operation selected is : ",operation," thus the nearest quotient is : ",(num1 // num2))
elif(operation == "modulus"):
    print("The operation selected is : ",operation," thus the remainder is : ",(num1 % num2))
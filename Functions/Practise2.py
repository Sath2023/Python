## WRITE A FUNCTION TO FIND THE FACTORIAL OF THE NUMBERS
def fact(n):
    fact = 1
    for i in range(1,n+1):
        fact = fact * i
    return fact

number = int(input("Enter the number for which factorial needs to be calculated : "))
# print("The factorial of the given number is : ",fact(5))   
print("The factorial of",number,"is",fact(number))

## WRITE A FUNCTION TO CONVERT USD TO INR

def conversion(usd):
    inr = usd * 83.14
    return inr
usd = int(input("Enter the amount in dollars : "))
print("For",usd,"it would be rupees",conversion(usd))
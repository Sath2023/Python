## AVERAGE OF THREE NUMBERS

def avg(a,b,c):
    average = (a+b+c)/3
    # return average
    print(average)

x = int(input("Enter the first number : "))
y = int(input("Enter the second number : "))
z = int(input("Enter the third number : "))
print("The average of three numbers is : ",avg(x,y,z))
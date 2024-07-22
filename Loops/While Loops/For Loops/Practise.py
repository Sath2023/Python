## WRITE A PROGRAM TO PRINT THE SUM OF N NUMBER 
n = int(input("Enter the number of numbers for which the sum needs to be calculated : "))
sum = 0
for i in range(1,n+1):
    sum = i+sum
print("The sum of",n,"numbers is : ",sum)


## PRINTING FACTORIAL OF A NUMBER
num = int(input("Enter the number for which factorial needs to be calculated : "))
fact = 1
for i in range(1,num+1):
    fact = i*fact
print("The factorial of",num,"is : ",fact)

## OR
num = int(input("Enter the number for which factorial needs to be calculated : "))
fact = 1
i=1
while i<=num:
    fact = i*fact
    i+=1
print(fact)
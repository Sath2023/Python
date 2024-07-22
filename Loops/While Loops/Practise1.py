## PRINTING NUMBERS FROM 1 TO 100
print("Ascending orders of numbers from 1 to 100")
i=1
while i<=100:
    print(i)
    i = i+1
print("*******************************************")


## PRINTING NUMBER FROM 100 TO 1
print("Descending order of numbers from 1 to 100")
i=100
while i>=1:
    print(i)
    i-=1

## WRITING MULTIPLICATION TABLE OF NUMBER N
num = int(input("Enter a number of your choice : "))
while i<=10:
    mul = num * i
    i += 1
    print(num," * ",i," = ",mul)


## PRINTING SQAURES OF NUMBERS
i = 1
while i<=10:
    print(i**2)
    i = i+1


## PRINTING NUMBERS FROM THE LIST
print("Traversing through list :")
num_list = [1,4,9,16,25,36,49,64,81,100]
idx = 0
while idx < len(num_list):
    print(num_list[idx])
    idx += 1


print("Searcing for an element from the list : ")
num_list = [1,4,9,16,25,36,49,64,81,100]
num = int(input("Enter the number to be searched : "))
i = 0
while i < len(num_list):
    if (num_list[i] == num):
        print("The requested element is present at ",i," position")
    i+=1
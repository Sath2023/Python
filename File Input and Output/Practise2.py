## CHECKING THE COUNT OF EVEN NUMBERS FROM THE FILE

with open("File Input and Output/read.txt","r") as f:
    data = f.read()
    print(data)
    num = data.split(",")
    print(num)
    count = 0
    for ele in num:
        if int(ele) %2 == 0:
            count += 1
print("The number of even numbers are : ",count)
            
    
# print("The number of even numbers are : ",count_even_numbers())
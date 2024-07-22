## PRINTING SQUARES FROM 1 TO 100 WITHIN A LIST 

squares_list = []
for i in range(1,11):
    squares_list.append(i**2)
    i = i+1
print(squares_list)

## FINDING AN ELEMENT FROM A TUPLE
squares_tuple = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
x = int(input("Enter the number to be searched in the tuple : "))
i = 0
for el in squares_tuple:
    if x == el:
        print(x, "found in tuples at position : ",i)
    i += 1
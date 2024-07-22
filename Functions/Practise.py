## WRITE A FUNCTION TO PRINT THE LENGTH OF LIST

def length(random_list):
    length  = len(random_list)
    return length

## PRINTING ELEMENTS OF THE LIST IN A SINGLE LINE
def print_elements(random_list):
    for i in random_list:
        print(i, end=" ")
    return i
    
    
random_list  = [1,2,3,4,5,6,7,8,9,10]
print("The length of the list is : ",length(random_list))
print(print_elements(random_list))

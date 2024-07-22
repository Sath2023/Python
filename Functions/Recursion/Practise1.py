## WRITE A RECURSIVE FUNCTION TO CALCULATE THE SUM OF NUMBERS
def sum(n):
    if n==0:
        return 0
    return sum(n-1)+ n
print(sum(5))


## WRITE A RECURSIVE FUNCTION TO PRINT THE ELEMENTS OF THE LIST HINT USE INDEX AND LENGTH
def show(num,index=0):
    if (index == len(num)):
        return
    print(num[index])
    show(num,index+1)
num = [1,2,3,4,5,6]
show(num)
def show(n):
    if(n==0):
        return
### THIS if ACTS AS AN ENDING CONDITION
    print(n)
    show(n-1)
    print("END")
    ### THIS IS RECURION BECAUSE show() function is being called inside show() function again
show(5) 

### RECURSIVE FACTORIAL
def fact(n):
    if(n==0) or (n==1):
        return 1
    return fact(n-1) * n
    
print(fact(5))
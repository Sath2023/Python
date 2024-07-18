A = int(input("Input : "))
G = input("M/F : ")
if((A==1)or(A==2) and (G=="M")):
    print("Fees is 100")
elif((A==3)or(A==4) or (G=="F")):
    print("Fees is 200")
elif((A==5)or(A==6)):
    print("Fees is 300")
else:
    print("Invalid Input")

year = int(input("Enter your birth year : "))
current_year = 2024
age = current_year - year
if(age >= 18):
    print("You are eligible for the following \n1. Driving License,\n2. Voting\n3. Working")
else:
    print("You are elgible for nothing")
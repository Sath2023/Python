new_list = [1,2,3,2,1]
print("The original list : ",new_list)
copy_list = new_list.copy()
copy_list.reverse
print("The copied and reverse list : ",copy_list)
if copy_list == new_list:
    print("It is a palindrome")
else:
    print("Not a palindrome")

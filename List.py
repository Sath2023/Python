new_list = [1,3,4,2,7,8,9,10,6,5]
temp = new_list
print("Original List : ",new_list)
new_list.append(11) # Adds a new element at the end of the list 
print("After appending 11 : ",new_list)
new_list.sort()
print("After sorting the list : ",new_list)
temp.sort(reverse=True) # Sorts the list in descending order
print("After sorting the list in reverse order : ",new_list)
temp.reverse() # Just interchanges the place of first element and the last element
print("After reversing the list : ",new_list)
new_list.insert(0,0)
print("After inserting 0 at the beginning of the list : ",new_list)

random_list = ['a','c','d','b','e']
l = random_list.reverse()
print(l)
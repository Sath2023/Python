sample_list = []
while True:
    ele = int(input("Enter the elements : "))
    if ele == -1:
        break
    sample_list.append(ele)
print(sample_list)
max = sample_list[0]
for i in range(1, len(sample_list)):
    if sample_list[i] > max:
        max = sample_list[i]
print("The max elements in the list : ",max)

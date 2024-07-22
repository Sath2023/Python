# f = open("File Input and Output/practise.txt","w")
# f.write("Hi everyone\nwe are learning File I/O\nusing Java\nI like programming in java")
# f.close()
# print("Writing performed successfully")


# ##SEARCHING FOR JAVA WORD AND CHANGING IT INTO PYTHON 
# with open("File Input and Output/practise.txt","r") as f:
#     data = f.read()
# print(data)
# new_data = data.replace("Java","Python")
# print(new_data)

# with open("File Input and Output/practise.txt","w") as f:
#     f.write(new_data)

# ## CHEC IF THE WORD LEARNING EXCISTS OR NOT 
# def check_for_word():
#     with open("File Input and Output/practise.txt","r") as f:   
#         data = f.read()
#         word = "learning"
#         if(data.find(word) != -1):
#             print("Found")
#         else:
#             print("Not found")

## WRITE A FUNCTION TO CHECK IN WHICH LINE THE WORD LEARNING EXCISTS
def check_for_line():
    word = "learning"
    data = True
    line_no = 1
    with open("File Input and Output/practise.txt","r") as f: 
        while data:
            data = f.readline()
            if (word in data):
                print("The word excists at line number : ",line_no) 
            line_no += 1                

    return -1
check_for_line()
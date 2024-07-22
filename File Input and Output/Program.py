# f = open("File Input and Output/text.txt","r")
# data = f.read()
# print(data)
# lne = f.readline()
# print(type(data))
# print(lne)
# f.close()


# ##WRITING INTO A FILE
# f = open("File Input and Output/write.txt","w")
# f.write("Hello how are you\nThis is the first class\nThis file content are written using Python")
# print("Successfully written onto write.txt")
# f.close()


# f = open("File Input and Output/demo.txt","r+")
# f.write("123")
# print(f.read())
# f.close()

# f = open("File Input and Output/demo.txt","w+")
# f.write("123")
# print(f.read())
# f.close()

import os
os.remove("File Input and Output/write.txt")
print("Deleted successsfully")
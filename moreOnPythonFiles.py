f = open("testFile3.txt")
# f.seek(11)        #Shift the file pointer to the specified position
print(f.tell())
print(f.readline())
# print(f.tell())

print(f.readline())
# print(f.tell())
f.close()
f = open("testFile.txt", "rt")
content = f.read()
print(content)
# print(f.readlines()) #Returns a list object
# print(f.readline())
# print(f.readline())
# print(f.readline())
# content = f.read() #Here, you will get the specified characters of the file.
#
# for line in f:
#     print(line, end="")
# print(content)
# content = f.read(34455)
# print("1", content)
#
# content = f.read(34455)
# print("2", content)
f.close()
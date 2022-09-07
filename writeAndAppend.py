# f = open("testFile2.txt", "w")
# a = f.write("Nirvikar bhai bahut achhe hain\n")
#  print(a)
# f.close()

# f = open("testFile3.txt", "a")
# a = f.write("Nirvikar bhai bahut achhe hain\n")
#  print(a)
# f.close()


# Handle read and write both

f = open("testFile3.txt", "r+")
print(f.read())
f.write("thank you\n")
  

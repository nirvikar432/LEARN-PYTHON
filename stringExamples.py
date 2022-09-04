#Example to store a string in a variable
mystr = "My name is Nirvikar"
print(mystr)
print(mystr[11:19])     #11 included and 19 excluded
print(len(mystr))       #To print length
print(mystr[11:19:1])   #[starting:end+1:skipitr]
print(mystr[::-1])      #Reverse String
print(mystr[-8:])       #Negative indices
print(mystr.isalnum())
print(mystr.isalpha())
print(mystr.isspace())
print(mystr.endswith("Nirvikar"))
print(mystr.count("N"))
print(mystr.capitalize())
print(mystr.upper())
print(mystr.lower())
print(mystr.find("N"))
a = input("Enter Any Sentence:")
b = a.split()
# split function is used
Acronym_word = ""
for i in b:
    Acronym_word = Acronym_word + i[0]
x = Acronym_word.upper()
# upper function is used to captilize the output
print(x)

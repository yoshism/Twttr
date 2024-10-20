text = input("Your text here *")

voyels = ["a", "e", "o", "u", "i", "A", "E", "O", "U", "I"]

i = 0

while i <= 9:
    text_voyels = voyels[i]
    text = text.replace(text_voyels, "")
    i += 1
    
print(text)

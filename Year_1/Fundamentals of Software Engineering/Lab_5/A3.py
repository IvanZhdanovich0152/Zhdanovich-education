text = input("Enter a text: ")

# New York City
# Yanka Kupala State University of Grodno


words = text.split()
abr = ""
for word in words:
    if len(word) >= 3:
        abr += word[0].upper()
    else:continue
print(abr)
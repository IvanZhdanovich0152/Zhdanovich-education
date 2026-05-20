import re

# He jests at scars. That never felt a wound!     Hello, friend! Are you OK?

text = input("Enter a text: ")
sentences = re.split(r'(?<=[.?!])', text)
count = 0

for sentence in sentences:
    count += 1
    while True:
        if "  " not in sentence:
            break
        else:
            sentence = sentence.replace("  ", "")
    print(sentence)

print(f"Предложений в тексте: {count}")

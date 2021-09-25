import random
word=input("Enter the string:")

jumble =""
while word:
    position = random.randrange(len(word))
    jumble += word[position]
    word = word[:position] + word[(position + 1):]
    
print("Jumbled word:",jumble)

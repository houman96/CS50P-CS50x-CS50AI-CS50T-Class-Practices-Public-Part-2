before = input("Input: ")
notgoodlist = ["a", "A", "e", "E", "i", "I", "o", "O", "u", "U"]
afterlist = []
for character in before:
    if character not in notgoodlist:
        afterlist.append(character)

afterstring = "".join(afterlist)
print ("Output: ", afterstring)

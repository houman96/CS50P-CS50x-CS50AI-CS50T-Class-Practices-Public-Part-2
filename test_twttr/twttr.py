def main():
    word = input("Input: ")
    finalword = shorten(word)
    print ("Output:", finalword)


def shorten(word):
    notgoodlist = ["a", "A", "e", "E", "i", "I", "o", "O", "u", "U"]
    afterlist = []
    for character in word:
        if character not in notgoodlist:
            afterlist.append(character)
    afterstring = "".join(afterlist)
    return f"{afterstring}"


if __name__ == "__main__":
    main()
